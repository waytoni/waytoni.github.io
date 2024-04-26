import sys

# print the original sys.path
# print('Original sys.path:', sys.path)

import os
sys.path.append('scripts/py')

# print the updated sys.path
# print('Updated sys.path:', sys.path)

from utilities import *



basepath = 'All_Playlists'

intro_file = os.path.join(basepath,'SiyaluDesana_intro.html')


utube_links_EP = os.path.join(basepath,'Abhidharma_Aruth_youtube_links.txt')
utube_links_B = os.path.join(basepath,'Abhidharma_Aruth_B_youtube_links.txt')
html_file = os.path.join(basepath,'SiyaluDesana.html')

playlist_url_EP = ''
playlist_url_B = ''

series_title = 'අභිධම්ම දේශනා  - සියල්ල'

print(intro_file)
print(html_file)


# PrepareHead(html_file, series_title)

##### prepare head for Siyalu Desana
with open(html_file, 'w', encoding="utf-8") as fp:
    fp.write('<html>\n<head>\n')
    
    with open('scripts/analytics_tag.txt', 'r', encoding="utf-8") as ftag:
        tag_info = ftag.read()
        fp.write(tag_info)
        ftag.close()
    
    with open('scripts/py/favicon_temp.html', 'r', encoding="utf-8") as ffavicon:
        favicon_info = ffavicon.read()
        fp.write(favicon_info)
        ffavicon.close()
    
    fp.write('\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    fp.write('\t<link rel="stylesheet" type="text/css" href="../css/nav_menu.css">\n')
    fp.write('\t<link rel="stylesheet" type="text/css" href="../css/dp_block.css">\n')
    #fp.write('\t<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">\n')
    fp.write('\t<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css" integrity="sha512-+4zCK9k+qNFUR5X+cKL9EIR+ZOhtIloNl9GIKS57V1MyNsYpYcUrUeQc9vNfzsWfV28IaLL3i96P9sdNyeRssA==" crossorigin="anonymous" />\n')
    fp.write('\t<script src="../scripts/nav_function.js"></script>\n')
    fp.write('\t<script src="../scripts/jquery-3.7.1.min.js"></script>\n')
    fp.write('\t<script src="../scripts/dp_function.js"></script>\n')
    fp.write('\t<body style="font-family:calibri;"></body>\n')
    fp.write('\t<link rel="icon" type="image/png" href="../images/favicon-16x16.png" sizes="16x16" />\n')
    fp.write('\t<title>අභිධම්ම දේශනා  - සියල්ල</title>\n')
    
    fp.write('</head>\n<body>\n')

    with open('scripts/py/navigation_header_1stLevel.html', 'r', encoding="utf-8") as fnavbar:
        navbar_info = fnavbar.read()
        fp.write(navbar_info)
        fnavbar.close()

    fp.write('<h1>අභිධම්ම දේශනා  - සියල්ල</h1>\n')
    
    fp.write('<h2><li><a href="../documents/file_list.html">සියලු අභිධම්ම දේශනා සඳහා සටහන්</a></li></h2>\n')
    # fp.write('<br>\n')
    
    fp.close()

### 1st

with open(html_file, 'a', encoding="utf-8") as fp:
    #fp.write('<br>\n')
    fp.write('<div class="normal-head">\n')
    fp.write('<h2>1. <a href="../Saturday_Abhidhamma_Lesson/index.html">තුන්කල්හි වෙනස් නොවන ලොව එකම විශ්ව දර්ශනය දේශනා මාලාව</a></h2>\n')
    fp.write('</div>\n')
    fp.close()
    
#### 2nd

with open(html_file, 'a', encoding="utf-8") as fp:
    #fp.write('<br>\n')
    fp.write('<div class="normal-head">\n')
    fp.write('<h2>2. <a href="../Nivan_Maga_Udesa/index.html">නිවන් මග උදෙසා දර්ශන ඥාණය දේශනා මාලාව (A කණ්ඩායම)</a></h2>\n')
    fp.write('</div>\n')
    fp.close()

#### 3rd 
playlist_3 = 'Abhidharma_Aruth/Abhidharma_Aruth_youtube_links.txt'
playlist_title_3 = "Abhidharma Aruth"
series_title_3 = "අභිධර්ම අරුත් දේශනා මාලාව"
HtmlDropdownBlockNoSections(3, playlist_3, playlist_title_3, html_file, '', 'EP', series_title_3)

#### 4th
playlist_4 = 'Abhidharma_Aruth/Abhidharma_Aruth_B_youtube_links.txt'
playlist_title_4 = "Abhidharma Aruth - B"
series_title_4 = "අභිධර්ම අරුත් - B දේශනා මාලාව"
HtmlDropdownBlockNoSections(4, playlist_4, playlist_title_4, html_file, '', '', series_title_4)

#### 5th
playlist_url_5 = ''
playlist_5 = 'Suthamaya/suthamaya_eththapana.txt'
playlist_title_5 = "සුතමයඤාණං - ඉත්තෑපාන අක්කර"
series_title_5 = "සුතමයඤාණං දේශනා මාලාව - ඉත්තෑපාන අක්කර"
HtmlDropdownBlockNoSections(5, playlist_5, playlist_title_5, html_file, '', '', series_title_5)

##### 6th
with open(html_file, 'a', encoding="utf-8") as fp:
    #fp.write('<br>\n')
    fp.write('<div class="normal-head">\n')
    fp.write('<h2>6. <a href="../KalutaraBodhiya/I_series/I_series.html">කළුතර බෝධි පරිශ්‍රයේදී පැවැත්වුන 9වෙනි දේශනා මාලාව (I Series)</a></h2>\n')
    fp.write('</div>\n')
    fp.close()

##### 7th
with open(html_file, 'a', encoding="utf-8") as fp:
    #fp.write('<br>\n')
    fp.write('<div class="normal-head">\n')
    fp.write('<h2>7. <a href="../VisheshaDesana/VisheshaDesana.html">විශේෂ දේශනා</a></h2>\n')
    fp.write('</div>\n')
    fp.close()

##### 8th
playlist_url_8 = 'https://www.youtube.com/playlist?list=PLqESXbJ82aIgmWdPzXFdJplUOPJgRXpZN'
playlist_8 = 'Suthamaya/suthamaya_mathugama.txt'
playlist_title_8 = "සුතමයඤාණං - Sri Sudharshanarama Maha Viharaya Mathugama"
series_title_8 = "සුතමයඤාණං දේශනා මාලාව - ශ්‍රී සුධර්ශනාරාම මහා විහාරය මතුගම"
HtmlDropdownBlockNoSections(8, playlist_8, playlist_title_8, html_file, '', '', series_title_8)

###### 9th
playlist_9 = 'KalutaraBodhiya/H_series.txt'
playlist_title_9 = "Kalutara Bodhiya H Series"
series_title_9 = "කළුතර බෝධි පරිශ්‍රයේදී පැවෙත්වුන අටවෙනි දේශනා මාලාව (H Series)"
HtmlDropdownBlockNoSections(9, playlist_9, playlist_title_9, html_file, '', '', series_title_9)

####### 10th
playlist_10 = 'KalutaraBodhiya/G_series.txt'
playlist_title_10 = "Kalutara Bodhiya G Series"
series_title_10 = "කළුතර බෝධි පරිශ්‍රයේදී පැවෙත්වුන හත්වෙනි දේශනා මාලාව (G Series)"
HtmlDropdownBlockNoSections(10, playlist_10, playlist_title_10, html_file, '', '', series_title_10)


##### 11th
playlist_11 = 'KalutaraBodhiya/F_series.txt'
playlist_title_11 = "Kalutara Bodhiya F Series"
series_title_11 = "කළුතර බෝධි පරිශ්‍රයේදී පැවෙත්වුන හයවෙනි දේශනා මාලාව (F Series)"
HtmlDropdownBlockNoSections(11, playlist_11, playlist_title_11, html_file, '', '',series_title_11)

##### 12th
playlist_12 = 'KalutaraBodhiya/E_series.txt'
playlist_title_12 = "Kalutara Bodhiya E Series"
series_title_12 = "කළුතර බෝධි පරිශ්‍රයේදී පැවෙත්වුන පස්වෙනි දේශනා මාලාව (E Series)"
HtmlDropdownBlockNoSections(12, playlist_12, playlist_title_12, html_file, '', '', series_title_12)

##### 13th
with open(html_file, 'a', encoding="utf-8") as fp:
    #fp.write('<br>\n')
    fp.write('<div class="normal-head">\n')
    fp.write('<h2>13. <a href="../KalutaraBodhiya/B_C_D_Batches.html">කළුතර බෝධි පරිශ්‍රයේදී පැවෙත්වුන දෙවන, තෙවන සහ සිව්වන අභිධම්ම දේශනා කාණ්ඩ (B, C, සහ D)</a>\n</h2>')
    fp.write('</div>\n')
    fp.close()

###### 14th
playlist_14 = 'KalutaraBodhiya/ParamarthaLokayaKalutharaBodhiya.txt'
playlist_title_14 = "Paramartha Lokaya Kalutara Bodhiya A"
series_title_14 = "කළුතර බෝධි පරිශ්‍රයේදී පැවෙත්වුන මුල්ම දේශනා මාලාව (A Series)"
HtmlDropdownBlockNoSections(14, playlist_14, playlist_title_14, html_file, '', '', series_title_14)


with open(html_file, 'a', encoding="utf-8") as fp:
    fp.write('<div class="normal-head">\n')
    fp.write('<h2>15. <a href="../Paramartha_Video/Paramartha_Video.html">පරමාර්ථ ලෝකය දේශනා</a>\n</h2>')
    fp.write('</div>\n')
    fp.close()

with open(html_file, 'a', encoding="utf-8") as fp:
    fp.write('<div class="normal-head">\n')
    fp.write('<h2>16. <a href="../Anichcha_Dukka_Anathma_Series/Anichcha_Dukka_Anathma.html">අනිච්ච, දුක්ඛ, අනත්ත දේශනා</a>\n</h2>')
    fp.write('</div>\n')
    fp.close()
    
######## tail #########
with open(html_file, 'a', encoding="utf-8") as fp:
#    fp.write('<h5>&emsp; F කාණ්ඩය අසම්පූර්ණයි</h5>\n')
    fp.write('<br>\n')
    fp.write('<li><a href="../documents/file_list.html">සියලු අභිධම්ම දේශනා සඳහා සටහන්</a></li>\n')
    fp.write('<br>\n')

    fp.write('<h3><a href="all_videos.html">සියලුම දේශනා - @WayToNibbana YouTube Channel</a></h3>\n')
    fp.close()

PrepareTail(html_file)