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
    moisture_value = int(request.args.get('moisture_value'))


    if moisture_value is None:
        return jsonify({'error': 'moisture_value is required'}), 400

    
    if moisture_value < MOISTURE_THRESHOLD:
        return jsonify({'moisture_value': moisture_value, 'motor_status': 'ON'})
    else:
        return jsonify({'moisture_value': moisture_value, 'motor_status': 'OFF'})


if __name__=="__main__":
    api.run(
        host='0.0.0.0',
        port=2000
    )