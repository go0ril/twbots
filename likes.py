import urllib.request
import re

def get_user_ids_of_post_likes(post_id):
    try:
        json_data = urllib.request.urlopen('https://twitter.com/i/activity/favorited_popup?id=' + str(post_id)).read()
        json_data = json_data.decode('utf-8')
        found_ids = re.findall(r'data-user-id=\\"+\d+', json_data)
        unique_ids = list(set([re.findall(r'\d+', match)[0] for match in found_ids]))
        return unique_ids

    except urllib.request.HTTPError:
        return False

# Example: 
# https://twitter.com/golan/status/731770343052972032

print (get_user_ids_of_post_likes(731770343052972032))

# ['13520332', '416273351', '284966399']
#
# 13520332 +> @TopLeftBrick
# 416273351 => @Berenger_r
# 284966399 => @FFrink