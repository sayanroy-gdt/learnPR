import firebase_admin       #pip install firebase_admin
from firebase_admin import credentials, firestore
import ast
import requests

cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def getImages():    # this function will download the latest image
    docs = db.collection(u'evidence').where(u'type', u'==', u'image').stream()
    for doc in docs:
        dictionary = f'{doc.to_dict()}'
        res = ast.literal_eval(dictionary)
        url = res.get('evidenceUrl')
        response = requests.get(url=url)
        file = open("sample.jpg", "wb")
        file.write(response.content)
        file.close()
        break

def sendDataToFirebase(name):     # this funtion will upload the data
    city_ref = db.collection(u'disaster').document('26.123,91.456')
    city_ref.set({
        u'name': name,
        }, merge=True)

getImages()     # download all images

# PUT YOUR CODE HERE

sendDataToFirebase('Wildfire')      # put the disaster name


