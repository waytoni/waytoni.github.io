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
# from All_Playlists import waytoni_all_videos

#from ../scripts_new import waytoni_all_videos_new
from All_Playlists import read_utube_links_all
from Nivan_Maga_Udesa import read_nivan_maga_udesa_youtube_links_B
from Suthamaya import read_suthamaya_youtube_links
import sys
sys.path.append('E:/src/github/waytoni_io/waytoni_desktop/scripts_new')
sys.path.append('c:/users/30010651/github/scripts_new')
import waytoni_all_videos_new

Read_Sat2pm_youtube_links
# waytoni_all_videos
waytoni_all_videos_new
read_utube_links_all
read_nivan_maga_udesa_youtube_links_B
read_suthamaya_youtube_links