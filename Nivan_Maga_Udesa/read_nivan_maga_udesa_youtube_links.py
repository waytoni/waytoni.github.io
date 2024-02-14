import sys

# print the original sys.path
print('Original sys.path:', sys.path)

# append a new directory to sys.path
sys.path.append('scripts')

# print the updated sys.path
# print('Updated sys.path:', sys.path)

from helpers import ReadSections
from helpers import *



notes_file = 'Nivan_Maga_Udesa/Nivan_Maga_Udesa_Notes.txt'  
utube_links = 'Nivan_Maga_Udesa/nivan_maga_udesa_youtube_links.txt'
html_file = 'Nivan_Maga_Udesa/index.html'
playlist_url = 'https://www.youtube.com/playlist?list=PLqESXbJ82aIgflkHivXH-cYXlz1onvNCi'

series_title = 'නිවන් මග උදෙසා දර්ශන ඥාණය - දේශනා'

sections = ReadSections(notes_file)

# print(sections)

print(html_file)
PrepareHead(html_file, series_title)

with open(html_file, 'a', encoding='utf-8') as fp:
    fp.write('<h1>නිවන් මග උදෙසා දර්ශන ඥාණය - දේශනා</h1>\n')
    fp.write('<h2>කල්‍යාණ මිත්‍ර අජන්ත සම්පත් ගුරුතුමන් ගේ දේශනා මාලාව</h2>')
    fp.write('<p></p>\n')
    fp.write('<p>සෑම සිකුරාදා සවස 6.00 සිට 8:00 දක්වා</p>\n')
    fp.write('<p><a href="../Nivan_Maga_Udesa/zoom_details.html">Zoom සජීවීව සම්බන්ධ වීමට</a></p>\n')
    fp.write('<p></p>\n')
    fp.write('<h2><li><a href="../Nivan_Maga_Udesa/docs/combined_notes/NMU_file_list.html">නිවන් මග උදෙසා දර්ශන ඥාණය දේශනා සඳහා සටහන්</a></li></h2>\n')
    fp.close()

block_id = ''
idx_prefix = 'A'

HtmlDropdownBlock(block_id, utube_links, series_title, html_file, playlist_url, idx_prefix, sections)

PrepareTail(html_file)
