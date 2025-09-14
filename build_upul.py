# Instructions for updating current set of files
#
# If there is an update (new video) in Kaluthala Bodhiya K lesson series
# then add an entry to the last line of the file: 
#   KalutaraBodhiya/K_series/K_series_ytlinks.txt
#
# If there is an update to the Thalawathugoda series,
# then add an entry to the last line of the file:
#   NivanMagaUdesaDesana/Thalawathugoda/Thalawathugoda_ytlinks.txt
#
# If there is an update to the Abhidharma Aruth C (Polgasowita) series,
# then add an entry to the last line of the file:
#   AbhidharmaAruth/C_series/AbhidharmaAruth_C_ytlinks.txt
#
# All files have the following format
# <index> <optional description> <youtube link (URL)> <date>


from scripts.py import build_series_NivanMagaUdesa

from scripts.py import build_series_AbhidharmaAruth_B2
from scripts.py import build_series_AbhidharmaAruth_C
from scripts.py import build_series_Thalawathugoda
from scripts.py import build_series_SuthamayaHirigal
from scripts.py import build_series_SiyaluDesana

from scripts.py import build_series_L
from scripts.py import build_series_ShortDhammaDiscussions
from scripts.py import build_homepage
from scripts.py import build_series_YouthForTruth

from testing import list_AllVideos_Jan9



import sys
# sys.path.append('E:/src/github/waytoni_io/waytoni_desktop/scripts_new')
# sys.path.append('../scripts_new')
#import waytoni_all_videos_new


menu_change = False

if menu_change == True:
    from scripts.py import build_series_AbhidharmaASeries
    build_series_AbhidharmaASeries
    from scripts.py import build_series_I
    build_series_I
    from scripts.py import build_series_J
    build_series_J
    from scripts.py import build_series_K
    build_series_K
    from scripts.py import build_ZoomPage
    build_ZoomPage
    from scripts.py import build_404Page
    build_404Page
    from scripts.py import build_series_ADA_ParamarthaLokaya
    build_series_ADA_ParamarthaLokaya
    from scripts.py import build_FileListForNotes
    build_FileListForNotes
    from scripts.py import build_page_ChiththaChithasika
    build_page_ChiththaChithasika
    from scripts.py import build_series_BCD
    build_series_BCD
    from scripts.py import build_series_AbhidharmaAruth_EP
    build_series_AbhidharmaAruth_EP
    from scripts.py import build_series_AbhidharmaAruth_B1
    build_series_AbhidharmaAruth_B1
    # Update
    # Chithatha_Chithasika (old page), and Vishesha Desana
  
   
    
   

# waytoni_all_videos_new
#list_AllVideos
list_AllVideos_Jan9
#build_series_AbhidharmaAruth_B2
build_series_AbhidharmaAruth_C
#build_series_NivanMagaUdesa
build_series_Thalawathugoda

build_series_L
#build_series_SuthamayaHirigal
build_series_SiyaluDesana
#build_series_ShortDhammaDiscussions
# build_series_YouthForTruth
build_homepage