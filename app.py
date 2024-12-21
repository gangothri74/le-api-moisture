import pickle
from flask import Flask,request,jsonify

api=Flask(__name__)

MOISTURE_THRESHOLD=120

with  open('le.pkl','rb') as f:
    le=pickle.load(f)

@api.route('/')
def home():
    return "API Server Running"

@api.route('/predict',methods=['GET'])
def predict():
    moisture_value = request.args.get('moisture_value', type=int)

if moisture_value is None:
        jsonify({'error': 'moisture_value is required'}), 400

return jsonify({'moisture_value': moisture_value, 'motor_status': 'ON' if moisture_value < 50 else 'OFF'})
response=le.predict(data)[0]
return response
if __name__=="__main__":
    api.run(
        host='0.0.0.0',
        port=2000
    )