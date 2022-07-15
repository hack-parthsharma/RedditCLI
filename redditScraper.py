#! usr/bin/env python3

import praw
import prawcore
import time
import math
from dotenv import load_dotenv
import os

class color:
    BOLD = '\033[1m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    END = '\033[0m'

def getData():
    load_dotenv()
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    USER_AGENT = os.getenv("USER_AGENT")
    CLIENT_USERNAME = os.getenv("CLIENT_USERNAME")
    CLIENT_PASSWORD = os.getenv("CLIENT_PASSWORD")

    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT,
        username=CLIENT_USERNAME,
        password=CLIENT_PASSWORD
    )

    desiredSubreddit = input("Enter which subreddit you would like to view:\nr/")
    subreddit = reddit.subreddit(desiredSubreddit)
    numberOfPosts= 10
    try:
        for count, submission in enumerate(subreddit.new(limit=numberOfPosts)):
            if submission.selftext == "":
                body = color.GREEN + submission.url + color.END
            else:
                body = submission.selftext

            print(color.CYAN + "#----------TITLE----------#" + color.END)
            print(color.BOLD + submission.title + color.END + "\n")
            print(color.CYAN + "#----------BODY----------#"+ color.END)
            print(body + "\n")
            print(color.CYAN + "#----------MISC----------#"+ color.END)
            print("Author: {}".format(submission.author))
            print("Upvotes: {}".format(submission.score))
            print("Upvote Ratio: {}\n".format(submission.upvote_ratio))
            userInput = input("Press ENTER to view next, q to quit\n\n\n\n")
            if userInput.strip() == "q":
                print("Exiting CLI for Reddit")
                return
    except prawcore.exceptions.NotFound as error:
        print(color.RED + "404 This is not the subreddit you're looking for...\nbecause it does not exist"+ color.END)

def main():
    startTime = time.time()
    print(color.CYAN + "\n\n#--------------------CLI FOR REDDIT--------------------#\n\n" + color.END)
    getData()
    runTime = math.floor(time.time() - startTime)
    minutes = math.floor(runTime / 60)
    seconds = runTime % 60
    print("You have spent {} minutes and {} seconds on the CLI for Reddit.\n".format(minutes, seconds))

if __name__ == "__main__":
    main()