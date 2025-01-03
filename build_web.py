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


# from scripts.py import build_series_Nivan_Maga_Udesa
from scripts.py import build_series_NivanMagaUdesa
# from scripts.py import build_series_Saturday_Abhidhamma_Lesson
from scripts.py import build_series_AbhidharmaASeries
from scripts.py import build_series_AbhidharmaMulaSita
from scripts.py import build_series_Abhidharma_Aruth
from scripts.py import build_series_AbhidharmaAruth
from scripts.py import build_series_SuthamayaHirigal
from scripts.py import build_series_SiyaluDesana
#from scripts.py import build_series_J_old
from scripts.py import build_series_J


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
    from scripts.py import build_page_ChiththaChithasika
    build_page_ChiththaChithasika
    # Update
    # Chithatha_Chithasika (old page), and Vishesha Desana
    # also update all_videos header
    # KalutharaBodhiya B C D Batches html
    # Zoom info Nivan Maga Udesa, and AbhidhmmaASeries
   


# build_series_Nivan_Maga_Udesa
build_series_NivanMagaUdesa
# build_series_Saturday_Abhidhamma_Lesson
build_series_AbhidharmaASeries
build_series_AbhidharmaMulaSita
build_series_Abhidharma_Aruth
build_series_AbhidharmaAruth
#build_series_J_old
build_series_J
build_series_SuthamayaHirigal
build_series_SiyaluDesana