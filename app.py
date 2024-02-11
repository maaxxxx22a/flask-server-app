from textblob import TextBlob
from flask import Flask, request, jsonify

app = Flask(__name__)

def preprocess_input(input_text):
    # Convert input text to lowercase
    preprocessed_text = input_text.lower()
    return preprocessed_text

def classify_sentiment(sentiment_score):
    # Classify sentiment based on score
    if sentiment_score > 0.5:
        return 'positive'
    elif sentiment_score < -0.5:
        return 'negative'
    else:
        return 'neutral'

def generate_response(sentiment_label):
    # Generate response based on sentiment label
    if sentiment_label == 'positive':
        return 'It sounds like you are feeling positive about it.'
    elif sentiment_label == 'negative':
        return 'It seems like you are feeling negative about it.'
    else:
        return 'Your sentiment is neutral.'

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    # Receive user input from Pandorabot
    user_input = request.json['user_input']
    
    # Preprocess user input
    preprocessed_input = preprocess_input(user_input)
    
    # Perform sentiment analysis with TextBlob
    sentiment_score = TextBlob(preprocessed_input).sentiment.polarity
    
    # Determine sentiment label based on sentiment score
    sentiment_label = classify_sentiment(sentiment_score)
    
    # Generate response based on sentiment label
    response = generate_response(sentiment_label)
    
    # Return response to Pandorabot
    return jsonify({'response': response, 'sentiment': sentiment_label})

if __name__ == '__main__':
    app.run(debug=True)

