import sys

# print the original sys.path
# print('Original sys.path:', sys.path)

import os
sys.path.append('scripts/py')

# print('Updated sys.path:', sys.path)

from utilities import *
from build_series_menu import *


basepath = '.'
contentpath = 'Homepage'

base_file = os.path.join(contentpath,'index_base.html')
messages_file = os.path.join(contentpath,'messages.html')
contents_file = os.path.join(contentpath,'homepage_content.html')
html_file = os.path.join(basepath,'index.html')


playlist_url = ''

# series_title = 'පරමාර්ථ ලෝකය – සර්වඥ දේශනා'
series_title = 'Way to Nibbana - අජන්ත සම්පත් ගුරුතුමන් ගේ දේශනා මාලා'

homepage_styles = """
    <!--link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" 
    rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" 
    crossorigin="anonymous"-->
   	<style>
    	:root {
            --primary-color: #2c5aa0;
            --secondary-color: #d4af37;
            --accent-color: #8b4513;
            --light-bg: #f8f5f0;
            --dark-text: #333;
            --light-text: #666;
            --border-radius: 8px;
            --shadow: 0 4px 6px rgba(0,0,0,0.1);
            /* --dark-color: #172f53; */
            --dark-color: #5D4037;
        }
        .section_header h1 {
            text-align: center;
            margin-bottom: 0px;
            margin-top: 0px;
        }
        .section_header h2  {
            text-align: center;
            margin-bottom: 0px;
        }
        .section_header h3 {
            text-align: center;
            margin-bottom: 0px;
            margin-top: 0px;
        }
        .section_header h4{
            text-align: center;
            margin-bottom: 0px;
        }
        .section_header p {
            text-align: center;
            margin-bottom: 0px;
            margin-top: 0px;
        }
		body {
			font-family: Arial, sans-serif;
		}

		h1, h2, h3, h4, a, p {
			text-align: left;
		}
    /* For all list items in the first section */
    .section1 h3 {
        font-size: 1.5em;
    }
    .section1 ul li {
    margin-bottom: 10px; /* Adds 10px spacing below each list item */
    font-size: 1.2em;
    }

    /* For all list items in the second section */
    .section2 ul li {
    margin-bottom: 5px; /* Adds 20px spacing below each list item */
    }
    

	</style>
"""
# <h1> පරමාර්ථ ලෝකය </h1>
# <h2>Way to Nibbana - YouTube channel</h2>

homepage_heading = """
    <div id="main_text" style="margin:5px 5px 5px 15px" ;>
    <div class="section_header">
        <p>වසර පහළොවකට අධික කාලයක් මුළුල්ලේ සිට දස දහසක් පිරිසකගේ දහම් ඇස පාදා ගැනීමට උරදුන් කල්‍යාණ මිත්‍ර පින්වත්</p>
        <h1>ගරු අජන්ත සම්පත් ගුරුතුමා</h1>
        <p>මෙහෙයවන</p>
        <h1>නිවන් මග උදෙසා දර්ශන ඥානය</h1>
        <h2>සදහම් දේශනා සහ සාකච්ඡා මාලා</h2>
        <h4>Way to Nibbana - Dhamma Sermon and Discussion Series by</h4>
        <h2>Honourable Ajantha Sampath Guruthuma</h2>
     </div>  
"""

print(base_file)
print(messages_file)
print(contents_file)
print(html_file)

PrepareHeadTop(html_file, series_title, homepage_styles)

with open(html_file, 'a', encoding='utf-8') as fp:
    fp.write(homepage_heading)
    with open(messages_file, 'r', encoding='utf-8') as fmessages:
        page_messages = fmessages.read()
        fp.write(page_messages)
        fmessages.close()
    
    with open(contents_file, 'r', encoding='utf-8') as fintro:
        page_base = fintro.read()
        fp.write(page_base)
        fintro.close()
