import base64
import json

import bbcworld
import cnn
import reuters
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('twitter-scraper.json')
firebase_admin.initialize_app(cred)


def run(event, context):
    """Background Cloud Function to be triggered by Pub/Sub.
    Args:
         event (dict):  The dictionary with data specific to this type of
         event. The `data` field contains the PubsubMessage message. The
         `attributes` field will contain custom attributes if there are any.
         context (google.cloud.functions.Context): The Cloud Functions event
         metadata. The `event_id` field contains the Pub/Sub message ID. The
         `timestamp` field contains the publish time.
    """
    payload64 = event['data']
    payloadJson = base64.b64decode(payload64)
    payload = json.loads(payloadJson)

    db = firestore.Client()
    coll = db.collection('news-articles')

    if payload['handle'] == 'reuters':
        print('scrape reuters')
        doc = reuters.scrape(payload['url'])
        doc['id'] = payload['id']
        doc['handle'] = payload['handle']
        doc_ref = coll.document(doc['id'])
        doc_ref.set(doc)
    elif payload['handle'] == 'bbcworld':
        print('scrape bbc')
        doc = bbcworld.scrape(payload['url'])
        doc['id'] = payload['id']
        doc['handle'] = payload['handle']
        doc_ref = coll.document(doc['id'])
        doc_ref.set(doc)
    elif payload['handle'] == 'ccn':
        print('scrape cnn')
        doc = cnn.scrape(payload['url'])
        doc['id'] = payload['id']
        doc['handle'] = payload['handle']
        doc_ref = coll.document(doc['id'])
        doc_ref.set(doc)
    else:
        print('not yet implemented')
        print(payload['handle'])
        print(payload['url'])
