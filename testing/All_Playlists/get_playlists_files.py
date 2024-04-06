from pytube import Playlist
import datetime

def get_playlist_list(url,filename):

    # Create a Playlist object
    playlist = Playlist(url)


    # Extract the video links from the playlist and save them to a file
    idx = 1
    with open(filename, "w") as file:
        for video in playlist.videos:
            # file.write(f"{video.watch_url}\n")
            
            # Extract the date uploaded for each video and write it to the file
            date_uploaded = video.publish_date.strftime("%Y-%b-%d")
            # file.write(f"Date Uploaded: {date_uploaded}\n\n")
            
            file.write(str(idx) + ' ' + f"{video.watch_url}" + ' ' + f"{date_uploaded}\n")
            idx = idx + 1
            
    return None
        


# Enter the URL of the playlist you want to scrape
url = "https://www.youtube.com/playlist?list=PLqESXbJ82aIgu16mtfCXK6ChqXQL0KLxh"
filename = "All_Playlists/First_A_Series.txt"

url = "https://www.youtube.com/playlist?list=PLqESXbJ82aIg2hMrX6I1_b5QKxHx3fD0w"
filename = "All_Playlists/Second_B_series.txt"

# url = "https://www.youtube.com/playlist?list=PLqESXbJ82aIj6-LTlyJRJNa3NEgnyeo5z"
# filename = "All_Playlists/annitha_dukka_annaththa.txt"

get_playlist_list(url, filename)
