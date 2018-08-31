import numpy as np
import pandas as pd
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

class Tweet_creds():
    consumer_key = 'insert_code'
    consumer_secret = 'insert_code'
    acess_token = 'insert_code' 
    acess_secret = 'insert_code'
    
class listener(StreamListener):
    def on_data(self, data):
        try: 
            jsonData = json.loads(data)

            if "extended_tweet" in data:
                tweet = jsonData["extended_tweet"]["full_text"]
            if "extended_tweet" not in data:
                tweet = jsonData["text"]
            
            print(tweet)

            save_to_file = '"' + tweet + '",'
            saveFile = open("tweetDB.csv", 'a')
            saveFile.write(save_to_file)
            saveFile.write('\n')
            saveFile.close()

            return True
        except BaseException as e:
            print("Failed on_data,", str(e))
            #time.sleep(5)
    def on_error(self, status):
            print(status)
          
def main():
  tweet_cred = Tweet_creds()
  auth = OAuthHandler(tweet_cred.consumer_key, tweet_cred.consumer_secret)
  auth.set_access_token(tweet_cred.acess_token, tweet_cred.acess_secret)
  twitterStream = Stream(auth, listener())
  twitterStream.filter(track = ["Key_words"])

if __name__ == "__main__":
    main()
