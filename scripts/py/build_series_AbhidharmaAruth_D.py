import sys

# print the original sys.path
# print('Original sys.path:', sys.path)

import os
sys.path.append('scripts/py')

# print('Updated sys.path:', sys.path)

from utilities import *
from build_series_menu import *


basepath = 'AbhidharmaAruth/D_series'

intro_file = os.path.join(basepath, 'AbhidharmaAruth_D_base.html')
intro_file_new = os.path.join(basepath, 'AbhidharmaAruth_D_base_new.html')
notes_file = os.path.join(basepath, 'AbhidharmaAruth_D_notes.txt')
utube_links = os.path.join(basepath,'AbhidharmaAruth_D_ytlinks.txt')
json_file = os.path.join(basepath,  'AbhidharmaAruth_D.json')
html_file = os.path.join(basepath,  'AbhidharmaAruthD.html')
html_file_new = os.path.join(basepath,  'AbhidharmaAruthD_new.html')

playlist_url = ''

series_title = 'පොල්ගස්ඕවිට පැවෙත්වෙන නිවන් මග උදෙසා දර්ශන ඥානය දේශනා මාලාව (D කන්ඩායම)'

AA_series_styles = """
   	<style>
		body {
			font-family: Arial, sans-serif;
		}

		p {
			margin: 0px;
		}

		#video-container {
			margin-top: 20px;
		}

		#notes {
			margin-top: 20px;
			white-space: pre-wrap;
		}

		#controls {
			margin-top: 20px;
		}
  
        #sutta {
			margin-left: 20px;
			margin-right: 20px;
        }
		#sutta p {
			text-align: left;
		}

	</style>
"""


AA_series_styles_new = """
 <style>
        :root {
            --primary-color: #2c5530;
            --secondary-color: #6b8e23;
            --accent-color: #d4af37;
            --light-bg: #f8f9fa;
            --dark-text: #333;
            --light-text: #fff;
            --border-radius: 8px;
            --box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        * {
            box-sizing: border-box;
        }
        
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            color: var(--dark-text);
            line-height: 1.6;
            background-color: #f5f5f5;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 15px;
        }
        
        .hero-section {
            background: linear-gradient(rgba(44, 85, 48, 0.85), rgba(44, 85, 48, 0.85)), 
                        url('/images/buddha-2909937_960_720.png') center/cover no-repeat;
            color: var(--light-text);
            padding: 30px 20px;
            text-align: center;
            margin-bottom: 30px;
            border-radius: 0 0 var(--border-radius) var(--border-radius);
        }
        
        .hero-section h1 {
            margin: 0 0 10px;
            font-size: 1.8rem;
        }
        
        .hero-section p {
            margin: 5px 0;
            font-size: 1rem;
        }
        
        .info-box {
            background-color: white;
            border-radius: var(--border-radius);
            box-shadow: var(--box-shadow);
            padding: 20px;
            margin-bottom: 25px;
        }
        
        .info-box h2 {
            color: var(--primary-color);
            margin-top: 0;
            border-bottom: 2px solid var(--accent-color);
            padding-bottom: 10px;
        }
        
        .info-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 25px;
        }
        
        .info-card {
            background-color: white;
            border-radius: var(--border-radius);
            box-shadow: var(--box-shadow);
            padding: 20px;
        }
        
        .info-card h3 {
            color: var(--primary-color);
            margin-top: 0;
            display: flex;
            align-items: center;
        }
        
        .info-card h3 i {
            margin-right: 10px;
            color: var(--accent-color);
        }
        
        .video-container {
            background-color: white;
            border-radius: var(--border-radius);
            box-shadow: var(--box-shadow);
            padding: 20px;
            margin-bottom: 25px;
        }
        
        .video-controls {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
            flex-wrap: wrap;
            gap: 10px;
        }
        
        .video-selector {
            flex-grow: 1;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 1rem;
        }
        
        .nav-buttons {
            display: flex;
            gap: 10px;
        }
        
        .nav-button {
            background-color: var(--primary-color);
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 1rem;
            transition: background-color 0.3s;
        }
        
        .nav-button:hover {
            background-color: var(--secondary-color);
        }
        
        .youtube-frame {
            width: 100%;
            height: 500px;
            border: none;
            border-radius: var(--border-radius);
        }
        
        .notes-container {
            background-color: white;
            border-radius: var(--border-radius);
            box-shadow: var(--box-shadow);
            padding: 20px;
            margin-bottom: 25px;
        }
        
        .notes-container h3 {
            color: var(--primary-color);
            margin-top: 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .font-control {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .font-slider {
            width: 150px;
        }
        
        .notes-content {
            margin-top: 15px;
            line-height: 1.6;
        }
        
        .resources-list {
            margin: 0;
            padding-left: 20px;
        }
        
        .resources-list li {
            margin-bottom: 8px;
        }
        
        .resources-list a {
            color: var(--secondary-color);
            text-decoration: none;
        }
        
        .resources-list a:hover {
            text-decoration: underline;
        }
        
        @media (max-width: 768px) {
            .info-grid {
                grid-template-columns: 1fr;
            }
            
            .video-controls {
                flex-direction: column;
                align-items: stretch;
            }
            
            .youtube-frame {
                height: 300px;
            }
            
            .hero-section h1 {
                font-size: 1.5rem;
            }
        }
    </style>
    """




print(intro_file)
print(notes_file)
print(utube_links)
print(html_file)
print(json_file)

# build the json file from the youtube links and notes files
BuildDropDownMenuWithNavigation(utube_links, notes_file, json_file)

# PrepareHead(html_file, series_title)
PrepareHeadTop(html_file, series_title, AA_series_styles)
PrepareHeadTop(html_file_new, series_title, AA_series_styles_new)

with open(html_file, 'a', encoding='utf-8') as fp:
    
    with open(intro_file, 'r', encoding='utf-8') as fintro:
        page_intro = fintro.read()
        fp.write(page_intro)
        fintro.close()

with open(html_file_new, 'a', encoding='utf-8') as fp:
    
    with open(intro_file_new, 'r', encoding='utf-8') as fintro:
        page_intro = fintro.read()
        fp.write(page_intro)
        fintro.close()

