import pickle
from flask import Flask,request

api=Flask(__name__)

with  open('le.pkl','rb') as f:
    le=pickle.load(f)

@api.route('/')
def home():
    return "API Server Running"

@api.route('/predict',methods=['GET'])
def predict():
    moisture_value = st.number_input('Enter moisture value:', min_value=0, max_value=100, step=1, value=0)
MOISTURE_THRESHOLD = 30

if st.button('Check Motor Status'):
    if moisture_value< MOISTURE_THRESHOLD :
        st.success(f'Moisture = {moisture-sensor}%. Motor: ON')
    else:
        st.info(f'Moisture = {moisture_value}%. Motor: OFF')
if __name__=="__main__":
    api.run(
        host='0.0.0.0',
        port=2000
    )