import base64
import json

from scrapers import bbcworld, cnn, reuters, abcnews, bbcbreaking, cbsnews, davos, emarketer, guardiannews, latimes, telegraphnews, usatoday, yahoonews
# import firebase_admin
# from firebase_admin import credentials
from firebase_admin import firestore

# cred = credentials.Certificate('twitter-scraper.json')
# firebase_admin.initialize_app(cred)


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
    print(payload)
    db = firestore.Client()
    doc = None
    if payload['handle'] == 'reuters':
        print('scrape reuters')
        doc = reuters.scrape(payload['url'])
        doc['id'] = payload['id']
        doc['handle'] = payload['handle']
        doc['date'] = payload['date']
        doc['time_stamp'] = payload['time_stamp']

    elif payload['handle'] == 'bbcworld':
        print('scrape bbc')
        doc = bbcworld.scrape(payload['url'])
        doc['id'] = payload['id']
        doc['handle'] = payload['handle']
        doc['date'] = payload['date']
        doc['time_stamp'] = payload['time_stamp']

    elif payload['handle'] == 'ccn':
        print('scrape cnn')
        doc = cnn.scrape(payload['url'])
        doc['id'] = payload['id']
        doc['handle'] = payload['handle']
        doc['date'] = payload['date']
        doc['time_stamp'] = payload['time_stamp']

    elif payload['handle'] == 'abc':
        print('scrape abc')
        doc = abcnews.scrape(payload['url'])
        doc['id'] = payload['id']
        doc['handle'] = payload['handle']
        doc['date'] = payload['date']
        doc['time_stamp'] = payload['time_stamp']

    elif payload['handle'] == 'bbcbreaking':
        print('scrape bbcbreaking')
        doc = bbcbreaking.scrape(payload['url'])
        doc['id'] = payload['id']
        doc['handle'] = payload['handle']
        doc['date'] = payload['date']
        doc['time_stamp'] = payload['time_stamp']

    elif payload['handle'] == 'cbsnews':
        print('scrape cbsnews')
        doc = cbsnews.scrape(payload['url'])
        doc['id'] = payload['id']
        doc['handle'] = payload['handle']
        doc['date'] = payload['date']
        doc['time_stamp'] = payload['time_stamp']

    elif payload['handle'] == 'davos':
        print('scrape davos')
        doc = davos.scrape(payload['url'])
        doc['id'] = payload['id']
        doc['handle'] = payload['handle']
        doc['date'] = payload['date']
        doc['time_stamp'] = payload['time_stamp']

    elif payload['handle'] == 'emarketer':
        print('scrape emarketer')
        doc = emarketer.scrape(payload['url'])
        doc['id'] = payload['id']
        doc['handle'] = payload['handle']
        doc['date'] = payload['date']
        doc['time_stamp'] = payload['time_stamp']

    elif payload['handle'] == 'guardiannews':
        print('scrape guardiannews')
        doc = guardiannews.scrape(payload['url'])
        doc['id'] = payload['id']
        doc['handle'] = payload['handle']

    elif payload['handle'] == 'latimes':
        print('scrape latimes')
        doc = latimes.scrape(payload['url'])
        doc['id'] = payload['id']
        doc['handle'] = payload['handle']
        doc['date'] = payload['date']
        doc['time_stamp'] = payload['time_stamp']

    elif payload['handle'] == 'telegraphnews':
        print('scrape telegraphnews')
        doc = telegraphnews.scrape(payload['url'])
        doc['id'] = payload['id']
        doc['handle'] = payload['handle']
        doc['date'] = payload['date']
        doc['time_stamp'] = payload['time_stamp']

    elif payload['handle'] == 'usatoday':
        print('scrape usatoday')
        doc = usatoday.scrape(payload['url'])
        doc['id'] = payload['id']
        doc['handle'] = payload['handle']
        doc['date'] = payload['date']
        doc['time_stamp'] = payload['time_stamp']


    elif payload['handle'] == 'yahoonews':
        print('scrape yahoonews')
        doc = yahoonews.scrape(payload['url'])
        doc['id'] = payload['id']
        doc['handle'] = payload['handle']
        doc['date'] = payload['date']
        doc['time_stamp'] = payload['time_stamp']

    else:
        print('not yet implemented')
        print(payload['handle'])
        print(payload['url'])

    if doc:
        coll = db.collection("news").document("articles").collection(payload['handle'])
        doc_ref = coll.document(doc['id'])
        doc_ref.set(doc)