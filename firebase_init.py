import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('projects/directed-will-431806-n0/secrets/Keyjson/versions/1')
firebase_admin.initialize_app(cred)

db = firestore.Client()
