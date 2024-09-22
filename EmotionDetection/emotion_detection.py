import requests
import json

def emotion_detector(text_to_analyze):

    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    if not text_to_analyze.strip():
        return None
        
    myobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(URL, json=myobj, headers=Headers)

    if response.status_code == 400:
        return None
        
    formatted_response = json.loads(response.text)

    emotions = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)

    emotions['dominant_emotion'] = dominant_emotion

    return emotions