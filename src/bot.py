import praw
import os
import re
import json

sub = "SaveRockAndRoll"

client_id = os.environ.get('client_id')
client_secret = os.environ.get('client_secret')
password = os.environ.get('pass')

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     password=password,
                     user_agent='r/RockAndRoll bot',
                     username='SnooPaintings9')

print("It worked!")


moderators = list(reddit.subreddit(sub).moderator())
for submission in reddit.subreddit(sub).new(limit=None):
    reply = "This is a list of links to comments made by moderators in this thread: \n\n "
    editing = ""
    print("Started")
    print(submission.title)
    if(submission.link_flair_text == "News"):
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
            print("Going through comments")
            if (comment.author in moderators and comment.author != "SnooPaintings9"):
                reply +="[Comment by u/{0}](https://reddit.com/r/SaveRockAndRoll/comments/{2}/{3}/{4}/): \n\n>{1} \n\n".format(comment.author, comment.body, submission.id, submission.title, comment.id)
            elif (comment.author == "SnooPaintings9"):
                editing = comment.id
    
        if editing is not "":
            comment = reddit.comment(editing)
            reply += "^Beep ^boop. This is a bot providing a service. If you have any questions, please [contact the moderators](https://www.reddit.com/message/compose?to=/r/SaveRockAndRoll)."
            if(reply == "This is a list of links to comments made by moderators in this thread: \n\n ^Beep ^boop. This is a bot providing a service. If you have any questions, please [contact the moderators](https://www.reddit.com/message/compose?to=/r/SaveRockAndRoll)."):
                comment.edit("No mod comments yet. ")
            else:
                comment.edit(reply)
        else:
            reply += "^Beep ^boop. This is a bot providing a service. If you have any questions, please [contact the moderators](https://www.reddit.com/message/compose?to=/r/SaveRockAndRoll)."
            if(reply == "This is a list of links to comments made by moderators in this thread: \n\n  ^Beep ^boop. This is a bot providing a service. If you have any questions, please [contact the moderators](https://www.reddit.com/message/compose?to=/r/SaveRockAndRoll)."):
                submission.reply("No mod comments yet. ").mod.distinguish(sticky=True)
            else:
                submission.reply(reply).mod.distinguish(sticky=True)
