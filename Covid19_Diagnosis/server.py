import fileinput
from flask import Flask , render_template ,Response ,request
import cv2
from werkzeug.utils import secure_filename
import datetime
import time
import json
import os
import cv2
import numpy as np
import pickle
import cv2
import os
from tqdm import tqdm
import pymongo
import cv2
import time
import globals
import Classes_PatientDiagnosis
import database_functions
import Other_Functions

with open('E:/FYP/Covid19_Diagnosis/config.json', 'r') as c:
    params = json.load(c)["params"]
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = params['upload_location']

# This route render homepage
@app.route('/')
def hel():
    return render_template('home.html')

# This route accept data from client side process it and render report web page
@app.route("/uploader", methods=["GET", "POST"])
def uploader():
    try:
        if request.method == "POST":
            f = request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            # print(f.filename)
            img = cv2.imread("E:/FYP/Covid19_Diagnosis/images/" + f.filename)
            current_patinet = Classes_PatientDiagnosis.Patient(request.form["fullname"].upper(),
                                                               int(request.form["age"]), int(request.form["cnic"]),
                                                               request.form.get('gender').upper(), request.form["city"].upper(),
                                                               img, f.filename)
            current_patinet.getCovidTest().classify()
            current_patinet.write()
            # print(current_patinet.getCovidTest().getResult())
            result=current_patinet.getCovidTest().getResult()
            if(result=="REGULAR" or result=="SEVERE"):
                resultheading="Positive"
            else:
                resultheading="Negative"

            return render_template("report.html", name=current_patinet.getName(), cnic=current_patinet.getCnic(),
                                   age=current_patinet.getAge(), city=current_patinet.getcity(),
                                   gender=current_patinet.getGender(),
                                   result=current_patinet.getCovidTest().getResult(),resulthead=resultheading)
    except:
        return "Image is not recieved at server end "


#this route renders stats web page

@app.route("/graph", methods=["GET","POST"])
def moveToGraphPage():
    try:
        control, regular, severe = database_functions.today_cases()
        dates, counts = database_functions.week()
        isl, lhr, kr, pes, others = database_functions.cities()
        return render_template("graphs.html", i=isl, l=lhr, k=kr, p=pes, o=others, m=counts[6], tu=counts[5],
                               w=counts[4],
                               th=counts[3], f=counts[2], sa=counts[1], su=counts[0], c=control, r=regular, s=severe,
                               d1=dates[6], d2=dates[5], d3=dates[4], d4=dates[3], d5=dates[2], d6=dates[1],
                               d7=dates[0])
    except:
        print("<<<<<<<<<<<<<<<< E R R O R >>>>>>>>>>>>>>>>>>>>>>>>>")
        print("Error !!!!!  unable to enter data in database")
        return render_template('error.html')


if __name__ == '__main__':
    app.debug= True
    app.run(host='0.0.0.0')

