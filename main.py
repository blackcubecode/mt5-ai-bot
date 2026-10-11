import time
from src.mt5_connector import MT5Connector
from src.data_handler import DataHandler
from src.ai_model import AIModel

def main():
    mt5 = MT5Connector()
    ai = AIModel()
    
    # 1. Koneksi ke MT5
    if not mt5.connect():
        return

    # 2. Load Model AI yang sudah dilatih
    try:
        ai.load()
    except Exception as e:
        print(e)
        mt5.disconnect()
        return

    print("Bot AI Trading dimulai...")
    
    # 3. Loop utama
    while True:
        try:
            # Ambil data terbaru
            df = mt5.get_historical_data(bars=500)
            if df is None:
                time.sleep(60)
                continue

            # Proses data & indikator
            df = DataHandler.add_indicators(df)
            
            # Ambil data bar terakhir (yang baru saja ditutup)
            latest_bar = df.iloc[[-1]]
            
            # Prediksi AI
            signal = ai.predict(latest_bar)
            print(f"Waktu: {latest_bar['time'].values[0]} | Prediksi AI: {signal}")
            
            # Eksekusi jika ada sinyal
            if signal != 0:
                mt5.execute_trade(signal)
                
            # Tunggu hingga candle berikutnya (misal timeframe M15 = 900 detik)
            # Kita cek setiap 60 detik untuk menghindari spam
            time.sleep(60) 
            
        except KeyboardInterrupt:
            print("Bot dihentikan oleh user.")
            break
        except Exception as e:
            print(f"Terjadi error: {e}")
            time.sleep(60)

    mt5.disconnect()

if __name__ == "__main__":
    main()
