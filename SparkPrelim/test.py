import json

input = '{"archived": "true", "author": "xelfer", "body": "Now with new xkcd subreddit!", "controversiality": 0, "created_utc": "1201240417", "downs": 0,  "gilded": 0, "id": "c02zpp2", "link_id": "t3_66k1x", "name": "t1_c02zpp2", "parent_id": "t3_66k1x", "retrieved_on": 1425824816, "score": 2,  "subreddit": "xkcd", "subreddit_id": "t5_2qh0z", "ups": 2}'

txt = json.loads(input)['archived']

print txt

