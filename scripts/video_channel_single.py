from googleapiclient.discovery import build
import isodate
from datetime import datetime
import os
import pytz

basepath = 'All_Playlists'
# Access the secret via the environment variable name used in the YAML file
API_KEY = os.environ.get('AB_API_KEY')

if API_KEY:
    print("Secret loaded successfully!")
else:
    print("Secret not found.")

template_file = "scripts/templates/AllVideos_template.html"
nav_header_file = os.path.join("scripts/templates", "navigation_header_template.html")

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def build_youtube_channel_video_list(video_list_filename, page_title, CHANNEL_ID):
    html_file = os.path.join(basepath, video_list_filename)
    timezone = pytz.timezone('Australia/Sydney')
    now = datetime.now(timezone)
    print(f'{now.strftime("%Y-%m-%d %H:%M:%S  %Z")}')

    channel_id = CHANNEL_ID
    video_details, video_list = get_video_details(channel_id)
    
    if video_list:
        generate_AllVideos_html(video_list, page_title, html_file, now)    
    else:
        print("No video details found or an error occurred.")

def format_duration(seconds):
    """Convert seconds into a formatted string: HH:MM:SS"""
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

def format_date(published_at):
    """Extract and format the date from ISO 8601 datetime"""
    try:
        date = datetime.fromisoformat(published_at.replace("Z", ""))  # Remove 'Z' for compatibility
        return date.strftime('%Y-%m-%d')  # Format as YYYY-MM-DD
    except ValueError:
        return "Unknown"

def get_video_details(channel_id):
    # Build the API client
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)

    try:
        # Get the channel's upload playlist ID
        channel_response = youtube.channels().list(
            part='contentDetails',
            id=channel_id
        ).execute()

        
        # uploads_playlist_id = youtube.channels().list(
        #     part='contentDetails',
        #     id=channel_id
        # ).execute()['items'][0]['contentDetails']['relatedPlaylists']['uploads']
                
        if not channel_response.get('items'):
            print("No channel found with the given ID.")
            return ([], '')

        uploads_playlist_id = channel_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

        # Fetch videos from the uploads playlist
        video_details = []
        next_page_token = None
     
        while True:
            playlist_response = youtube.playlistItems().list(
                part='contentDetails',
                playlistId=uploads_playlist_id,
                maxResults=50,
                pageToken=next_page_token
            ).execute()

            video_ids = [item['contentDetails']['videoId'] for item in playlist_response['items']]

            # Fetch video details
            video_response = youtube.videos().list(
                part='snippet,contentDetails',
                id=','.join(video_ids)
            ).execute()

            print(f"Fetched details for {len(video_response['items'])} videos.")
            print(f"Processing {len(video_response['items'])} videos...")
                       
            for video in video_response['items']:
                title = video['snippet']['title']
                published_at = video['snippet']['publishedAt']
                published_date = format_date(published_at)
                duration = video['contentDetails'].get('duration', '')
                video_id = video['id']
                video_url = f'https://www.youtube.com/watch?v={video_id}'

                # Parse duration using isodate
                if duration:
                    try:
                        parsed_duration = isodate.parse_duration(duration)
                        formatted_duration = format_duration(parsed_duration.total_seconds())
                    except Exception as e:
                        print(f"Error parsing duration for video {video['id']}: {e}")
                        formatted_duration = "Error"
                else:
                    formatted_duration = "Unknown"
                
                video_details.append({
                    'title': title,
                    'url': video_url,
                    'published_date': published_date,
                    'duration_formatted': formatted_duration
                })

            next_page_token = playlist_response.get('nextPageToken')
            if not next_page_token:
                break

        # Build HTML rows with descending index (total → 1)
        total = len(video_details)
        video_list = ''
        for i, v in enumerate(video_details):
            index = total - i
            video_list += (
                f'\t\t<tr><td>{index}. </td>'
                f'<td><a href="{v["url"]}"> {v["title"]}</a></td>'
                f'<td>&nbsp;{v["published_date"]} </td>'
                f'<td> &nbsp;&nbsp;&nbsp;{v["duration_formatted"]}</td></tr>\n'
            )

        return (video_details, video_list)

    except Exception as e:
        print(f"An error occurred: {e}")
        return ([], '')


def generate_AllVideos_html(video_list, page_title, html_file, now):
    # Read the template
    try:
        with open(template_file, 'r', encoding='utf-8') as file:
            template_content = file.read()
    except FileNotFoundError:
        print(f"Error: Template file {template_file} not found.")
        return

    template_content = template_content.replace('$TITLE_VIDEO_LIST$', page_title)
    # Read and replace navigation header
    try:
        with open(nav_header_file, 'r', encoding='utf-8') as file:
            nav_header_content = file.read()
        template_content = template_content.replace('$NAVIGATION_HEADER$', nav_header_content)
    except FileNotFoundError:
        print(f"Error: Navigation header file {nav_header_file} not found.")
        return

    process_time = f'Last updated on: {now.strftime("%Y-%b-%d %H:%M:%S  %Z")}'
    
    template_content = template_content.replace('$PROCESS_TIME$', process_time)
    
    template_content = template_content.replace('$TABLE_CONTENT$', video_list)
    
    # Write the output file
    try:
        with open(html_file, 'w', encoding='utf-8') as file:
            file.write(template_content)
    except Exception as e:
        print(f"Error writing HTML file: {e}")
        





