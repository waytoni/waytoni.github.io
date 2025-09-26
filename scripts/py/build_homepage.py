import sys

# print the original sys.path
# print('Original sys.path:', sys.path)

import os
sys.path.append('scripts/py')

# print('Updated sys.path:', sys.path)

from utilities import *
from build_series_menu import *


basepath = '.'
contentpath = 'Homepage'

base_file = os.path.join(contentpath,'index_base.html')
messages_file = os.path.join(contentpath,'messages.html')
contents_file = os.path.join(contentpath,'homepage_content.html')
html_file = os.path.join(basepath,'index.html')


playlist_url = ''

# series_title = 'පරමාර්ථ ලෝකය – සර්වඥ දේශනා'
series_title = 'Way to Nibbana - අජන්ත සම්පත් ගුරුතුමන් ගේ දේශනා මාලා'

homepage_styles = """
    <!--link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" 
    rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" 
    crossorigin="anonymous"-->
   	<style>
		body {
			font-family: Arial, sans-serif;
		}

		h1, h2, h3, h4, a, p {
			text-align: left;
		}

	</style>
"""
# <h1> පරමාර්ථ ලෝකය </h1>
# <h2>Way to Nibbana - YouTube channel</h2>

homepage_heading = """
    <div id="main_text" style="margin:5px 5px 5px 15px" ;>
        
        <h1>කල්‍යාණ මිත්‍ර අජන්ත සම්පත් ගුරුතුමන් ගේ දේශනා මාලා</h1>
       
"""

print(base_file)
print(messages_file)
print(contents_file)
print(html_file)

PrepareHeadTop(html_file, series_title, homepage_styles)

with open(html_file, 'a', encoding='utf-8') as fp:
    fp.write(homepage_heading)
    with open(messages_file, 'r', encoding='utf-8') as fmessages:
        page_messages = fmessages.read()
        fp.write(page_messages)
        fmessages.close()
    
    with open(contents_file, 'r', encoding='utf-8') as fintro:
        page_base = fintro.read()
        fp.write(page_base)
        fintro.close()
