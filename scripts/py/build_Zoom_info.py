import sys

# print the original sys.path
# print('Original sys.path:', sys.path)

import os
sys.path.append('scripts/py')

# print('Updated sys.path:', sys.path)

from utilities import *


basepath = 'Zoom_info'

intro_file_Saturday2pm = os.path.join(basepath,'Zoom_info_Saturday2pm.txt')
intro_file_Saturday4pm = os.path.join(basepath,'Zoom_info_Saturday4pm.txt')
html_file_Saturday2pm = os.path.join(basepath,'zoom_info_Saturday2pm.html')
html_file_Saturday4pm = os.path.join(basepath,'zoom_info_Saturday4pm.html')
intro_file_NMU = os.path.join(basepath,'Zoom_info_NMU.txt')
html_file_NMU = os.path.join(basepath,'zoom_info_NMU.html')

playlist_url = ''

series_title = 'Zoom Info - තුන්කල්හි වෙනස් නොවන ලොව එකම විශ්ව දර්ශනය'

html_file = html_file_Saturday2pm
intro_file = intro_file_Saturday2pm 
print(intro_file)
print(html_file)

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
PrepareTail(html_file)

html_file = html_file_NMU
intro_file = intro_file_NMU
print(intro_file)
print(html_file)

series_title = 'Zoom Info - නිවන් මග උදෙසා දර්ශන ඥාණය'

PrepareHead(html_file, series_title)

with open(html_file, 'a', encoding='utf-8') as fp:
    with open(intro_file, 'r', encoding='utf-8') as fintro:
        page_intro = fintro.read()
        fp.write(page_intro)
        fintro.close()

block_id = ''
idx_prefix = ''
PrepareTail(html_file)

html_file = html_file_Saturday4pm
intro_file = intro_file_Saturday4pm 
print(intro_file)
print(html_file)
series_title = 'Zoom Info - නිවන් මග උදෙසා දර්ශන ඥාණය - සෙනසුරාදා සවස 4.00'

PrepareHead(html_file, series_title)

with open(html_file, 'a', encoding='utf-8') as fp:
    with open(intro_file, 'r', encoding='utf-8') as fintro:
        page_intro = fintro.read()
        fp.write(page_intro)
        fintro.close()

block_id = ''
idx_prefix = ''
PrepareTail(html_file)