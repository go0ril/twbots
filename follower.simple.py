from config import api
import random
import time
#TextBlob perform simple natural language processing tasks.
#from textblob import TextBlob

SCREEN_NAME = "go0ril"
#followers = api.get_follower_ids(screen_name=SCREEN_NAME)
#API.search_tweets(q, *, geocode, lang, locale, result_type, count, until, since_id, max_id, include_entities)¶
tags = [
  "برنامه‌نویس","برنامه نویس","برنامه_نویس","نرم‌افزار","نرم افزار","نرم_افزار",
  "erlang",  "ارلنگ",
  "lualang","لوالنگ",
  "pytorch","پایتورچ","هوش مصنوعی",
  "james webb",  "jwst",  "جیمزوب","جیمز وب",
  "python",  "پایتون",
  "github","gitlab","open source","foss","gnu","linux","unix","bsd",
  "develop","programm",
  "quantum","کوانتوم",
  "hack","hacker"," هک ",
]
langs = ["en","fa","tr"]
types = ["popular","recent","mixed"]
followed = [SCREEN_NAME,]

while True:
  tag = random.choice(tags)
  lang = random.choice(langs)
  rtype = random.choice(types)
  tweets = api.search_tweets(tag, count = 1,lang=lang,result_type=rtype)
 
  for tweet in tweets:
    #print(b.__dict__.keys())
    tags_list=[x['text'] for x in tweet.entities.get('hashtags')]
    with open("./twitterbot/tags.txt", "a+") as file_object:
    # Append 'hello' at the end of file
      file_str = file_object.read()
      for t in tags_list:
        if t not in file_str:
          file_object.write(t+"\n")
          print(t," added to taglist.")
    
    if tweet.user.screen_name not in followed:
      followed.append(tweet.user.screen_name)
      print(tweet.user.screen_name," followed")
      api.create_friendship(screen_name=tweet.user.screen_name)
      nsecs=random.randint(5,25)
      time.sleep(nsecs)
    else:
      print(tweet.user.screen_name," ignored")
      time.sleep(2)
    