from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

attrition_model = joblib.load("model/attrition.joblib")
 
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['data']
    prediction = attrition_model.predict(data)
    return jsonify({'prediction': prediction.tolist()})
 
if __name__ == '__main__':
    app.run(debug=True)