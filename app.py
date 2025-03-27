from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# โหลดโมเดล ML ที่เซฟไว้
try:
    with open(r'C:\carbon-footprint-app\carbon_footprint_model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    model = None
    print("Error: carbon_footprint_model.pkl not found.")
except Exception as e:
    model = None
    print(f"Error loading model: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded. Please check the model file.'}), 500

    try:
        data = request.json
        if 'electricity_usage' not in data:
            return jsonify({'error': 'Missing "electricity_usage" in request data.'}), 400

        electricity_usage = float(data['electricity_usage'])

        # ทำนายผลด้วยโมเดล
        prediction = model.predict([[electricity_usage]])[0]

        # คำนวณเทียบเท่าต้นไม้ (สมมติว่า ต้นไม้ 1 ต้นดูดซับ CO2 ได้ 21.77 กิโลกรัมต่อปี)
        trees_equivalent = prediction / 21.77

        return jsonify({
            'carbon_footprint': round(prediction, 2),
            'trees': round(trees_equivalent, 2)
        })
    except ValueError:
        return jsonify({'error': 'Invalid input. Please provide a valid number for "electricity_usage".'}), 400
    except Exception as e:
        return jsonify({'error': f'An error occurred: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True)

    # run คำสั่งนี้
    # python app.py
