from flask import Flask, request, jsonify
from sklearn.externals import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')  # Replace 'model.pkl' with the actual filename/path of your trained model

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    predictions = model.predict(data)
    response = {'predictions': predictions.tolist()}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
