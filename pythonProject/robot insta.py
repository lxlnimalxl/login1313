from instapy import InstaPy

session = InstaPy(username="ahmadggman", password="ahmad2121")

session.login()

session.set_relationship_bounds(enabled=True, max_followers=500)

session.set_do_follow(True, percentage=100)

session.like_by_tags(["BMW", "steam"], amount=3)

session.end()








