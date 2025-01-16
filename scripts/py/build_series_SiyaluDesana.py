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
    fp.write('\t<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css" integrity="sha512-+4zCK9k+qNFUR5X+cKL9EIR+ZOhtIloNl9GIKS57V1MyNsYpYcUrUeQc9vNfzsWfV28IaLL3i96P9sdNyeRssA==" crossorigin="anonymous" />\n')
    fp.write('\t<script src="/scripts/nav_function.js"></script>\n')
    fp.write('\t<script src="/scripts/jquery-3.7.1.min.js"></script>\n')
    fp.write('\t<script src="/scripts/dp_function.js"></script>\n')
    fp.write('\t<body style="font-family:calibri;"></body>\n')
    fp.write('\t<link rel="icon" type="image/png" href="../images/favicon-16x16.png" sizes="16x16" />\n')
    fp.write('\t<title>අභිධම්ම දේශනා  - සියල්ල</title>\n')
    
    fp.write('</head>\n<body>\n')

    with open('scripts/py/navigation_header.html', 'r', encoding="utf-8") as fnavbar:
        navbar_info = fnavbar.read()
        fp.write(navbar_info)
        fnavbar.close()

    fp.write('<h1>අභිධම්ම දේශනා  - සියල්ල</h1>\n')
    
    fp.write('<h2><li><a href="/documents/file_list.html">සියලු අභිධම්ම දේශනා සඳහා සටහන්</a></li></h2>\n')
    # fp.write('<br>\n')
    
    fp.close()

### 1st
id = 1
with open(html_file, 'a', encoding="utf-8") as fp:
    #fp.write('<br>\n')
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>{id}. <a href="/Nivan_Maga_Udesa/index.html">නිවන් මග උදෙසා දර්ශන ඥාණය දේශනා මාලාව (A කණ්ඩායම)</a></h2>\n')
    fp.write('</div>\n')
    fp.close()

#### 2nd
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>{id}. <a href="/KalutaraBodhiya/K_series/K_series.html">2025 කළුතර බෝධි පරිශ්‍රයේදී පැවෙත්වෙන නිවන් මග උදෙසා දර්ශන ඥාණය දේශනා මාලාව (K Series)</a></h2>\n')
    fp.write('</div>\n')
    fp.close()
    
#### 3rd
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>{id}. <a href="/AbhidharmaAruth/AbhidharmaAruthC.html">පොල්ගස්ඕවිට පැවෙත්වෙන නිවන් මග උදෙසා දර්ශන ඥාණය දේශනා මාලාව (C කන්ඩායම)</a></h2>\n')
    fp.write('</div>\n')
    fp.close() 

    
####  4th
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>{id}. <a href="/AbhidharmaAruth/AbhidharmaAruthB2.html">පොල්ගස්ඕවිට පැවෙත්වෙන නිවන් මග උදෙසා දර්ශන ඥාණය දේශනා මාලාව (B කන්ඩායම)</a></h2>\n')
    fp.write('</div>\n')
    fp.close()  
    
#### 5th
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    #fp.write('<br>\n')
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>{id}. <a href="/KalutaraBodhiya/J_series/J_series.html">2024 කළුතර බෝධි පරිශ්‍රයේදී පැවැත්වුන නිවන් මග උදෙසා දර්ශන ඥාණය දේශනා මාලාව (J Series)</a></h2>\n')
    fp.write('</div>\n')
    fp.close()


#### 6th
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    #fp.write('<br>\n')
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>{id}. <a href="/AbhidharmaSeries/index.html">තුන්කල්හි වෙනස් නොවන ලොව එකම විශ්ව දර්ශනය දේශනා මාලාව</a></h2>\n')
    fp.write('</div>\n')
    fp.close()


#### 7th
id = id + 1
playlist_AA_EP = 'Abhidharma_Aruth/Abhidharma_Aruth_youtube_links.txt'
playlist_title_AA_EP = "Abhidharma Aruth"
series_title_AA_EP = "අභිධර්ම අරුත් දේශනා මාලාව (EP)"
HtmlDropdownBlockNoSections(id, playlist_AA_EP, playlist_title_AA_EP, html_file, '', 'EP', series_title_AA_EP)

#### 8th
# id = id + 1
# playlist_AA_B = 'Abhidharma_Aruth/Abhidharma_Aruth_B_youtube_links.txt'
# playlist_title_AA_B = "Abhidharma Aruth - B"
# series_title_AA_B = "අභිධර්ම අරුත් - B දේශනා මාලාව"
# HtmlDropdownBlockNoSections(id, playlist_AA_B, playlist_title_AA_B, html_file, '', '', series_title_AA_B)

####  4th
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>{id}. <a href="/AbhidharmaAruth/AbhidharmaAruthB1.html">පොල්ගස්ඕවිට පැවෙත්වෙන නිවන් මග උදෙසා දර්ශන ඥාණය දේශනා මාලාව (B කන්ඩායම - පළමු කොටස)</a></h2>\n')
    fp.write('</div>\n')
    fp.close()  



#### 9th
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    #fp.write('<br>\n')
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>{id}. <a href="/Suthamaya/SuthamayaHirigal.html">සුතමයඤාණං දේශනා මාලාව - හිරිගල් ගොඩැල්ල ශ්‍රී පුෂ්පාරාමය</a></h2>\n')
    fp.write('</div>\n')
    fp.close()

##### 10th
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    #fp.write('<br>\n')
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>{id}. <a href="../VisheshaDesana/VisheshaDesana.html">විශේෂ දේශනා</a></h2>\n')
    fp.write('</div>\n')
    fp.close()

