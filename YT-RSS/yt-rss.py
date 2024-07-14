#!/usr/bin/python3

import requests, re, feedparser

print('''
    __   _______     ____  ____ ____
    \ \ / |_   _|   |  _ \/ ___/ ___|
     \ V /  | |_____| |_) \___ \___ \\
      | |   | |_____|  _ < ___) ___) |
      |_|   |_|     |_| \_|____|____/
      --------------------------------
 YouTube RSS Link extractor by CiscoSteve42
''')
def extract_channel_rss(url):
    response = requests.get(url)
    html_content = response.text

    channel_id_match = re.search(r'"externalId"\s*:\s*"([^"]+)"', html_content)
    if not channel_id_match:
        print("Channel ID not found.")
        return

    channel_id = channel_id_match.group(1)
    channel_rss = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    return channel_rss

def parse_rss_feed(rss_url):
    feed = feedparser.parse(rss_url)
    channel_title = feed.feed.title
    return channel_title, entries

if __name__ == "__main__":
    youtube_url = input('Enter a a YouTube URL to get rss info from:\n')

    channel_rss_url = extract_channel_rss(youtube_url)
    if channel_rss_url:
        print("RSS Feed URL:", channel_rss_url)
    else:
        print("Failed to extract channel RSS feed URL.")

