import sys

# print the original sys.path
# print('Original sys.path:', sys.path)

import os
sys.path.append('scripts/py')

# print('Updated sys.path:', sys.path)

from utilities import *
from build_series_menu import *


basepath = 'KalutaraBodhiya/J_series'

intro_file = os.path.join(basepath,'J_series_intro.txt')
notes_file = os.path.join(basepath,'J_series_notes.txt')
utube_links = os.path.join(basepath,'J_series_new.txt')
# html_file = os.path.join(basepath,'J_series.html')
json_file = os.path.join(basepath,'J_series.json')

playlist_url = ''

series_title = 'නිවන් මග උදෙසා දර්ශන ඥාණය (B කණ්ඩායම) දේශනා මාලාව'

print(intro_file)
print(notes_file)
print(utube_links)
# print(html_file)
print(json_file)

BuildDropDownMenuWithNavigation(utube_links, notes_file, json_file)