import sys

# print the original sys.path
# print('Original sys.path:', sys.path)

import os
sys.path.append('scripts/py')

# print('Updated sys.path:', sys.path)

from utilities import *
from build_series_menu import *


basepath = 'NivanMagaUdesaDesana/A_series'

intro_file = os.path.join(basepath,'NivanMagaUdesa_base.html')
notes_file = os.path.join(basepath,'NivanMagaUdesa_Notes.txt')
utube_links = os.path.join(basepath,'NivanMagaUdesa_ytlinks.txt')
#html_file = os.path.join(basepath,'NivanMagaUdesa.html')
html_file = os.path.join(basepath,'index.html')
json_file = os.path.join(basepath,'NivanMagaUdesa.json')

playlist_url = 'https://www.youtube.com/playlist?list=PLqESXbJ82aIgflkHivXH-cYXlz1onvNCi'

series_title = 'නිවන් මග උදෙසා දර්ශන ඥානය දේශනා'

print(intro_file)
print(notes_file)
print(utube_links)
print(html_file)
print(json_file)

# build the json file from the youtube links and notes files
BuildDropDownMenuWithNavigation(utube_links, notes_file, json_file)

simple_style = """
	<style>
		h1,
	 	h2, 
		h3, 
		p, 
		a {
			text-align: center;
		}
	</style>
"""
PrepareHeadTop(html_file, series_title, simple_style)

with open(html_file, 'a', encoding='utf-8') as fp:
    
    with open(intro_file, 'r', encoding='utf-8') as fintro:
        page_intro = fintro.read()
        fp.write(page_intro)
        fintro.close()

