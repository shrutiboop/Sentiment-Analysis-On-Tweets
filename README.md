# Sentiment-Analysis-On-Tweets
Analyses tweets as positive negative or neutral.
# Twitter Sentiment Analysis Tool

This project is a Twitter Sentiment Analysis tool that fetches tweets based on a specified keyword and classifies them as positive, negative, or neutral using Natural Language Processing (NLP) techniques.

## Features
- Fetches tweets using the Twitter API
- Cleans and preprocesses the tweet text
- Analyzes the sentiment of tweets using TextBlob
- Saves the analyzed tweets to a CSV file

## Technologies Used
- Python
- Tweepy
- TextBlob
- Pandas

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/twitter-sentiment-analysis.git
    cd twitter-sentiment-analysis
    ```

2. Install the required libraries:

    ```bash
    pip install tweepy nltk textblob scikit-learn python-dotenv
    ```

3. Set up your Twitter API keys:

    - Create a `.env` file in the project directory.
    - Add your Twitter API keys to the `.env` file:

      ```ini
      CONSUMER_KEY=your_consumer_key
      CONSUMER_SECRET=your_consumer_secret
      ACCESS_TOKEN=your_access_token
      ACCESS_TOKEN_SECRET=your_access_token_secret
      ```

## Usage

1. Run the script:

    ```bash
    python sentiment_analysis.py
    ```

2. Enter the keyword you want to search for when prompted.
3. The script will fetch tweets, analyze their sentiment, and save the results to a `tweets_sentiment.csv` file.

