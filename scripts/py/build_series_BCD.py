import sys

# print the original sys.path
# print('Original sys.path:', sys.path)

import os
sys.path.append('scripts/py')

# print('Updated sys.path:', sys.path)

from utilities import *
from build_series_menu import *


basepath = 'KalutaraBodhiya'

contents_file = os.path.join(basepath,'B_C_D_Batches_content.html')
html_file = os.path.join(basepath,'B_C_D_Batches.html')

series_title = 'මුල් අභිධම්ම දේශනා කාණ්ඩ B, C, සහ D'


BCD_series_styles = """
   	<style>
		body {
			font-family: Arial, sans-serif;
			margin: 0px;
		}

		p {
            text-align: left;
			margin-left: 10px;
		}
  
        #B_Batch p {
            margin-left: 20px;
        }

	</style>
"""

print(html_file)
print(contents_file)



PrepareHeadTop(html_file, series_title, BCD_series_styles)

with open(html_file, 'a', encoding='utf-8') as fp:
    
    with open(contents_file, 'r', encoding='utf-8') as fintro:
        page_intro = fintro.read()
        fp.write(page_intro)
        fintro.close()

