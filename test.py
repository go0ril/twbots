from config import api
#pt = api.home_timeline()
tweets = api.user_timeline(
  screen_name="@go0ril", 
  # 200 is the maximum allowed count
  count=200,
  include_rts = False,
  # Necessary to keep full_text 
  # otherwise only the first 140 words are extracted
  tweet_mode = 'extended'
)
for tweet in tweets:
  get_user_ids_of_post_likes(tweet.id)
  print(
    #tweet.id,
    #tweet.geo,
    #tweet.text,
    #tweet.user.screen_name,
    #tweet.user.location
  )