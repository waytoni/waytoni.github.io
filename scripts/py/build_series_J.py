import sys

# print the original sys.path
# print('Original sys.path:', sys.path)

import os
sys.path.append('scripts/py')

# print('Updated sys.path:', sys.path)

from utilities import *


basepath = 'KalutaraBodhiya/J_series'

intro_file = os.path.join(basepath,'J_series_intro.txt')
notes_file = os.path.join(basepath,'J_series_notes.txt')
utube_links = os.path.join(basepath,'J_series.txt')
html_file = os.path.join(basepath,'J_series.html')

playlist_url = ''

series_title = 'කළුතර බෝධි පරිශ්‍රයේදී පැවෙත්වෙන 2024 වසර සඳහා නිවන් මග උදෙසා දර්ශන ඥාණය දේශනා මාලාව'

print(intro_file)
print(notes_file)
print(utube_links)
print(html_file)

sections = ReadSections(notes_file)

PrepareHead_2ndLevel(html_file, series_title)


with open(html_file, 'a', encoding='utf-8') as fp:
    
    with open(intro_file, 'r', encoding='utf-8') as fintro:
        page_intro = fintro.read()
        fp.write(page_intro)
        fintro.close()

block_id = ''
idx_prefix = ''


# HtmlDropdownBlock(block_id, utube_links, series_title, html_file, playlist_url, idx_prefix, sections)

PrepareTail_2ndLevel(html_file)