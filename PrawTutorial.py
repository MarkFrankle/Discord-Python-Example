import praw

reddit = praw.Reddit(client_id = 'pfT97fO7k9D8PA',
                    client_secret = 'slqFsE3ILsyv05DS55RaJVApzRg',
                    username = 'KingofSpaniards',
                    password = 'King0spain',
                    user_agent = 'prawtutorial')

subreddit = reddit.subreddit('python')

hot_python = subreddit.hot(limit = 9)

for submission in hot_python:
    if(submission.stickied == False):
        print(submission.url)
        # print(dir(submission))
