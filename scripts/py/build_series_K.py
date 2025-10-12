import sys

# print the original sys.path
# print('Original sys.path:', sys.path)

import os
sys.path.append('scripts/py')

# print('Updated sys.path:', sys.path)

from utilities import *
from build_series_menu import *


basepath = 'KalutaraBodhiya/K_series'

base_file = os.path.join(basepath,'K_series_base.html')
notes_file = os.path.join(basepath,'K_series_notes.txt')
utube_links = os.path.join(basepath,'K_series_ytlinks.txt')
html_file = os.path.join(basepath,'K_series.html')
json_file = os.path.join(basepath,'K_series.json')

playlist_url = ''

series_title = '2025 කළුතර බෝධි පරිශ්‍රයේදී පැවැත්වුන නිවන් මග උදෙසා දර්ශන ඥාණය දේශනා මාලාව (K Series)'

K_series_styles = """
   	<style>
		body {
			font-family: Arial, sans-serif;
		}

		p {
			margin: 0;
		}

		#video-container {
			margin-top: 20px;
		}

		#notes {
			margin-top: 20px;
			white-space: pre-wrap;
		}

		#controls {
			margin-top: 20px;
		}

	</style>
"""

print(base_file)
print(notes_file)
print(utube_links)
print(html_file)
print(json_file)

BuildDropDownMenuWithNavigation(utube_links, notes_file, json_file)

PrepareHeadTop(html_file, series_title, K_series_styles)

with open(html_file, 'a', encoding='utf-8') as fp:
    
    with open(base_file, 'r', encoding='utf-8') as fintro:
        page_base = fintro.read()
        fp.write(page_base)
        fintro.close()
