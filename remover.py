from config import *
import random
import time
SCREEN_NAME = "@go0ril"
#SCREEN_NAME = "@jikjikuo"
#SCREEN_NAME = "@girdakan"
from twitter_scraper import get_tweets


loop = 0
while True:
  tweets= api.user_timeline(
      screen_name=SCREEN_NAME,count=200,
      )
  
  for status in tweets:
    try:
      #print(dir(status))
      api.destroy_status(status.id)
      txt=" ".join(filter(lambda x: x[0]!="@",status.text.split()))[::-1]
      
      print(txt)
      print ("Deleted:", status.id)
      print("\033[32m°•°•°•°•°•°•°•°•°•°•°•°•°•°\033[39m")
    except Exception as e:
      print ("Failed to delete:", status.id)
      print(e)