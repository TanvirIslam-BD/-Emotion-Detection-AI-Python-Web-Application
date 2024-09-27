"""
Emotion Detection Server

This script runs a Flask server that allows users to detect emotions
from a given text input using the emotion_detector and emotion_predictor
from the EmotionDetection package.

Routes:
- /emotionDetector: Accepts a 'textToAnalyze' query parameter and returns 
  the detected emotions and the dominant emotion.
- /: Renders the index.html page.

"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
from EmotionDetection.emotion_detection import emotion_predictor

app = Flask("Emotion Detection")

def run_emotion_detection():
    """
    Start the Flask server for emotion detection.
    
    This function starts the Flask server and listens for incoming
    requests on host '0.0.0.0' and port 5123.
    """
    app.run(host="0.0.0.0", port=5000)

@app.route("/emotionDetector")
def sent_detector():
    """
    Emotion detection from a query parameter.
    
    This function retrieves the 'textToAnalyze' parameter from the request,
    passes it to the emotion_detector to get emotion probabilities, and
    formats the response using the emotion_predictor.
    
    Returns:
        str: A formatted string showing the detected emotions and the dominant emotion.
             If the text is invalid, it returns a prompt to retry.
    """
    text_to_detect = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_detect)
    formated_response = emotion_predictor(response)
    if formated_response['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    return (
        f"For the given statement, the system response is 'anger': {formated_response['anger']}, "
        f"'disgust': {formated_response['disgust']}, 'fear': {formated_response['fear']}, "
        f"'joy': {formated_response['joy']}, and 'sadness': {formated_response['sadness']}. "
        f"The dominant emotion is {formated_response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Render the index page.
    
    This function handles the root route and renders the main index
    page (`index.html`) for the emotion detection service.
    
    Returns:
        str: Rendered HTML content of the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    run_emotion_detection()