#### 11th
id = id + 1
playlist_url_suthamaya_eththapana = ''
playlist_suthamaya_eththapana = 'Suthamaya/suthamaya_eththapana.txt'
playlist_title_suthamaya_eththapana = "සුතමයඤාණං - ඉත්තෑපාන අක්කර"
series_title_suthamaya_eththapana = "සුතමයඤාණං දේශනා මාලාව - ඉත්තෑපාන අක්කර"
HtmlDropdownBlockNoSections(id, playlist_suthamaya_eththapana, playlist_title_suthamaya_eththapana, html_file, '', '', series_title_suthamaya_eththapana)

    
##### 12th
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    #fp.write('<br>\n')
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>{id}. <a href="../KalutaraBodhiya/I_series/I_series.html">කළුතර බෝධි පරිශ්‍රයේදී පැවැත්වුන 9වෙනි දේශනා මාලාව (I Series)</a></h2>\n')
    fp.write('</div>\n')
    fp.close()

##### 13th
id = id + 1
playlist_url_SU_M = 'https://www.youtube.com/playlist?list=PLqESXbJ82aIgmWdPzXFdJplUOPJgRXpZN'
playlist_SU_M = 'Suthamaya/suthamaya_mathugama.txt'
playlist_title_SU_M = "සුතමයඤාණං - Sri Sudharshanarama Maha Viharaya Mathugama"
series_title_SU_M = "සුතමයඤාණං දේශනා මාලාව - ශ්‍රී සුධර්ශනාරාම මහා විහාරය මතුගම"
HtmlDropdownBlockNoSections(id, playlist_SU_M, playlist_title_SU_M, html_file, '', '', series_title_SU_M)

###### 14th
id = id + 1
playlist_KB_H = 'KalutaraBodhiya/H_series.txt'
playlist_title_KB_H = "Kalutara Bodhiya H Series"
series_title_KB_H = "කළුතර බෝධි පරිශ්‍රයේදී පැවෙත්වුන අටවෙනි දේශනා මාලාව (H Series)"
HtmlDropdownBlockNoSections(id, playlist_KB_H, playlist_title_KB_H, html_file, '', '', series_title_KB_H)

####### 15th
id = id + 1
playlist_KB_G = 'KalutaraBodhiya/G_series.txt'
playlist_title_KB_G = "Kalutara Bodhiya G Series"
series_title_KB_G = "කළුතර බෝධි පරිශ්‍රයේදී පැවෙත්වුන හත්වෙනි දේශනා මාලාව (G Series)"
HtmlDropdownBlockNoSections(id, playlist_KB_G, playlist_title_KB_G, html_file, '', '', series_title_KB_G)


##### 16th
id = id + 1
playlist_KB_F = 'KalutaraBodhiya/F_series.txt'
playlist_title_KB_F = "Kalutara Bodhiya F Series"
series_title_KB_F = "කළුතර බෝධි පරිශ්‍රයේදී පැවෙත්වුන හයවෙනි දේශනා මාලාව (F Series)"
HtmlDropdownBlockNoSections(id, playlist_KB_F, playlist_title_KB_F, html_file, '', '',series_title_KB_F)

##### 17th
id = id + 1
playlist_KB_E = 'KalutaraBodhiya/E_series.txt'
playlist_title_KB_E = "Kalutara Bodhiya E Series"
series_title_KB_E = "කළුතර බෝධි පරිශ්‍රයේදී පැවෙත්වුන පස්වෙනි දේශනා මාලාව (E Series)"
HtmlDropdownBlockNoSections(id, playlist_KB_E, playlist_title_KB_E, html_file, '', '', series_title_KB_E)

##### 18th
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    #fp.write('<br>\n')
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>{id}. <a href="../KalutaraBodhiya/B_C_D_Batches.html">කළුතර බෝධි පරිශ්‍රයේදී පැවෙත්වුන දෙවන, තෙවන සහ සිව්වන අභිධම්ම දේශනා කාණ්ඩ (B, C, සහ D)</a>\n</h2>')
    fp.write('</div>\n')
    fp.close()

###### 19th
id = id + 1
playlist_KB_A = 'KalutaraBodhiya/ParamarthaLokayaKalutharaBodhiya.txt'
playlist_title_KB_A = "Paramartha Lokaya Kalutara Bodhiya A"
series_title_KB_A = "කළුතර බෝධි පරිශ්‍රයේදී පැවෙත්වුන මුල්ම දේශනා මාලාව (A Series)"
HtmlDropdownBlockNoSections(id, playlist_KB_A, playlist_title_KB_A, html_file, '', '', series_title_KB_A)


id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>{id}. <a href="../Paramartha_Video/Paramartha_Video.html">පරමාර්ථ ලෝකය දේශනා</a>\n</h2>')
    fp.write('</div>\n')
    fp.close()

id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>{id}. <a href="../Anichcha_Dukka_Anathma_Series/Anichcha_Dukka_Anathma.html">අනිච්ච, දුක්ඛ, අනත්ත දේශනා</a>\n</h2>')
    fp.write('</div>\n')
    fp.close()
    
######## tail #########
with open(html_file, 'a', encoding="utf-8") as fp:
#    fp.write('<h5>&emsp; F කාණ්ඩය අසම්පූර්ණයි</h5>\n')
    fp.write('<br>\n')
    fp.write('<li><a href="/documents/file_list.html">සියලු අභිධම්ම දේශනා සඳහා සටහන්</a></li>\n')
    fp.write('<br>\n')

    fp.write('<h3><a href="AllVideos_V2.html">සියලුම දේශනා - @WayToNibbana YouTube Channel</a></h3>\n')
    fp.close()

PrepareTail(html_file)

old_html_file = 'All_Playlists/සියුලු_දේශනා.html'
shutil.copy2(html_file, old_html_file, follow_symlinks=False)