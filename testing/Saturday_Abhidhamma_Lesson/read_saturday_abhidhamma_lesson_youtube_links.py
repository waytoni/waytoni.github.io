import sys

# print the original sys.path
print('Original sys.path:', sys.path)

# append a new directory to sys.path
sys.path.append('assets/py')

# print the updated sys.path
# print('Updated sys.path:', sys.path)

from helpers import ReadSections
from helpers import *



notes_file = 'Saturday_Abhidhamma_Lesson/saturday_abhidhamma_lesson_notes.txt'  
utube_links = 'Saturday_Abhidhamma_Lesson/saturday_abhidhamma_lesson_youtube_links.txt'
html_file = 'Saturday_Abhidhamma_Lesson/index.html'
playlist_url = 'https://www.youtube.com/playlist?list=PLqESXbJ82aIip-TA7Efg5JjwmEDJ95kAx'

series_title = 'තුන්කල්හි වෙනස් නොවන ලොව එකම විශ්ව දර්ශනය - දේශනා'

sections = ReadSections(notes_file)

# print(sections)

print(html_file)
PrepareHead(html_file, series_title)

with open(html_file, 'a', encoding='utf-8') as fp:
    fp.write('<h1>තුන්කල්හි වෙනස් නොවන ලොව එකම විශ්ව දර්ශනය - දේශනා</h1>\n')

    fp.write('<p>මානවයාගේ වැරදි දෘෂ්ඨීන්ගෙන් මුදවා ගැනීමේ අදහසින්, තරුණ දූදරුවන්ට ගැලපෙන පරිදි, Science විෂයට (සම්මුති විද්‍යා විෂයට) ගලපමින් පවත්වන දේශනා මාලාව. සරලව මුල සිට……. </p>\n')
    
    fp.write('<p></p>\n')
    fp.write('<p>සජීවි දේශනා සෑම සෙනසුරාදා සවස 2.00 සිට (ලංකාවේ වේලාවෙන්) <a href="../Zoom_Info/zoom_info.html">Zoom සැසියට සම්බන්ද වීමට</a></p>\n')
    fp.write('<p></p>\n')


    fp.close()

block_id = ''
idx_prefix = 'A'

HtmlDropdownBlock(block_id, utube_links, series_title, html_file, playlist_url, idx_prefix, sections)

PrepareTail(html_file)