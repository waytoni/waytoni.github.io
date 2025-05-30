import sys

# print the original sys.path
# print('Original sys.path:', sys.path)

import os
sys.path.append('scripts/py')

# print('Updated sys.path:', sys.path)

from utilities import *


basepath = 'KalutaraBodhiya/I_series'

intro_file = os.path.join(basepath,'I_series_intro.txt')
notes_file = os.path.join(basepath,'I_series_notes.txt')
utube_links = os.path.join(basepath,'I_series.txt')
html_file = os.path.join(basepath,'I_series.html')

playlist_url = 'https://www.youtube.com/playlist?list=PLqESXbJ82aIjuYvXqOWBWMs-moFFukBbN'

series_title = 'කළුතර බෝධියේදී පැවැත්වුන 9වෙනි දේශනා මාලාව (I Series)'

print(intro_file)
print(notes_file)
print(utube_links)
print(html_file)

sections = ReadSections(notes_file)

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

block_id = ''
idx_prefix = ''

HtmlDropdownBlock(block_id, utube_links, series_title, html_file, playlist_url, idx_prefix, sections)

PrepareTail(html_file)