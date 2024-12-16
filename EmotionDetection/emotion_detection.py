import json
import requests


def emotion_detector(text_to_analyze):
    response = requests.post(
        "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict",
        headers={
            "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        },
        json={
            "raw_document": {
                "text": text_to_analyze,
            },
        }
    )

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    response_dict = json.loads(response.text)
    emotions = response_dict["emotionPredictions"][0]["emotion"]
    emotions["dominant_emotion"] = max(emotions, key=emotions.get)

    return emotions
