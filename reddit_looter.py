import praw
import requests
import config,os
from RedDownloader import RedDownloader

reddit = praw.Reddit(
    client_id= config.client_id,
    client_secret= config.client_secret,
    user_agent= config.user_agent,
    username= config.username
)

def links():
    x=1
    # Clearing the folder
    for i in os.listdir("bot\\Reddit"):
        os.remove("bot\\Reddit\\" + i)

    for l in os.listdir("bot\\Output"):
        os.remove("bot\\Output\\" + l)

    # Grabbing links
    for submission in reddit.subreddit(config.subreddit).new(limit=None): #can use hot,top,new,rising
        if(x == 10):
            break
        elif (submission.over_18==False and submission.is_video==True):
            urls = submission.url
            link = requests.get(urls).url
            RedDownloader.Download(url = link ,
                                   output="bot\\Reddit\\Output %04i" %x,
                                   quality = 1080)
            x+=1
            print(link)
        else:
            print("NSFW or Image")

    return "Finished Downloading video"