import sys

# print the original sys.path
print('Original sys.path:', sys.path)

# append a new directory to sys.path
sys.path.append('scripts')

# print the updated sys.path
# print('Updated sys.path:', sys.path)

from helpers import ReadSections
from helpers import *



notes_file_eththapana = 'Suthamaya/suthamaya_eththapana_notes.txt'  
notes_file_mathugama = 'Suthamaya/suthamaya_mathugama_notes.txt'  
utube_links_eththapana = 'Suthamaya/suthamaya_eththapana.txt'
utube_links_mathugama = 'Suthamaya/suthamaya_mathugama.txt'
html_file = 'Suthamaya/index.html'
playlist_url = 'https://www.youtube.com/playlist?list=PLqESXbJ82aIjuYvXqOWBWMs-moFFukBbN'
series_title = 'සුතමයඤාණං - දේශනා'

sections_eththapana = ReadSections(notes_file_eththapana)
sections_mathugama = ReadSections(notes_file_mathugama)

# print(sections)

print(html_file)
PrepareHead(html_file, series_title)

with open(html_file, 'a', encoding='utf-8') as fp:
#    fp.write('<h1>සුතමයඤාණං - ඉත්තෑපාන අක්කර දේශනා</h1>\n')
#    fp.write('<h2>කල්‍යාණ මිත්‍ර අජන්ත සම්පත් ගුරුතුමන් ගේ දේශනා මාලාව</h2>')
    fp.write('<p></p>\n')
    fp.close()

block_id = '1'
idx_prefix = ''
series_title_eththapana = 'සුතමයඤාණං - ඉත්තෑපාන අක්කර දේශනා'
series_title_mathugama = 'සුතමයඤාණං - Sri Sudharshanarama Maha Viharaya Mathugama'

with open(html_file, 'a', encoding="utf-8") as fp:  
    fp.write('<h2>' + str(block_id) + '. ' + series_title_eththapana + '</h2>\n\n')
    fp.close()


HtmlDropdownBlock(1, utube_links_eththapana, series_title_eththapana, html_file, playlist_url, idx_prefix, sections_eththapana)

# block_id = '2'
# with open(html_file, 'a', encoding="utf-8") as fp:  
#     fp.write('<h2>' + str(block_id) + '. ' + series_title_mathugama + '</h2>\n\n')
#     fp.close()
    
# HtmlDropdownBlock(2, utube_links_mathugama, series_title_mathugama, html_file, playlist_url, idx_prefix, sections_mathugama)

PrepareTail(html_file)

#################


