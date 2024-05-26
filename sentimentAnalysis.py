import tweepy
import re
from textblob import TextBlob
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def fetch_tweets(keyword, count=100):
    tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang='en').items(count)
    tweets_list = [[tweet.text] for tweet in tweets]
    return tweets_list

def clean_tweet(tweet):
    tweet = re.sub(r'http\S+', '', tweet)
    tweet = re.sub(r'@\S+', '', tweet)
    tweet = re.sub(r'#', '', tweet)
    tweet = re.sub(r'\s+', ' ', tweet)
    return tweet

def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

def get_tweet_sentiments(keyword, count=100):
    tweets = fetch_tweets(keyword, count)
    tweet_sentiments = []

    for tweet in tweets:
        cleaned_tweet = clean_tweet(tweet[0])
        sentiment = analyze_sentiment(cleaned_tweet)
        tweet_sentiments.append({'tweet': cleaned_tweet, 'sentiment': sentiment})

    return tweet_sentiments

def save_to_csv(tweets, filename='tweets_sentiment.csv'):
    df = pd.DataFrame(tweets)
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    keyword = input("Enter the keyword to search for tweets: ")
    tweets = get_tweet_sentiments(keyword)
    save_to_csv(tweets)

    for tweet in tweets:
        print(f"Tweet: {tweet['tweet']}\nSentiment: {tweet['sentiment']}\n")
