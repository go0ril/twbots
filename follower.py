from config import api
import random
import time
#TextBlob perform simple natural language processing tasks.
#from textblob import TextBlob

SCREEN_NAME = "@go0ril"
#followers = api.get_follower_ids(screen_name=SCREEN_NAME)
#API.search_tweets(q, *, geocode, lang, locale, result_type, count, until, since_id, max_id, include_entities)¶
tags = ["python","پایتون"]
langs = ["en","fa","tr"]

friends = api.get_friend_ids(screen_name=SCREEN_NAME)
time.sleep(5)
while True:
  tag = random.choice(tags)
  lang = random.choice(langs)
  tweets = api.search_tweets(tag, count = 10,lang=lang,result_type="recent")
 
  for tweet in tweets:
    #print(b.__dict__.keys())
    if tweet.user.id not in friends:
      print(tweet.user.screen_name," followed")
      api.create_friendship(screen_name=tweet.user.screen_name)
     
    else:
      print(tweet.user.screen_name," ignored")
      
    nsecs=random.randint(5,25)
    time.sleep(nsecs)