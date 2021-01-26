import firebase_admin       #pip install firebase_admin
from firebase_admin import credentials, firestore
import ast

cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def inputDataForQuery():    # this function will give the input data
    final_list = []
    docs = db.collection(u'query').stream()
    for doc in docs:
        dictionary = f'{doc.to_dict()}'
        res = ast.literal_eval(dictionary) 
        values = res.values()
        values_list = list(values) 
        final_list = final_list + values_list
    return final_list

def sendDataToFirebase(food, medic, water, shelter, necessities, donation):     # this funtion will upload the data
    city_ref = db.collection(u'disaster').document('26.123,91.456')
    city_ref.set({
        u'medic': medic,
        u'food': food,
        u'water': water,
        u'shelter': shelter,
        u'necessities': necessities,
        u'donation': donation,
        }, merge=True)

inputDataForQuery()     # take the input data

# PUT YOUR CODE HERE

sendDataToFirebase(90, 80, 30, 40, 50, 60)      # put the respective percentage values


