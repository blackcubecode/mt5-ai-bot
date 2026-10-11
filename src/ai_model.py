import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

class AIModel:
    def __init__(self, model_path="models/ai_trader.pkl"):
        self.model_path = model_path
        self.model = None
        self.feature_columns = [
            'SMA_20', 'SMA_50', 'RSI_14', 
            'MACD_12_26_9', 'MACDs_12_26_9',
            'BBL_5_2.0', 'BBM_5_2.0', 'BBU_5_2.0'
        ]

    def train(self, df):
        print("Melatih model AI...")
        X = df[self.feature_columns]
        y = df['target']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
        self.model.fit(X_train, y_train)

        # Evaluasi
        y_pred = self.model.predict(X_test)
        print(classification_report(y_test, y_pred))

        # Simpan model
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
        joblib.dump(self.model, self.model_path)
        print(f"Model disimpan di {self.model_path}")

    def load(self):
        if not os.path.exists(self.model_path):
            raise FileNotFoundError("Model tidak ditemukan. Silakan lakukan training terlebih dahulu.")
        self.model = joblib.load(self.model_path)

    def predict(self, latest_data):
        # latest_data adalah 1 baris DataFrame terbaru
        X_latest = latest_data[self.feature_columns].values.reshape(1, -1)
        prediction = self.model.predict(X_latest)[0]
        return prediction # 1, -1, atau 0
