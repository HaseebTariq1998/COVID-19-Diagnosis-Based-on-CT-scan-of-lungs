
import time
import globals
import pymongo
import globals
import datetime
import Other_Functions

#query database for positive case in past seven days
def week():
    dates=[]
    count=[]
    dic={}
    mydb = globals.myclient["Covid-19_diagnosis"]
    mycol = mydb["Testing_Results"]
    l=Other_Functions.dates_generator()
    for date in l:
        no = 0
        print(str(date))
        myquery = {"Date": str(date)}
        mydoc = mycol.find(myquery)
        for x in mydoc:
            if x["Result"]=="REGULAR" or x["Result"]=="SEVERE":
                no=no+1
        dic[str(date)]=no
        dates.append(str(date))
        count.append(no)
    #print(dic)
    return  dates,count

# query database to find positive case in different cities
def cities():
    isl=0
    lhr=0
    kr=0
    pes=0
    mydb = globals.myclient["Covid-19_diagnosis"]
    mycol = mydb["Testing_Results"]
    myquery = {"City":"ISLAMABAD"}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        if x["Result"] == "REGULAR" or x["Result"] == "SEVERE":
            isl=isl+1
    myquery = {"City": "LAHORE"}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        if  x["Result"] == "REGULAR" or x["Result"] == "SEVERE":
            lhr = lhr + 1

    myquery = {"City": "KARACHI"}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        if x["Result"] == "REGULAR" or x["Result"] == "SEVERE":
            kr = kr + 1
    myquery = {"City": "PESHAWAR"}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        if x["Result"] == "REGULAR" or x["Result"] == "SEVERE":
            pes = pes + 1
    myquery = {"Result": "REGULAR"}
    reg = mycol.count_documents(myquery)

    myquery = {"Result": "SEVERE"}
    sev = mycol.count_documents(myquery)


    others=(reg+sev)-(isl+lhr+kr+pes)

    #print(isl,lhr,kr,pes,others)
    return isl,lhr,kr,pes,others

# quesry database to find control , regular , and severe cases on current date
def today_cases():
    mydb = globals.myclient["Covid-19_diagnosis"]
    mycol = mydb["Testing_Results"]
    now = datetime.datetime.now()
    date= now.strftime("%Y-%m-%d")
    print(date)
    myquery = {"Date": str(date)}
    mydoc = mycol.find(myquery)
    regular=0
    control=0
    severe=0
    for x in mydoc:
        if x["Result"] == "REGULAR":
            regular=regular+1
        elif x["Result"] == "SEVERE":
            print("h")
            severe=severe+1
        else:
            control=control+1
    print(control,regular,severe)
    return control,regular,severe


