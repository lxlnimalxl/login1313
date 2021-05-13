from instapy import InstaPy

session = InstaPy(username= "haniyeh.py", password= "nimapro8689")
session.login()

session.set_relationship_bounds(enabled= True, max_followers= 200)

session.set_do_follow(True, percentage=100)
session.like_by_tags(["birjand", "بیرجند"], amount= 3)
session.set_dont_like(["nsfw"])

#session.unfollow_users(amount=450, allFollowing=True, sleep_delay=False)

session.end()