import sys

# print the original sys.path
# print('Original sys.path:', sys.path)

import os
sys.path.append('scripts/py')

# print('Updated sys.path:', sys.path)

from utilities import *
from build_series_menu import *


basepath = 'AbhidharmaAruth'

intro_file = os.path.join(basepath, 'AbhidharmaAruth_B1_base.html')
notes_file = os.path.join(basepath, 'AbhidharmaAruth_B1_notes.txt')
utube_links = os.path.join(basepath,'AbhidharmaAruth_B1_ytlinks.txt')
json_file = os.path.join(basepath,  'AbhidharmaAruth_B1.json')
html_file = os.path.join(basepath,  'AbhidharmaAruthB1.html')

playlist_url = ''

series_title = 'පොල්ගස්ඕවිට පැවෙත් වුන නිවන් මග උදෙසා දර්ශන ඥාණය දේශනා මාලාව (B කන්ඩායම - පළමු කොටස)'

AA_series_styles = """
   	<style>
		body {
			font-family: Arial, sans-serif;
		}

		p {
			margin: 0px;
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
  
        #sutta {
			margin-left: 20px;
			margin-right: 20px;
        }
		#sutta p {
			text-align: left;
		}

	</style>
"""

print(intro_file)
print(notes_file)
print(utube_links)
print(html_file)
print(json_file)

# build the json file from the youtube links and notes files
BuildDropDownMenuWithNavigation(utube_links, notes_file, json_file)

# PrepareHead(html_file, series_title)
PrepareHeadTop(html_file, series_title, AA_series_styles)

with open(html_file, 'a', encoding='utf-8') as fp:
    
    with open(intro_file, 'r', encoding='utf-8') as fintro:
        page_intro = fintro.read()
        fp.write(page_intro)
        fintro.close()

