import tweepy
import random
import schedule
import time
import json
from threading import Thread
from schedule import run_pending
from tweepy import api
from tweepy import Stream
from tweepy.streaming import StreamListener


ACCOUNT_ID = ''  # account id
ACCOUNT_NAME = ''  # needs the accounts @

# everything here is a secret, these are extremely important for the bot to work
consumer_key = ''
consumer_secret = ''

key = ''
secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)



# needed for StreamListener and everything else for the reply code
def setUpAuth():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(key, secret)
    api = tweepy.API(auth)
    return api, auth


# what the bot uses to tweet
def job():
    variable = [
        '',
        '',
        '',
        '',
    ]
    api.update_status(random.choice(variable))


# list of stuff you want your bot to tweet, gonna want a whole lot to avoid duplicate tweets
table = [
    '',
    '',
    '',
    '', ]


# Stream listener
class StdOutListener(StreamListener):
    def on_data(self, data):
        clean_data = json.loads(data)
        tweetId = clean_data["id"]
        tweet = random.choice(table)
        respondToTweet(tweet, tweetId)

        
        
# streams for tweets with account name
def followStream():
    api, auth = setUpAuth()
    listener = StdOutListener()
    stream = Stream(auth, listener)
    stream.filter(track=[ACCOUNT_NAME])


def respondToTweet(tweet, tweetId):
    api, auth = setUpAuth()
    api.update_status(tweet, in_reply_to_status_id=tweetId, auto_populate_reply_metadata=True)

    
    
# tells the bot to tweet every x amount of minutes
def main():
    schedule.every(x).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
    return


# runs both 'main' and 'followStream' so they can both run at the same time without any error
if __name__ == '__main__':
    Thread(target=main).start()
    Thread(target=followStream).start()
