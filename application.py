#!/usr/bin/python3.4
import praw
import http.client
#import re #regex

def trackComment():
    reddit = praw.Reddit(
        user_agent='TrackerBot v1.0',
        client_id='<Reddit app client_id>',
        client_secret='<Reddit app client_secret>',
        username='<Reddit username>',
        password='<Reddit password>')

    subreddit = reddit.subreddit("<sub1+sub2>")

    commentstream = subreddit.stream.comments()

    for comment in commentstream:
        text = comment.body # Fetch body
        if '<Tracked_word>' in text.lower():
        #if re.search("<regex expression>", text.lower()): # Use this if using regex
            author = comment.author # Fetch author
            submissionLink = comment.link_id[3:] # Trim the t3_ at the beginning of the string
            link = "https://www.reddit.com//comments/" + submissionLink + "//" + comment.id # Build comment URL
            message = "New message from : " + str(author) + "\n" + text + "\n" + link # Build bot message content
            sendDiscordMessage(message)

def sendDiscordMessage(message):
    webhook = '<Webhook URL>'

    conn = http.client.HTTPSConnection("discordapp.com")

    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"content\"\r\n\r\n" + message + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"

    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache",
        }

    conn.request("POST", webhook, payload.encode('utf-8'), headers)

    conn.getresponse()
    res = conn.getresponse()
    data = res.read() # Must have read the whole response before you can send a new request to the server
    #print(data.decode("utf-8")) # Response should be empty so no need for that

if __name__ == "__main__":
    trackComment();
