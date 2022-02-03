# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('Random_forest_regression.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        GRE_Score=int(request.form.get("GRE_Score",False))
        TOEFL_Score=float(request.form.get("TOEFL_Score",False))
        University_Rating=int(request.form.get("University_Rating",False))
        SOP=float(request.form.get("SOP",False))
        LOR=float(request.form.get("LOR",False))
        CGPA=float(request.form.get("CGPA",False))
        Research=int(request.form.get("Research",False))
        if GRE_Score> 340 or TOEFL_Score>250 or SOP>5 or LOR>5 or CGPA>10:
            return render_template('index.html',prediction_text="exceeds the value= {}")
        else:
            prediction=model.predict([[GRE_Score,TOEFL_Score,University_Rating,SOP,LOR,CGPA,Research]])
            output=str(round(prediction[0],2))
            #return str(output)
            return render_template('index.html',prediction_text="Chance of Admission = {}".format(output))
       

if __name__=="__main__":
    app.run(debug=True)

