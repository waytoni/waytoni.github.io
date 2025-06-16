import sys

# print the original sys.path
# print('Original sys.path:', sys.path)

import os
sys.path.append('scripts/py')

# print('Updated sys.path:', sys.path)

from utilities import *


basepath = 'Zoom_info'

base_file = os.path.join(basepath,'ZoomInfo_base.html')
html_file = os.path.join(basepath,'ZoomInfo.html')

Tue_base_file = os.path.join(basepath,'ZoomInfoTue_base.html')
Tue_html_file = os.path.join(basepath,'ZoomInfoTue.html')

playlist_url = ''

series_title = 'Zoom Info'

print(base_file)
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
    with open(base_file, 'r', encoding='utf-8') as fintro:
        page_intro = fintro.read()
        fp.write(page_intro)
        fintro.close()

block_id = ''
idx_prefix = ''


PrepareHeadTop(Tue_html_file, series_title, simple_style)

with open(Tue_html_file, 'a', encoding='utf-8') as fp:
    with open(Tue_base_file, 'r', encoding='utf-8') as fintro:
        page_intro = fintro.read()
        fp.write(page_intro)
        fintro.close()

block_id = ''
idx_prefix = ''
# PrepareTail(html_file)

