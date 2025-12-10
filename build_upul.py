# Instructions for updating current set of files
#
# If there is an update (new video) in Kaluthala Bodhiya L series
# then add an entry to the last line of the file: 
#   KalutaraBodhiya/L_series/L_series_ytlinks.txt
#
# If there is an update to the ThalawathugodaB series,
# then add an entry to the last line of the file:
#   NivanMagaUdesaDesana/ThalawathugodaB/ThalawathugodaB_ytlinks.txt
#
# If there is an update to the Abhidharma Aruth D (Polgasowita) series,
# then add an entry to the last line of the file:
#   AbhidharmaAruth/D_series/AbhidharmaAruth_D_ytlinks.txt
#
# All files have the following format
# <index> <optional description> <youtube link (URL)> <date>


# from scripts.py import build_series_ShortDhammaDiscussions


menu_change = False

if menu_change == True:
    from scripts import gen_series_past
    gen_series_past

    #from scripts.py import build_ZoomPage
    #build_ZoomPage
    
    from scripts import gen_notes
    gen_notes
    
    from scripts import gen_SutraList
    gen_SutraList
    
    # The following files are updated using gen_navbar_replace script 
    #'Anichcha_Dukka_Anathma_Series/Anichcha_Dukka_Anathma.html', 
    #'Paramartha_Video/Paramartha_Video.html',
    # 'ChiththaChithasika/index.html'
    from scripts import gen_navbar_replace
    gen_navbar_replace


    # The following files are updated using load-template.js script
    # Paramartha_Video/ParamarthaDarama.html
    # 404.html
    # KalutaraBodhiya/B_C_D_Batches.html
    
    #from scripts.py import build_page_ChiththaChithasika
    #build_page_ChiththaChithasika

    # Update
    # Chithatha_Chithasika (old page), and Vishesha Desana
  
 
#list_AllVideos
from testing import gen_AllVideos
from testing import gen_AllVideos_AA
gen_AllVideos
gen_AllVideos_AA


from scripts import gen_SiyaluDesana
gen_SiyaluDesana
#build_series_ShortDhammaDiscussions

from scripts import gen_homepage
gen_homepage

from scripts import gen_series_current
gen_series_current