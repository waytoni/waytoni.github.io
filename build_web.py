# Instructions for updating current set of files
#
# If there is an update (new video) in Saturday 2:00 pm series,
# then add an entry to the last line of the file: 
#   Kaluthara_Bodhiya_A_Series/Saturday2pm_youtube_links.txt
#
# If there is an update to the I series,
# then add an entry to the last line of the file:
#   All_Playlists/I_series.txt
#
# YouTube links should be saved in the following format
# <index> <youtube link (URL)> <date>

from Kaluthara_Bodhiya_A_Series import Read_Sat2pm_youtube_links
from Saturday_Abhidhamma_Lesson import read_saturday_abhidhamma_lesson_youtube_links
from All_Playlists import read_Iseries
from All_Playlists import read_utube_links_all
from Nivan_Maga_Udesa import read_nivan_maga_udesa_youtube_links
from Suthamaya import read_suthamaya_youtube_links
from Abhidharma_Aruth import read_Abhidharma_Aruth_youtube_links

Read_Sat2pm_youtube_links
read_saturday_abhidhamma_lesson_youtube_links
read_Iseries
read_utube_links_all
read_nivan_maga_udesa_youtube_links
read_suthamaya_youtube_links
read_Abhidharma_Aruth_youtube_links