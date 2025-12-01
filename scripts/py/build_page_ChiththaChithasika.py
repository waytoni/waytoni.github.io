import sys

# print the original sys.path
# print('Original sys.path:', sys.path)

import os
sys.path.append('scripts/py')

# print('Updated sys.path:', sys.path)

from utilities import *
from build_series_menu import *


basepath = 'ChiththaChithasika'

base_file = os.path.join(basepath,'ChiththaChithasika_base.html')
style_file = os.path.join(basepath,'ChiththaChithasika_style.txt')
html_file = os.path.join(basepath,'index_old.html')


page_title = 'චිත්ත සහ චෛතසික  Chiththa Saha Chithisika'

print(base_file)
print(style_file)
print(html_file)


PrepareHeadWithSyles(html_file, page_title, style_file)

with open(html_file, 'a', encoding='utf-8') as fp:
    
    with open(base_file, 'r', encoding='utf-8') as fintro:
        page_intro = fintro.read()
        fp.write(page_intro)
        fintro.close()

