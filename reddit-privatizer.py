import praw
import time
from datetime import datetime, timedelta

# COMMENT AND POST DELETER SCRIPT
# Create a Reddit app at https://www.reddit.com/prefs/apps
# choose "script" as the app type and fill in the required fields
#
# Rarely the script will stop because of rate limits, just re-run it to continue

# Your Reddit API credentials
CLIENT_ID = 'your client id from reddit'
CLIENT_SECRET = 'your client secret from reddit'
USERNAME = 'your reddit username'
PASSWORD = 'your reddit password'
USER_AGENT = 'Anything you want, for example: "content deleter script"'

# Authenticate
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    username=USERNAME,
    password=PASSWORD,
    user_agent=USER_AGENT
)

# Everything older than 3 days will be deleted, put 0 to delete everything
cutoff = time.time() - (3 * 24 * 60 * 60)

# Delete comments
###############
for comment in reddit.redditor(USERNAME).comments.new(limit=None):
    if comment.created_utc < cutoff:
        print(f"Deleting comment from {datetime.utcfromtimestamp(comment.created_utc)}: {comment.body[:30]}...")
        comment.delete()
###############


# Delete posts
###############
# for submission in reddit.redditor(USERNAME).submissions.new(limit=None):
#     if submission.created_utc < cutoff:
#         print(f"Deleting post from {datetime.utcfromtimestamp(submission.created_utc)}: {submission.title[:30]}...")
#         submission.delete()
###############
