import sys

# print the original sys.path
# print('Original sys.path:', sys.path)

import os
sys.path.append('scripts/py')

# print('Updated sys.path:', sys.path)

from utilities import *
from build_series_menu import *


basepath = 'AbhidharmaAruth/EP_series'

json_filename = 'AbhidharmaAruth_EP.json'
intro_file = os.path.join(basepath, 'AbhidharmaAruth_EP_intro.html')
notes_file = os.path.join(basepath, 'AbhidharmaAruth_EP_notes.txt')
utube_links = os.path.join(basepath,'AbhidharmaAruth_EP_ytlinks.txt')
json_file = os.path.join(basepath,  json_filename)
html_file = os.path.join(basepath,  'AbhidharmaAruthEP.html')

playlist_url = ''

series_title = 'පොල්ගස්ඕවිට පැවෙත් වුන අභිධර්ම අරුත් දේශනා මාලාව (EP කන්ඩායම)'

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


BuildSeriesPageUsingTemplate(intro_file, series_title, json_filename, html_file)