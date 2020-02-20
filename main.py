import reuters
import json

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

    payload = event['data']
    print(payload)

    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import firestore

    # Project ID is determined by the GCLOUD_PROJECT environment variable
    # Use the application default credentials
    # cred = credentials.ApplicationDefault()
    # firebase_admin.initialize_app(cred, {
    #   'projectId': project_id,
    # })

    cred = credentials.Certificate('twitter-scraper.json')
    firebase_admin.initialize_app(cred)

    db = firestore.Client()
    coll = db.collection('news-articles')

    if payload['handle'] == 'reuters':
        doc = reuters.scrape(payload['url'])
        doc['id'] = payload['id']
        doc_ref = coll.document(doc['id'])
        doc_ref.set(doc)



# tweet = "impeachment process against Trump https://t.co/FjjrOCMixG https://t.co/DMjh6zLElJ"
# splitted = tweet.split()
# if len(splitted) < 3:
#     print('err')
# else:
#     print(splitted[-2])
#     data = {"url": splitted[-2]}
#     data['handle']='reuters'
#     event = {"data": data}
#     run(event, "")
#
#
# from google.cloud import pubsub_v1
#
# project_id = 'twitter-scraper-265920'
# topic_name = 'web-scraper'
#
# # TODO project_id = "Your Google Cloud Project ID"
# # TODO subscription_name = "Your Pub/Sub subscription name"
# # TODO timeout = 5.0  # "How long the subscriber should listen for
# # messages in seconds"
#
# subscriber = pubsub_v1.SubscriberClient()
# # The `subscription_path` method creates a fully qualified identifier
# # in the form `projects/{project_id}/subscriptions/{subscription_name}`
# subscription_path = subscriber.subscription_path(
#     project_id, "projects/twitter-scraper-265920/subscriptions/web-scraper-subsription")
#
# def callback(message):
#     print("Received message: {}".format(message))
#     message.ack()
#
# streaming_pull_future = subscriber.subscribe(
#     subscription_path, callback=callback
# )
# print("Listening for messages on {}..\n".format(subscription_path))
#
# # result() in a future will block indefinitely if `timeout` is not set,
# # unless an exception is encountered first.
# try:
#     streaming_pull_future.result()
# except:  # noqa
#     streaming_pull_future.cancel()