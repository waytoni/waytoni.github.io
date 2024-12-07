import sys

# print the original sys.path
# print('Original sys.path:', sys.path)

import os
sys.path.append('scripts/py')

# print('Updated sys.path:', sys.path)

from utilities import *
from build_series_menu import *


basepath = 'KalutaraBodhiya/DhammaDiscussions'

base_file = os.path.join(basepath,'ShortDhammaDiscussions_base.html')
notes_file = os.path.join(basepath,'ShortDhammaDiscussions_notes.txt')
utube_links = os.path.join(basepath,'ShortDhammaDiscussions_ytlinks.txt')
html_file = os.path.join(basepath,'ShortDhammaDiscussions.html')
json_file = os.path.join(basepath,'ShortDhammaDiscussions.json')

playlist_url = ''

# series_title = 'කෙටි ධර්ම සාකච්ඡා'
series_title = 'ධර්ම සාකච්ඡා'


ShortDhammaDiscussions_styles = """
   	<style>
		body {
			font-family: Arial, sans-serif;
			margin: 20px;
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

PrepareHeadTop(html_file, series_title, ShortDhammaDiscussions_styles)

with open(html_file, 'a', encoding='utf-8') as fp:
    
    with open(base_file, 'r', encoding='utf-8') as fintro:
        page_base = fintro.read()
        fp.write(page_base)
        fintro.close()
