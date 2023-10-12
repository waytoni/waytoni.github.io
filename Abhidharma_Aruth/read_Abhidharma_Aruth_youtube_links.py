#import io
import shutil
import os
import sys

sys.path.append('E:\src\github\waytoni_io\waytoni_desktop\waytoni.github.io\scripts')
from prepare_html_dropdown_block import prepare_html_dropdown_block_1

text_filename = 'Abhidharma_Aruth/Abhidarma_Aruth_working.txt'
# Uncomment the following line only if everything is okay
html_filename = 'Abhidharma_Aruth/Abhidharma_Aruth_EP.html'

with open(text_filename, 'w', encoding="utf-8") as fp:
    fp.write('<html>\n<head>\n')
    
    with open('scripts/analytics_tag.txt', 'r', encoding="utf-8") as ftag:
        tag_info = ftag.read()
        fp.write(tag_info)
        ftag.close()
        
    fp.write('\n')    
    fp.write('\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    fp.write('\t<link rel="stylesheet" type="text/css" href="A_series.css">\n')
    fp.write('\t<link rel="stylesheet" type="text/css" href="../css/nav_menu.css">\n')
    fp.write('\t<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">\n')
    fp.write('\t<script src="../scripts/menu_function.js"></script>\n')
    fp.write('\t<link rel="icon" type="image/png" href="../images/favicon-16x16.png" sizes="16x16" />\n')
    fp.write('\t<title>අභිධර්ම අරුත් - දේශනා</title>\n')
    
    fp.write('</head>\n<body>\n')
    
    fp.write('<div class="topnav" id="Topnavbar">\n')
    fp.write('<a href="https://waytoni.github.io/" class="active">Home </a>\n') 
    fp.write('<a href="../All_Playlists/සියුලු_දේශනා.html">සියලුම දේශනා </a>\n')
    
    fp.write('<a href="../Paramartha_Video/Paramartha_Video.html">පරමාර්ථ ලෝකය දේශනා </a>\n \
        <a href="../Anichcha_Dukka_Anathma_Series/Anichcha_Dukka_Anathma.html">අනිච්ච, දුක්ඛ, අනත්ත දේශනා </a>\n') 
    fp.write('<a href="../Nivan_Maga_Udesa/index.html">නිවන් මග උදෙසා දේශනා</a>\n')
    fp.write('<a href="../Chithatha_Chithasika/Chiththa_Chithasika.html">චිත්ත සහ චෛතසික</a>\n')
    fp.write('<a href="javascript:void(0);" class="icon" onclick="navFunction()"> <i class="fa fa-bars"></i></a>\n')
    fp.write('</div>\n')
    
    fp.write('<h1>අභිධර්ම අරුත් - දේශනා</h1>\n')

    fp.write('<p>උතුම් සූත්‍ර අභිධර්ම පිටකයන් ට අදාළව, ප්‍රායෝගිකව සදහම් මග ක්‍රමානුකූලව පියවරෙන් පියවර, ලෞකික ජීවිතියෙන් උත්තරීතර නිර්වාණය කරා සරලව විග්‍රහ කෙරෙන උතුම් සදහම් සාකච්ඡා.</p>\n')
    fp.write('<p>බ්‍රහස්පතින්දා ප.ව. 2:00 සිට 4:00 දක්වා</p>\n')
    fp.write('<p>විමසීම්: 0777 047174, 0714 480752</p>\n')
    fp.write('')
    fp.close()  
    
playlist_url_0 = ""
playlist_0 = 'Abhidharma_Aruth/Abhidharma_Aruth_youtube_links.txt'
playlist_title_0 = "Abhidharma Aruth"
idx_prefix_0 = 'EP'

playlist_url_1 = ""
playlist_1 = 'Abhidharma_Aruth/Abhidharma_Aruth_B_youtube_links.txt'
playlist_title_1 = "Abhidharma Aruth - B"
idx_prefix_1 = ''


prepare_html_dropdown_block_1(1, playlist_0, playlist_title_0, text_filename, playlist_url_0, idx_prefix_0)
prepare_html_dropdown_block_1(2, playlist_1, playlist_title_1, text_filename, playlist_url_1, idx_prefix_1)    
 
with open(text_filename, 'a', encoding="utf-8") as fp:  
    fp.write('</body>\n')
    fp.write('</html>\n')
    fp.close()

shutil.copy2(text_filename, html_filename, follow_symlinks=False)
os.remove(text_filename)
