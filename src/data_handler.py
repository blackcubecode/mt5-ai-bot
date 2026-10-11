import pandas as pd
import pandas_ta as ta

class DataHandler:
    @staticmethod
    def add_indicators(df):
        # Menambahkan indikator teknikal
        df.ta.sma(length=20, append=True)
        df.ta.sma(length=50, append=True)
        df.ta.rsi(length=14, append=True)
        df.ta.macd(append=True)
        df.ta.bbands(append=True)
        
        # Drop NaN yang muncul akibat perhitungan indikator awal
        df.dropna(inplace=True)
        return df

    @staticmethod
    def create_target(df, lookahead=5, threshold=0.0005):
        # Membuat label target untuk AI (Supervised Learning)
        # 1 = Buy (harga naik > threshold), -1 = Sell (harga turun > threshold), 0 = Hold
        future_return = df['close'].shift(-lookahead) / df['close'] - 1
        
        df['target'] = 0
        df.loc[future_return > threshold, 'target'] = 1
        df.loc[future_return < -threshold, 'target'] = -1
        
        df.dropna(inplace=True)
        return df
