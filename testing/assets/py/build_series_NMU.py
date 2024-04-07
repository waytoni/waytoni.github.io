import sys

# print the original sys.path
# print('Original sys.path:', sys.path)

import os
sys.path.append('assets/py')

# print the updated sys.path
# print('Updated sys.path:', sys.path)

from helpers import ReadSections
from helpers import *


basepath = 'Nivan_Maga_Udesa'

intro_file = os.path.join(basepath,'Nivan_Maga_Udesa_intro.html')
notes_file = os.path.join(basepath,'Nivan_Maga_Udesa_Notes.txt')
utube_links = os.path.join(basepath,'Nivan_Maga_Udesa_youtube_links.txt')
html_file = os.path.join(basepath,'index.html')



playlist_url = 'https://www.youtube.com/playlist?list=PLqESXbJ82aIgflkHivXH-cYXlz1onvNCi'

series_title = 'නිවන් මග උදෙසා දර්ශන ඥාණය - දේශනා'


sections = ReadSections(notes_file)

print(intro_file)
print(notes_file)
print(utube_links)
print(html_file)

sections = ReadSections(notes_file)

PrepareHead(html_file, series_title)


with open(html_file, 'a', encoding='utf-8') as fp:
    
    with open(intro_file, 'r', encoding='utf-8') as fintro:
        page_intro = fintro.read()
        fp.write(page_intro)
        fintro.close()

block_id = ''
idx_prefix = ''

HtmlDropdownBlock(block_id, utube_links, series_title, html_file, playlist_url, idx_prefix, sections)

PrepareTail(html_file)