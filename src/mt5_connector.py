import MetaTrader5 as mt5
import pandas as pd
import time
import os
from dotenv import load_dotenv

load_dotenv()

class MT5Connector:
    def __init__(self):
        self.symbol = os.getenv("SYMBOL", "EURUSD")
        self.lot = float(os.getenv("LOT_SIZE", "0.01"))
        
    def connect(self):
        if not mt5.initialize():
            print(f"initialize() gagal, error code: {mt5.last_error()}")
            return False
        print(f"Terhubung ke MT5. Akun: {mt5.account_info().login}")
        return True

    def get_historical_data(self, timeframe=mt5.TIMEFRAME_M15, bars=1000):
        rates = mt5.copy_rates_from_pos(self.symbol, timeframe, 0, bars)
        if rates is None or len(rates) == 0:
            print("Gagal mengambil data")
            return None
        df = pd.DataFrame(rates)
        df['time'] = pd.to_datetime(df['time'], unit='s')
        return df

    def execute_trade(self, signal):
        # signal: 1 = Buy, -1 = Sell, 0 = Hold
        if signal == 0:
            return

        symbol_info = mt5.symbol_info(self.symbol)
        if not symbol_info.visible:
            mt5.symbol_select(self.symbol, True)

        tick = mt5.symbol_info_tick(self.symbol)
        point = mt5.symbol_info(self.symbol).point
        
        # Tentukan SL dan TP (misal 50 pips)
        sl_tp_distance = 50 * point 

        if signal == 1: # BUY
            price = tick.ask
            sl = price - sl_tp_distance
            tp = price + sl_tp_distance
            order_type = mt5.ORDER_TYPE_BUY
        else: # SELL
            price = tick.bid
            sl = price + sl_tp_distance
            tp = price - sl_tp_distance
            order_type = mt5.ORDER_TYPE_SELL

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": self.symbol,
            "volume": self.lot,
            "type": order_type,
            "price": price,
            "sl": sl,
            "tp": tp,
            "deviation": 20,
            "magic": 123456,
            "comment": "AI Bot Trade",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }

        result = mt5.order_send(request)
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print(f"Gagal order. Error: {result.retcode}")
        else:
            print(f"Order berhasil! Ticket: {result.order}")

    def disconnect(self):
        mt5.shutdown()
