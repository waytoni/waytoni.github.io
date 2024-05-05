import sys

# print the original sys.path
# print('Original sys.path:', sys.path)

import os
sys.path.append('scripts/py')

# print the updated sys.path
# print('Updated sys.path:', sys.path)

from utilities import *



basepath = 'Anichcha_Dukka_Anathma_Series'
intro_file = os.path.join(basepath,'Anichcha_Dukka_Anathma_intro.txt')
html_file = os.path.join(basepath,'Anichcha_Dukka_Anathma.html')

playlist_url = ''
series_title = 'අනිච්ච, දුක්ඛ, අනත්ත ප්‍රඥප්ති අර්ථය ඉක්මවූ ධර්මතා අර්ථය'

print(intro_file)
print(html_file)

PrepareHead(html_file, series_title)

with open(html_file, 'a', encoding='utf-8') as fp:
    
    with open(intro_file, 'r', encoding='utf-8') as fintro:
        page_intro = fintro.read()
        fp.write(page_intro)
        fintro.close()

PrepareTail(html_file)


######  Paramartha Video ############

basepath = 'Paramartha_Video'
intro_file = os.path.join(basepath,'Paramartha_Lokaya_intro.txt')
html_file = os.path.join(basepath,'Paramartha_Video.html')

playlist_url = ''
series_title = 'පරමාර්ථ ලෝකය දේශනා'

print(intro_file)
print(html_file)

PrepareHead(html_file, series_title)

with open(html_file, 'a', encoding='utf-8') as fp:
    
    with open(intro_file, 'r', encoding='utf-8') as fintro:
        page_intro = fintro.read()
        fp.write(page_intro)
        fintro.close()

PrepareTail(html_file)