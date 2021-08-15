import cv2
import time
import globals
import pymongo
import Other_Functions
import globals
import datetime
class diagnosis:
    def __init__(self,sample,sample_serial):
        self.__sample = sample
        self.__sample_serial=sample_serial
        self.__Date = None
        self.__result = None

    def classify(self):
        now = datetime.datetime.now()
        self.__Date= now.strftime("%Y-%m-%d")
        self.__result=Other_Functions.test(self.__sample)

    def getSample(self):
        return self.__sample
    def getsample_serial(self):
        return self.__sample_serial
    def getDate(self):
        return self.__Date
    def getResult(self):
        return self.__result

    def setSample(self,s):
        self.__sample=s
    def setsample_serial(self,ss):
        self.__sample_serial=ss
    def setDate(self,d):
        self.__Date=d
    def setResult(self,r):
        self.__result=r



class Patient:
    def __init__(self, name, age, cnic, gender, city, sample,sample_serial):
        self.__name = name
        self.__age = age
        self.__cnic = cnic
        self.__gender = gender
        self.__city = city
        self.__covid19_test = diagnosis(sample,sample_serial)

    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def getCnic(self):
        return self.__cnic
    def getGender(self):
        return self.__gender
    def getcity(self):
        return self.__city
    def getCovidTest(self):
        return self.__covid19_test

    def setName(self,n):
        self.__name=n
    def setAge(self,a):
        self.__age=a
    def setCnic(self,c):
        self.__cnic=c
    def setGender(self,g):
        self.__gender=g
    def setcity(self,ci):
        self.__city=ci

    def write(self):
        try:
            mydb = globals.myclient["Covid-19_diagnosis"]
            mycol = mydb["Testing_Results"]
            mydict = {"Cnic": self.__cnic, "Name": self.__name, "Gender": self.__gender, "Age": self.__age,
                      "City": self.__city, "Result": self.__covid19_test.getResult(),
                      "Date": self.__covid19_test.getDate(), "Image": self.__covid19_test.getsample_serial()}
            x = mycol.insert_one(mydict)
        except:
            print("Server Error!!! information is not stored  in database")

