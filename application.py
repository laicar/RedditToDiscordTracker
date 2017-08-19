#!/usr/bin/python3.4
import praw
import http.client

def trackComment(word):
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
        if word in text.lower():
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

    conn.request("POST", webhook, payload, headers)

if __name__ == "__main__":
    trackComment('<Tracked_word>');