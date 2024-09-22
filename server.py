'''
A module that handles the Flask web application for Emotion Detection.
Defines routes for performing emotion analysis and rendering the home page.
'''

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route('/emotionDetector', methods=['GET', 'POST'])
def sent_detector():
    '''
    Handles requests to /emotionDetector for emotion analysis.
    Accepts both GET and POST requests and processes the input text.
    Returns a formatted string response with emotion analysis results.
    '''

    # Initialize text variable
    text = None

    # Process input based on request method
    if request.method == 'POST':
        text = request.form.get('textToAnalyze', None)

    elif request.method == 'GET':
        text = request.args.get('textToAnalyze', None)

    # If text is still None, return an error response
    if not text:
        return "Invalid text! Please try again!"

    # Perform emotion detection
    emotion_data = emotion_detector(text)

    # Check if emotion_data is None (indicating invalid or blank input)
    if emotion_data is None:
        return "Invalid text! Please try again!"

    # Format the response as requested by the customer
    formatted_emotions = (
        f"'anger': {emotion_data['anger']}, 'disgust': {emotion_data['disgust']}, "
        f"'fear': {emotion_data['fear']}, 'joy': {emotion_data['joy']} and "
        f"'sadness': {emotion_data['sadness']}"
    )
    dominant_emotion = emotion_data['dominant_emotion']

    # Create the final output message
    response_message = (
        f"For the given statement, the system response is {formatted_emotions}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    # Return the response message
    return response_message


# Route for the home page (to serve the index.html file)
@app.route('/')
def index():
    '''
    Renders the home page for the web application.
    '''
    return render_template('index.html')


# Run the Flask application
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
