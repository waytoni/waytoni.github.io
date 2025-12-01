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



menu_change = False 

if menu_change == True:
    from scripts import gen_series_past
    gen_series_past

    from scripts.py import build_ZoomPage
    build_ZoomPage
   
    from scripts import gen_notes_v1
    gen_notes_v1
    
    from scripts.py import build_series_BCD
    build_series_BCD
    

from scripts import gen_SiyaluDesana
gen_SiyaluDesana
#build_series_ShortDhammaDiscussions

from scripts import gen_homepage
gen_homepage

from scripts.py import build_homepage
build_homepage

from scripts import gen_series_current
gen_series_current