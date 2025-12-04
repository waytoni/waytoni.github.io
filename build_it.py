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



menu_change = False 

if menu_change == True:
    from scripts import gen_series_past
    gen_series_past

    from scripts.py import build_ZoomPage
    build_ZoomPage
   
    from scripts import gen_notes_v1
    gen_notes_v1
    
    from scripts import gen_SutraList
    gen_SutraList   

    from scripts import gen_SiyaluDesana
    gen_SiyaluDesana
    #build_series_ShortDhammaDiscussions

from scripts import gen_homepage
gen_homepage

from scripts import gen_series_current
gen_series_current