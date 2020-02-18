import reuters




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





    if payload['handle'] == 'reuters':
        doc = reuters.scrape(
            "https://www.reuters.com/article/uk-eu-ryanair-subsidies-idUKKBN20B174?taid=5e4ab64b035a2400014b6715&utm_campaign=trueAnthem:+Trending+Content&utm_medium=trueAnthem&utm_source=twitter")


import re

tweet = " 'I'm exposing your hatred of this president,' Senator Lindsey Graham criticized Democrats for https://francis.com the way they are handling the impeachment process against Trump https://t.co/FjjrOCMixG https://t.co/DMjh6zLElJ fsfdsf"
splitted = re.split(r'(?<=\s)(?=https[^\s]+$)',tweet)
if len(splitted) < 3:
    print('err')
else:
    print(splitted[-2])