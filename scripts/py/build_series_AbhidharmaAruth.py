import sys

# print the original sys.path
# print('Original sys.path:', sys.path)

import os
sys.path.append('scripts/py')

# print('Updated sys.path:', sys.path)

from utilities import *
from build_series_menu import *


basepath = 'AbhidharmaAruth'

intro_file = os.path.join(basepath,'NivanMagaUdesaAbhidharmaVigrahaya_base.html')


notes_file = os.path.join(basepath,'NivanMagaUdesaAbhidharmaVigrahaya_notes.txt')
utube_links = os.path.join(basepath,'NivanMagaUdesaAbhidharmaVigrahaya_ytlinks.txt')
json_file = os.path.join(basepath,'NivanMagaUdesaAbhidharmaVigrahaya.json')


html_file = os.path.join(basepath,'index.html')

playlist_url = ''

series_title = 'නිවන් මග උදෙසා දර්ශන ඥාණය - අභිධර්ම විග්‍රහය'

print(intro_file)
print(notes_file)
print(utube_links)
print(html_file)
print(json_file)

# build the json file from the youtube links and notes files
BuildDropDownMenuWithNavigation(utube_links, notes_file, json_file)

PrepareHead(html_file, series_title)

with open(html_file, 'a', encoding='utf-8') as fp:
    
    with open(intro_file, 'r', encoding='utf-8') as fintro:
        page_intro = fintro.read()
        fp.write(page_intro)
        fintro.close()

