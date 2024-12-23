import pickle
from flask import Flask,request,jsonify

api=Flask(__name__)



with  open('le.pkl','rb') as f:
    le=pickle.load(f)

@api.route('/')
def home():
    return "API Server Running"

@api.route('/predict',methods=['GET'])
def predict():
    data = request.args.get('moisture')
    
    data = int(data)
    x=[[data]]
    response = le.predict(x)[0]
    return response

if __name__=="__main__":
    api.run(
        host='0.0.0.0',
        port=2000
    )