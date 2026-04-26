import os
import sys
sys.path.append('scripts')
from video_channel_single import build_youtube_channel_video_list


video_list_filename = 'AllVideos.html'
page_title = 'සියලුම දේශනා - @WayToNibbana YouTube Channel'
CHANNEL_ID = 'UC63kf7W9KLLCj0jK6HF5PdA'
print(f'Building video channel list for {page_title}...')
build_youtube_channel_video_list(video_list_filename, page_title, CHANNEL_ID)

video_list_filename = 'AllVideos_AA.html'
page_title = 'සියලුම දේශනා - Abhidharma Aruth - අභිධර්ම අරුත් YouTube Channel'
CHANNEL_ID = 'UCHB486800OSZYo-umwIo72w'
print(f'Building video channel list for {page_title}...')
build_youtube_channel_video_list(video_list_filename, page_title, CHANNEL_ID)


