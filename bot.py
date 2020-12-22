  
import tweepy
import random 
import schedule 
import time
from schedule import run_pending
from tweepy import api


consumer_key = ''
consumer_secret = '' 
key = ''
secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth

def job(): 
  variable = [
    '', # add whatever you want your bot to say here like for example 'do yall got laptops'
    '',
    '',
    '']
  api.update_status(random.choice(variable))
  
 if __name__ == '__main__':
  job()

def main():
  schedule.every(30).minutes.do(job)
   while True:
    schedule.run_pending()
    time.sleep(1)
   return

if __name__ == '__main__':
  main()
