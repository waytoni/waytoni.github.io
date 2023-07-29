from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dateutil import parser
import datetime
import pytz

# API_KEY and CHANNEL_ID for waytoni.com
API_KEY = 'AIzaSyCiuhuaoYjef7CIw--bBN_flufdCeT0etg'
# CHANNEL_ID = 'UC9o0X9rR7V-3PQUHxNosIAQ'
CHANNEL_ID = 'UC63kf7W9KLLCj0jK6HF5PdA'

try:
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    # Retrieve the playlist ID of the user's uploaded videos
    uploads_playlist_id = youtube.channels().list(
        part='contentDetails',
        id=CHANNEL_ID
    ).execute()['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    # Retrieve the list of videos in the uploads playlist
    videos = []
    next_page_token = ''
    while next_page_token is not None:
        playlist_items = youtube.playlistItems().list(
            part='snippet',
            playlistId=uploads_playlist_id,
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        videos += playlist_items['items']
        next_page_token = playlist_items.get('nextPageToken')

    # Print the titles of the user's videos
    idx = 1
    with open('All_Playlists/all_videos.txt', 'w', encoding="utf-8") as fp:
        with open('All_playlists/all_videos.html','w',encoding="utf-8") as fph:
            
            with open('All_playlists/all_videos_header.txt','r',encoding="utf-8") as all_video_header:
                fph.write(all_video_header.read())
                all_video_header.close()
                
                
                timezone = pytz.timezone('Australia/Sydney')
                now = datetime.datetime.now(timezone)
            
                fph.write(f'Last updated on: {now.strftime("%Y-%b-%d %H:%M:%S  %Z")} \n')
                fph.write('<br>   \n')
                print(f'{now.strftime("%Y-%m-%d %H:%M:%S  %Z")}')

                for video in videos:
                    title = video['snippet']['title']
                    video_id = video['snippet']['resourceId']['videoId']
                    url = f'https://www.youtube.com/watch?v={video_id}'
                    published_date = parser.parse(video['snippet']['publishedAt'])
                    p_date = published_date.strftime("%Y-%b-%d")
                    print(f'{idx}. {title} ({published_date.date()}) : {url}')
                    # print(video['snippet']['title'])
                    # print(p_date)
                    fp.write(f'{url} {p_date} {title} \n')
                    fph.write(f'<p>{idx}. <a href="{url}"> {title}</a>   Posted on: {p_date}</p>\n')
                    idx = idx + 1
            
            with open('All_playlists/all_videos_footer.txt','r',encoding="utf-8") as all_video_footer:
                fph.write(all_video_footer.read())
                all_video_footer.close()               
        fph.close()
            
    fp.close()

except HttpError as e:
    print('An HTTP error occurred: %s' % e)
