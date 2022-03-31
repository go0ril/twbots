from config import api
import random
import time
SCREEN_NAME = "@go0ril"
followers = api.get_follower_ids(screen_name=SCREEN_NAME)
friends = api.get_friend_ids(screen_name=SCREEN_NAME)


for status in tweepy.Cursor(api.user_timeline).items():
  try:
    
  except:
    print ("Failed to delete:", status.id)
