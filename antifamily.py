# import the module 
import tweepy 
# assign the values accordingly 
consumer_key = "" 
consumer_secret = "" 
access_token = "" 
access_token_secret = "" 
fako_famils_list=[
  "حسین‌زاده روزگذران خوش قلب",
  "شکرالله‌ نژاد دراز کلاء",
  "گرد علی قرکهریزی",
  "النچری چادرچی",
  "میش مست نمکی",
  "گدا",
  "آهی",
  "آژند",
  "مزدور اول",
]
# authorization of consumer key and consumer secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
# set access to user's access key and access secret  
auth.set_access_token(access_token, access_token_secret) 
# calling the api  
api = tweepy.API(auth) 
# the screen_name of the targeted user 
screen_name = "go0ril"
# printing the latest 20 followers of the user 

for follower in api.followers(screen_name):
    if follower.screen_name in fako_famils_list:
        print(follower.screen_name) 