import sys

# print the original sys.path
print('Original sys.path:', sys.path)

# append a new directory to sys.path
sys.path.append('scripts')

# print the updated sys.path
# print('Updated sys.path:', sys.path)

from helpers import ReadSections
from helpers import *



notes_file = 'All_Playlists/I_series_notes.txt'  
utube_links = 'All_Playlists/I_series.txt'
html_file = 'All_Playlists/I_series.html'
playlist_url = 'https://www.youtube.com/playlist?list=PLqESXbJ82aIjuYvXqOWBWMs-moFFukBbN'

series_title = 'කළුතර බෝධි පරිශ්‍රයේදී පැවෙත්වෙන 9වෙනි දේශනා මාලාව'

sections = ReadSections(notes_file)

# print(sections)

print(html_file)
PrepareHead(html_file, series_title)

with open(html_file, 'a', encoding='utf-8') as fp:
    fp.write('<h1>කළුතර බෝධි පරිශ්‍රයේදී පැවෙත්වෙන 9වෙනි දේශනා මාලාව</h1>\n')
    fp.write('<h2>කල්‍යාණ මිත්‍ර අජන්ත සම්පත් ගුරුතුමන් ගේ දේශනා මාලාව</h2>')
    fp.write('<p></p>\n')
    # fp.write('<p>සෑම සිකුරාදා සවස 6.00 සිට 8:00 දක්වා</p>\n')
    # fp.write('<p><a href="../Nivan_Maga_Udesa/zoom_details.html">Zoom සජීවීව සම්බන්ධ වීමට</a></p>\n')
    fp.close()

block_id = ''
idx_prefix = ''

HtmlDropdownBlock(block_id, utube_links, series_title, html_file, playlist_url, idx_prefix, sections)