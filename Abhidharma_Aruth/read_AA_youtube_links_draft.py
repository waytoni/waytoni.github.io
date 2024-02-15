# import io
# import shutil
import os
import sys

# sys.path.append('scripts')
sys.path.append(os.path.dirname('scripts'))

from scripts.helpers import ReadSections
from scripts.helpers import *


notes_file_EP = 'Abhidharma_Aruth/AA_EP_notes.txt'  
notes_file_B = 'Abhidharma_Aruth/AA_B_notes.txt'  
utube_links_EP = 'Abhidharma_Aruth/Abhidharma_Aruth_youtube_links.txt'
utube_links_B = 'Abhidharma_Aruth/Abhidharma_Aruth_B_youtube_links.txt'
html_file = 'Abhidharma_Aruth/index.html'
playlist_url_EP = ""
playlist_url_B = ""

series_title = 'අභිධර්ම අරුත් - දේශනා'

sections_EP = ReadSections(notes_file_EP)
sections_B = ReadSections(notes_file_B)

PrepareHead(html_file, series_title)

with open(html_file, 'a', encoding='utf-8') as fp:
    fp.write('<h1>අභිධර්ම අරුත් - දේශනා</h1>\n')
    fp.write('<p></p>\n')
    fp.write('<p>උතුම් සූත්‍ර අභිධර්ම පිටකයන් ට අදාළව, ප්‍රායෝගිකව සදහම් මග ක්‍රමානුකූලව පියවරෙන් පියවර, ලෞකික ජීවිතියෙන් උත්තරීතර නිර්වාණය කරා සරලව විග්‍රහ කෙරෙන උතුම් සදහම් සාකච්ඡා.</p>\n')
    fp.write('<p>බ්‍රහස්පතින්දා ප.ව. 2:00 සිට 4:00 දක්වා</p>\n')
    fp.write('<p>විමසීම්: 0777 047174, 0714 480752</p>\n')
    fp.write('')
    fp.close()  
    
block_id = '1'
series_title_EP = "Abhidharma Aruth"
idx_prefix = 'EP'

with open(html_file, 'a', encoding="utf-8") as fp:  
    fp.write('<h2>' + str(block_id) + '. ' + series_title_EP + '</h2>\n\n')
    fp.close()


HtmlDropdownBlock(1, utube_links_EP, series_title_EP, html_file, playlist_url_EP, idx_prefix, sections_EP)

block_id = '2'
idx_prefix = ''
series_title_B = "Abhidharma Aruth - B"


with open(html_file, 'a', encoding="utf-8") as fp:  
    fp.write('<h2>' + str(block_id) + '. ' + series_title_B + '</h2>\n\n')
    fp.close()
    
HtmlDropdownBlock(2, utube_links_B, series_title_B, html_file, playlist_url_B, idx_prefix, sections_B)

PrepareTail(html_file)

#####################################################


 
    




