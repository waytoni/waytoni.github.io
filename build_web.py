# Instructions for updating current set of files
#
# If there is an update (new video) in Saturday 2:00 pm series,
# then add an entry to the last line of the file: 
#   Saturday_Abhidhamma_Lesson/saturday_abhidhamma_lesson_youtube_links.txt
#
# If there is an update to the J series,
# then add an entry to the last line of the file:
#   KalutharaBodhiya/J_series/J_series.txt
#
# YouTube links should be saved in the following format
# <index> <youtube link (URL)> <date>

# from Kaluthara_Bodhiya_A_Series import Read_Sat2pm_youtube_links
# from Saturday_Abhidhamma_Lesson import read_saturday_abhidhamma_lesson_youtube_links
# from All_Playlists import read_Iseries
# from All_Playlists import read_utube_links_all
# from Nivan_Maga_Udesa import read_nivan_maga_udesa_youtube_links
# from Suthamaya import read_suthamaya_youtube_links
# from Abhidharma_Aruth import read_Abhidharma_Aruth_youtube_links

from scripts.py import build_series_Nivan_Maga_Udesa
from scripts.py import build_series_Saturday_Abhidhamma_Lesson
from scripts.py import build_series_Abidharma_Aruth
from scripts.py import build_series_Suthamaya
from scripts.py import build_series_SiyaluDesana
from scripts.py import build_series_J_old

# Read_Sat2pm_youtube_links
# read_saturday_abhidhamma_lesson_youtube_links
# read_Iseries
# read_utube_links_all
# read_nivan_maga_udesa_youtube_links
# read_suthamaya_youtube_links
# read_Abhidharma_Aruth_youtube_links


menu_change = False

if menu_change == True:
    from scripts.py import build_series_I
    build_series_I
    from scripts.py import build_Zoom_info
    build_Zoom_info
    from scripts.py import build_series_ADA_ParamarthaLokaya
    build_series_ADA_ParamarthaLokaya
    from scripts.py import build_NMU_file_list
    # when new images are added run create_thubnails.py in Nivan_Maga_Udesa.docs.combined_notes
    build_NMU_file_list
    from scripts.py import build_file_list
    # when new images are added run create_thubnails.py in Documents
    build_file_list
    
    # Update
    # Chithatha_Chithasika, and Vishesha Desana
    # also update all_videos header

build_series_Nivan_Maga_Udesa
build_series_Saturday_Abhidhamma_Lesson
build_series_Abidharma_Aruth
build_series_J_old
build_series_Suthamaya
build_series_SiyaluDesana