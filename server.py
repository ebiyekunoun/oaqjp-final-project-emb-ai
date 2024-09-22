from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
@app.route('/emotionDetector', methods=['GET', 'POST'])
def sent_detector():

    if request.method == 'POST':
        text = request.form['textToAnalyze']

    elif request.method == 'GET':
        text = request.args.get('textToAnalyze')

    emotion_data = emotion_detector(text)

    # Format the response as requested by the customer
    formatted_emotions = f"'anger': {emotion_data['anger']}, 'disgust': {emotion_data['disgust']}, 'fear': {emotion_data['fear']}, 'joy': {emotion_data['joy']} and 'sadness': {emotion_data['sadness']}"
    dominant_emotion = emotion_data['dominant_emotion']

     # Create the final output message
    response_message = f"For the given statement, the system response is {formatted_emotions}. The dominant emotion is {dominant_emotion}."

    # Return the response message
    return response_message

# Route for the home page (to serve the index.html file)
@app.route('/')
def index():
    return render_template('index.html')

# Run the Flask application
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)