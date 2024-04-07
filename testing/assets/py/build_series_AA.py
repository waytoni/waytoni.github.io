import sys

# print the original sys.path
# print('Original sys.path:', sys.path)

import os
sys.path.append('assets/py')

# print the updated sys.path
# print('Updated sys.path:', sys.path)

from helpers import ReadSections
from helpers import *

basepath = 'Abhidharma_Aruth'

intro_file = os.path.join(basepath,'Abhidharma_Aruth_intro.html')
notes_file_EP = os.path.join(basepath,'AA_EP_notes.txt')
notes_file_B = os.path.join(basepath,'AA_EP_notes.txt')
html_file = os.path.join(basepath,'index.html')
utube_links_EP = os.path.join(basepath, 'Abhidharma_Aruth_youtube_links.txt')
utube_links_B = os.path.join(basepath, 'Abhidharma_Aruth_B_youtube_links.txt')

playlist_url_EP = ""
playlist_url_B = ""

series_title = 'අභිධර්ම අරුත් - දේශනා'

sections_EP = ReadSections(notes_file_EP)
sections_B = ReadSections(notes_file_B)

print(intro_file)
print(notes_file_EP)
print(notes_file_B)
print(utube_links_EP)
print(utube_links_B)
print(html_file)

PrepareHead(html_file, series_title)

with open(html_file, 'a', encoding='utf-8') as fp:
    
    with open(intro_file, 'r', encoding='utf-8') as fintro:
        page_intro = fintro.read()
        fp.write(page_intro)
        fintro.close()

block_id = ''
idx_prefix = ''

block_id = '1'
series_title_EP = "Abhidharma Aruth"
idx_prefix = 'EP'

with open(html_file, 'a', encoding="utf-8") as fp:  
    fp.write('<h2>' + str(block_id) + '. ' + series_title_EP + '</h2>\n\n')
    fp.close()

HtmlDropdownBlock(1, utube_links_EP, series_title_EP, html_file, playlist_url_EP, idx_prefix, sections_EP)

block_id = '2'
idx_prefix = ''
series_title_B = "Abhidharma Aruth - B"

with open(html_file, 'a', encoding="utf-8") as fp:  
    fp.write('<h2>' + str(block_id) + '. ' + series_title_B + '</h2>\n\n')
    fp.close()
    
HtmlDropdownBlock(2, utube_links_B, series_title_B, html_file, playlist_url_B, idx_prefix, sections_B)

PrepareTail(html_file)