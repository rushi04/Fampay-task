from celery import shared_task
from django.conf import settings
from .models import Video, Channel
import datetime
import requests

# fetch the data from api and save to the database
#
# @param [String] pageToken (default = "") token used for next page
# @param [Integer] count (default = 0) searching upto maximum 5 pages
# @exception create the video object in database if it doesn't exists
def fetch_and_save_data(pageToken="", count = 0):

    url = "https://youtube.googleapis.com/youtube/v3/search"

    params = {
        "key":settings.API_KEYS[0],
        "part": "snippet",
        "q": "cricket",
        "type": "video",
        "order": "date",
        "publishedAfter": (datetime.datetime.now() - datetime.timedelta(days=2)).isoformat() + "Z",
        "pageToken": pageToken
    }
    # hit the api and fetch response
    response = requests.get(url = url, params = params)

    print(response.status_code)

    #save the data if the response has status code 200
    if response.status_code == 200:
        data = response.json()
        nextPageToken = data['nextPageToken']
        next_page = True
        for video in data["items"]:
            try:
                video_obj = Video.objects.get(videoId= video["id"]["videoId"])
                # as orderded by date so the objects of next pages will already exist in the database
                next_page = False
                # if the video is already present we break the loop.
                break
            except Video.DoesNotExist:

                try:
                    channel_obj = Channel.objects.get(channelId = video["snippet"]["channelId"])
                except Channel.DoesNotExist:
                    channel_obj = Channel(
                       channelId = video["snippet"]["channelId"],
                       channelTitle = video["snippet"]["channelTitle"],
                    )
                    channel_obj.save()

                video_obj = Video(
                    videoId = video["id"]["videoId"],
                    title = video["snippet"]["title"],
                    description = video["snippet"]["description"],
                    publishedAt = video["snippet"]["publishedAt"],
                    thumbnail = video["snippet"]["thumbnails"]["default"]["url"],
                    channelId = video["snippet"]["channelId"],
                )
                video_obj.save()

        if next_page and count < 50:
            # limiting the request upto 5 pages
            fetch_and_save_data(pageToken = nextPageToken, count = count + 1)
    
    elif response.status_code == 403:
        # if the status_code is 403 means rate limit excedded
        # now will iterate through other api keys
        first = settings.API_KEYS.pop(0)
        settings.API_KEYS.append(first)
        fetch_and_save_data()

@shared_task(name="fetch_api")
def fetch_api():
    fetch_and_save_data()
