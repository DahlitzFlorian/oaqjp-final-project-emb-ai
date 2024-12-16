"""Flask server for emotion detection."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_detector():
    """Entrypoint for emotion detection."""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    dominant_emotion = response["dominant_emotion"]
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    del response["dominant_emotion"]
    emotions_string = ""
    length = len(response.items())
    for idx, (emotion, value) in enumerate(response.items()):
        emotions_string += f"'{emotion}': {value}"
        if idx == length - 2:
            emotions_string += " and "
        elif idx < length - 2:
            emotions_string += ", "

    # Return a formatted string
    return f"For the given statement, the system response is {emotions_string}. " \
            "The dominant emotion is {dominant_emotion}."


@app.route("/")
def render_index_page():
    """Entrypoint for index page."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
