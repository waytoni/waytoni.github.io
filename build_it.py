# Instructions for updating current set of files
#
# If there is an update (new video) in Saturday 2:00 pm series,
# then add an entry to the last line of the file: 
#   Kaluthara_Bodhiya_A_Series/youtube_links.txt
#
# If there is an update to the H series,
# then add an entry to the last line of the file:
#   All_Playlists/H_series.txt
#
# Both files have the following format
# <index> <youtube link (URL)> <date>

from Kaluthara_Bodhiya_A_Series import Read_Sat2pm_youtube_links
from All_Playlists import waytoni_all_videos
from All_Playlists import read_utube_links_all

Read_Sat2pm_youtube_links
waytoni_all_videos
read_utube_links_all