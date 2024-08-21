import sys

# print the original sys.path
# print('Original sys.path:', sys.path)

import os
sys.path.append('scripts/py')

# print('Updated sys.path:', sys.path)

from utilities import *
from build_series_menu import *






basepath = 'AbhidharmaAruth'

intro_file = os.path.join(basepath,'AbhidharmaAruth_base.html')


notes_file_EP = os.path.join(basepath,'AA_EP_notes.txt')
notes_file_B = os.path.join(basepath,'AA_B_notes.txt')
utube_links_EP = os.path.join(basepath,'AbhidharmaAruthEP_ytlinks.txt')
utube_links_B  = os.path.join(basepath,'AbhidharmaAruthB_ytlinks.txt')
json_file_EP = os.path.join(basepath,'AbhidharmaAruthEP.json')
json_file_B = os.path.join(basepath,'AbhidharmaAruthB.json')

html_file = os.path.join(basepath,'index.html')



playlist_url = ''

series_title = 'අභිධර්ම අරුත් - දේශනා'

print(intro_file)
print(notes_file_EP)
print(notes_file_B)
print(utube_links_EP)
print(utube_links_B)
print(html_file)
print(json_file_EP)
print(json_file_B)

# build the json file from the youtube links and notes files
BuildDropDownMenuWithNavigation(utube_links_EP, notes_file_EP, json_file_EP)

BuildDropDownMenuWithNavigation(utube_links_B, notes_file_B, json_file_B)

PrepareHead(html_file, series_title)

with open(html_file, 'a', encoding='utf-8') as fp:
    
    with open(intro_file, 'r', encoding='utf-8') as fintro:
        page_intro = fintro.read()
        fp.write(page_intro)
        fintro.close()

