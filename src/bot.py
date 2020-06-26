import praw
import os
import re
import json

sub = "BobbbayBots"

client_id = os.environ.get('client_id')
client_secret = os.environ.get('client_secret')
password = os.environ.get('pass')

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     password=password,
                     user_agent='r/RedditsQuests bot',
                     username='SnooMaster9')

print("It worked!")


moderators = list(reddit.subreddit(sub).moderator())
for submission in reddit.subreddit(sub).new(limit=None):
    print("Started")
    print(submission.title)
    submission.comments.replace_more(limit=None)
    if True:
        for comment in submission.comments.list():
            print("Going through comments")
            if (comment.author in moderators):
                if True:
                    reply = 'Mod replies: \n{0}:{1} \n\n^Beep ^boop^.'.format(comment.author, comment.body)
                    submission.reply(reply).mod.distinguish(sticky=True)
                    print("Finished! Breaking...")