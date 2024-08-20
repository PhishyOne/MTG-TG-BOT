import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('/home/chessphishguy/MTG-TG-BOT/key.json')
firebase_admin.initialize_app(cred)

db = firestore.Client()
