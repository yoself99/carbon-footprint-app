# filepath: c:\carbon-footprint-app\train\train_model.py
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# ตัวอย่างข้อมูล
data = np.array([
    [100, 50],
    [200, 100],
    [300, 150],
    [400, 200],
    [500, 250]
])

X = data[:, 0].reshape(-1, 1)  # electricity_usage
y = data[:, 1]  # carbon_footprint

# สร้างโมเดล
model = LinearRegression()
model.fit(X, y)

# บันทึกโมเดล
with open(r'C:\carbon-footprint-app\carbon_footprint_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved successfully!")