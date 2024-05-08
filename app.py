from flask import Flask,render_template,url_for,request
import pickle
import numpy as np 
import pandas as pd 
from sklearn.preprocessing import StandardScaler

model = pickle.load(open('scaler.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        Age = int(request.form["Age"])
        yummy = int(request.form["yummy"])
        convenient = int(request.form["convenient"])
        spicy = int(request.form["spicy"])
        fattening = int(request.form["fattening"])
        greasy = int(request.form["greasy"])
        fast = int(request.form["fast"])
        cheap = int(request.form["cheap"])
        tasty = int(request.form["tasty"])
        expensive = int(request.form["expensive"])
        healthy = int(request.form["healthy"])
        disgusting = int(request.form["disgusting"])
        Gender = int(request.form["Gender"])

        total = [[yummy,convenient,spicy,fattening,greasy,fast,cheap,tasty,expensive,healthy,disgusting]]
        prediction = model.predict(total)
        prediction = int(prediction)
        return render_template('index.html',predict=prediction)

if __name__ == '__main__':
    app.run(debug=True)