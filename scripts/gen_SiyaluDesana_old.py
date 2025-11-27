import sys

# print the original sys.path
# print('Original sys.path:', sys.path)

import os
sys.path.append('scripts/py')

# print the updated sys.path
# print('Updated sys.path:', sys.path)

from utilities import *



basepath = 'All_Playlists'

html_file = os.path.join(basepath,'SiyaluDesanaNew.html')


series_title = 'ගරු අජන්ත සම්පත් ගුරුතුමා මෙහෙයවන සහ මෙහෙයවූ දේශනා සියල්ල'

print(html_file)


def siyalu_desana():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_file = os.path.join(base_dir, 'script', 'templates/SiyuluDesana_template.html ')
    navigation_file = 'scripts/py/navigation_header.html'  # Adjusted path
    # Read template
    try:
        with open(template_file, 'r', encoding='utf-8') as file:
            template_content = file.read()
    except FileNotFoundError:
        print(f"Error: Template file {template_file} not found.")
        return

    # Replace navigation header
    try:
        with open(navigation_file, 'r', encoding='utf-8') as file:
            navigation_content = file.read()
        template_content = template_content.replace('$NAVIGATION_HEADER$', navigation_content)
        print("Successfully replaced navigation header")
    except FileNotFoundError:
        print(f"Error: Navigation file {navigation_file} not found.")
        return
    
    



old_html_file = 'All_Playlists/සියුලු_දේශනා.html'
shutil.copy2(html_file, old_html_file, follow_symlinks=False)