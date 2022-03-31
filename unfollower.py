from config import api
import random
import time
SCREEN_NAME = "@go0ril"
followers = api.get_follower_ids(screen_name=SCREEN_NAME)
friends = api.get_friend_ids(screen_name=SCREEN_NAME)

for f in friends:
    
    print (api.get_user(user_id=f).screen_name, end=": ")  
    if f not in followers:
        #print (f)
        print("\u001b[31mUnfollowed\u001b[0m")
        api.destroy_friendship(user_id=f)
        nsecs=random.random()
        time.sleep(nsecs)
    else:
        print("\u001b[32mIgnored\u001b[0m")
        continue
