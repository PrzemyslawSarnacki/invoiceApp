import os
import pymongo
import pandas as pd
import csv
import json


# This program is made to export old database in form of dbf files
# which were converted to csv format and then converted to json.
# Database in form of JSON files will be inserted to MongoDB 
# local database 
 

myclient = pymongo.MongoClient('mongodb://localhost:27017')
database = myclient.mongotest


def moveCSVToFolder():
    for filename in os.listdir('C:/Users/Przemysław/Desktop/FAKT KOPIA/'):
        file = filename.endswith(".csv")
        if file:
            os.rename(r'C:/Users/Przemysław/Desktop/FAKT KOPIA/' + filename,
                      r'C:/Users/Przemysław/Desktop/FAKT KOPIA/CSV/' + filename)


def convertToJSON(filename):
    df = pd.read_csv(r'C:/Users/Przemysław/Desktop/FAKT KOPIA/CSV/' + filename + '.csv', sep=';',
                     decimal=',', engine='python')  # loading csv file
    print(df)
    # saving to json file
    df.to_json(r'C:/Users/Przemysław/Desktop/FAKT KOPIA/JSON/' + filename + '.json', orient='records', force_ascii=False)


# When the Parser Exception raises we use default pandas engine 
def altconvertToJSON(filename):
    df = pd.read_csv(r'C:/Users/Przemysław/Desktop/FAKT KOPIA/CSV/' + filename + '.csv', sep=';',
                     decimal=',', engine='c')  # loading csv file
    print(df)
    # saving to json file
    df.to_json(r'C:/Users/Przemysław/Desktop/FAKT KOPIA/JSON/' + filename + '.json', orient='records', force_ascii=False)


def pushToMongoDB(filename):
    collection = database[filename]
    # adding json to collection
    jdf = open(r'C:/Users/Przemysław/Desktop/FAKT KOPIA/JSON/' + filename + '.json').read()  # loading the json file
    data = json.loads(jdf)  # reading json file
    print(data)
    collection.insert_many(data)


def grabCSV():
    list_ = ['.'.join(x.split('.')[:-1]) for x in os.listdir(r'C:/Users/Przemysław/Desktop/FAKT KOPIA/CSV/') if
             os.path.isfile(os.path.join(r'C:/Users/Przemysław/Desktop/FAKT KOPIA/CSV/', x))]
    print(list_)
    for filename in list_:
        print(filename)
        pushToMongoDB(filename)
        try:
            convertToJSON(filename)
            pushToMongoDB(filename)
        except UnicodeDecodeError:
            print(filename + "nie wrzucony")
        except:
            altconvertToJSON(filename)
            pushToMongoDB(filename)


# moveCSVToFolder()
# file = 'PZZAW'
# convertToJSON(file)
# pushToMongoDB(file)
grabCSV()
