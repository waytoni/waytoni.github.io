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

html_file = os.path.join(basepath,'SiyaluDesana.html')

series_title = 'ගරු අජන්ත සම්පත් ගුරුතුමා මෙහෙයවන සහ මෙහෙයවූ දේශනා සියල්ල'

print(intro_file)
print(html_file)


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
    fp.write('\t<link rel="stylesheet" type="text/css" href="/css/nav_menu.css">\n')
    fp.write('\t<link rel="stylesheet" type="text/css" href="/css/dp_block.css">\n')
    fp.write('\t<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css" integrity="sha512-+4zCK9k+qNFUR5X+cKL9EIR+ZOhtIloNl9GIKS57V1MyNsYpYcUrUeQc9vNfzsWfV28IaLL3i96P9sdNyeRssA==" crossorigin="anonymous" />\n')
    fp.write('\t<script src="/scripts/nav_function.js"></script>\n')
    fp.write('\t<script src="/scripts/jquery-3.7.1.min.js"></script>\n')
    fp.write('\t<script src="/scripts/dp_function.js"></script>\n')
    fp.write('\t<body style="font-family:calibri;"></body>\n')
    fp.write('\t<link rel="icon" type="image/png" href="../images/favicon-16x16.png" sizes="16x16" />\n')
    fp.write('\t<title>ගරු අජන්ත සම්පත් ගුරුතුමා මෙහෙයවන සහ මෙහෙයවූ දේශනා සියල්ල</title>\n')
    
    fp.write('</head>\n<body>\n')

    with open('scripts/py/navigation_header.html', 'r', encoding="utf-8") as fnavbar:
        navbar_info = fnavbar.read()
        fp.write(navbar_info)
        fnavbar.close()

    fp.write('<h1>ගරු අජන්ත සම්පත් ගුරුතුමා මෙහෙයවන සහ මෙහෙයවූ දේශනා සියල්ල</h1>\n')
    
    #fp.write('<h2><li><a href="/documents/file_list.html">සියලු අභිධම්ම දේශනා සඳහා සටහන්</a></li></h2>\n')
    
    # fp.write('<h2><li><a href="/documents/NotesForDesana/NotesForDesana.html">සියුලු දේශනා සඳහා සටහන්</a></li></h2>\n')
    # fp.write('<br>\n')
    
    fp.close()

#### 1st
id = 1
with open(html_file, 'a', encoding="utf-8") as fp:
    #fp.write('<br>\n')
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>29. <a href="/NivanMagaUdesaDesana/ThalawathugodaB/ThalawathugodaB.html">තලවතුගොඩ ගනේලන්ද පන්සලේ පැවෙත්වෙන නිවන් මග උදෙසා දර්ශන ඥානය දේශනා මාලාව (B කන්ඩායම)</a></h2>\n')
    fp.write('</div>\n')
    fp.close()
    
### 2nd
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>28. <a href="/AbhidharmaAruth/D_series/AbhidharmaAruthD.html">පොල්ගස්ඕවිට පැවෙත්වෙන නිවන් මග උදෙසා දර්ශන ඥානය දේශනා මාලාව (D කන්ඩායම)</a></h2>\n')
    fp.write('</div>\n')
    fp.close() 

### 3rd
id = id + 1   
with open(html_file, 'a', encoding="utf-8") as fp:
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>27. <a href="/NivanMagaUdesaDesana/MaharagamaA/MaharagamaA.html">මහරගම තරුණ බෞද්ධ මන්දිරයේ පැවෙත්වෙන නිවන් මග උදෙසා දර්ශන ඥානය දේශනා මාලාව</a></h2>\n')
    fp.write('</div>\n')
    fp.close()

### 4th
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>26. <a href="/KalutaraBodhiya/L_series/L_series.html">2025 කළුතර බෝධි පරිශ්‍රයේදී පැවෙත්වෙන නිවන් මග උදෙසා දර්ශන ඥානය දේශනා මාලාව (L Series)</a></h2>\n')
    fp.write('</div>\n')
    fp.close()

#### 5th
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    #fp.write('<br>\n')
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>25. <a href="/VisheshaDesana/RuwanweliMahaSeya/RuwanweliMahaSeya.html">පොහොය දිනවල රුවන්වැලි මහාසෑය අභියස පැවෙත්වෙන දේශනා</a></h2>\n')
    fp.write('</div>\n')
    fp.close()
    
#### 6th
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    #fp.write('<br>\n')
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>24. <a href="../VisheshaDesana/index.html">විශේෂ දේශනා</a></h2>\n')
    fp.write('</div>\n')
    fp.close()
    

#### 7th
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    #fp.write('<br>\n')
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>23. <a href="/NivanMagaUdesaDesana/Thalawathugoda/Thalawathugoda.html">තලවතුගොඩ ගනේලන්ද පන්සලේ පැවැත්වුන නිවන් මග උදෙසා දර්ශන ඥානය දේශනා මාලාව</a></h2>\n')
    fp.write('</div>\n')
    fp.close()

#### 8th
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>22. <a href="/AbhidharmaAruth/C_series/AbhidharmaAruthC.html">පොල්ගස්ඕවිට පැවැත්වුන නිවන් මග උදෙසා දර්ශන ඥානය දේශනා මාලාව (C කන්ඩායම)</a></h2>\n')
    fp.write('</div>\n')
    fp.close() 

#### 9th
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>21. <a href="/KalutaraBodhiya/K_series/K_series.html">2025 කළුතර බෝධි පරිශ්‍රයේදී පැවැත්වුන නිවන් මග උදෙසා දර්ශන ඥානය දේශනා මාලාව (K Series)</a></h2>\n')
    fp.write('</div>\n')
    fp.close()
        
#### 10th
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    #fp.write('<br>\n')
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>20. <a href="/NivanMagaUdesaDesana/A_series/index.html">නිවන් මග උදෙසා දර්ශන ඥානය දේශනා මාලාව (A කණ්ඩායම)</a></h2>\n')
    fp.write('</div>\n')
    fp.close()
        
#### 11th
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>19. <a href="/AbhidharmaAruth/B2_series/AbhidharmaAruthB2.html">පොල්ගස්ඕවිට පැවැත්වුන නිවන් මග උදෙසා දර්ශන ඥානය දේශනා මාලාව (B කන්ඩායම - දෙවන කොටස)</a></h2>\n')
    fp.write('</div>\n')
    fp.close()  
    
#### 12th
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    #fp.write('<br>\n')
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>18. <a href="/KalutaraBodhiya/J_series/J_series.html">2024 කළුතර බෝධි පරිශ්‍රයේදී පැවැත්වුන නිවන් මග උදෙසා දර්ශන ඥානය දේශනා මාලාව (J Series)</a></h2>\n')
    fp.write('</div>\n')
    fp.close()


#### 13th
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    #fp.write('<br>\n')
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>17. <a href="/AbhidharmaSeries/A_series/index.html">තුන්කල්හි වෙනස් නොවන ලොව එකම විශ්ව දර්ශනය දේශනා මාලාව</a></h2>\n')
    fp.write('</div>\n')
    fp.close()

####  14th
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>16. <a href="/AbhidharmaAruth/B1_series/AbhidharmaAruthB1.html">පොල්ගස්ඕවිට පැවැත්වුන නිවන් මග උදෙසා දර්ශන ඥානය දේශනා මාලාව (B කන්ඩායම - පළමු කොටස)</a></h2>\n')
    fp.write('</div>\n')
    fp.close()  
    
#### 15th
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>15. <a href="/AbhidharmaAruth/EP_series/AbhidharmaAruthEP.html">පොල්ගස්ඕවිට පැවැත්වුන අභිධර්ම අරුත් දේශනා මාලාව (EP)</a></h2>\n')
    fp.write('</div>\n')
    fp.close()  

#### 16th
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    #fp.write('<br>\n')
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>14. <a href="/Suthamaya/Hirigal/SuthamayaHirigal.html">සුතමයඤාණං දේශනා මාලාව - හිරිගල් ගොඩැල්ල ශ්‍රී පුෂ්පාරාමය</a></h2>\n')
    fp.write('</div>\n')
    fp.close()

#### 17th
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    #fp.write('<br>\n')
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>13. <a href="/Suthamaya/Ittapane/SuthamayaIttapane.html">සුතමයඤාණං දේශනා මාලාව - ඉත්තෑපාන අක්කර</a></h2>\n')
    fp.write('</div>\n')
    fp.close()

    
##### 18th
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    #fp.write('<br>\n')
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>12. <a href="/KalutaraBodhiya/I_series/I_series.html">කළුතර බෝධි පරිශ්‍රයේදී පැවැත්වුන 9වෙනි දේශනා මාලාව (I Series)</a></h2>\n')
    fp.write('</div>\n')
    fp.close()

##### 19th
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    #fp.write('<br>\n')
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>11. <a href="/Suthamaya/Mathugama/SuthamayaMathugama.html">සුතමයඤාණං දේශනා මාලාව - ශ්‍රී සුධර්ශනාරාම මහා විහාරය මතුගම</a></h2>\n')
    fp.write('</div>\n')
    fp.close()
    
###### 20th
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    #fp.write('<br>\n')
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>10. <a href="/KalutaraBodhiya/H_series/H_series.html">2022-2023 කළුතර බෝධි පරිශ්‍රයේදී පැවැත්වුන අටවෙනි දේශනා මාලාව (H Series)</a></h2>\n')
    fp.write('</div>\n')
    fp.close()


###### 21st
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>9. <a href="/Anichcha_Dukka_Anathma_Series/Anichcha_Dukka_Anathma.html">අනිච්ච, දුක්ඛ, අනත්ත දේශනා</a>\n</h2>')
    fp.write('</div>\n')
    fp.close()
    
##### 22nd
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    #fp.write('<br>\n')
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>8. <a href="/KalutaraBodhiya/G_series/G_series.html">2020 කළුතර බෝධි පරිශ්‍රයේදී පැවැත්වුන හත්වෙනි දේශනා මාලාව (G Series)</a></h2>\n')
    fp.write('</div>\n')
    fp.close()



##### 20th
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    #fp.write('<br>\n')
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>7. <a href="/KalutaraBodhiya/F_series/F_series.html">2019 කළුතර බෝධි පරිශ්‍රයේදී පැවැත්වුන හයවෙනි දේශනා මාලාව (F Series)</a></h2>\n')
    fp.write('</div>\n')
    fp.close()

##### 21st
id = id + 1
playlist_KB_E = 'KalutaraBodhiya/E_series.txt'
playlist_title_KB_E = "Kalutara Bodhiya E Series"
series_title_KB_E = "කළුතර බෝධි පරිශ්‍රයේදී පැවෙත්වුන පස්වෙනි දේශනා මාලාව (E Series)"
HtmlDropdownBlockNoSections(6, playlist_KB_E, playlist_title_KB_E, html_file, '', '', series_title_KB_E)

##### 25th
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    #fp.write('<br>\n')
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>3, 4 සහ 5. <a href="/KalutaraBodhiya/B_C_D_Batches.html">කළුතර බෝධි පරිශ්‍රයේදී පැවෙත්වුන දෙවන, තෙවන සහ සිව්වන අභිධම්ම දේශනා කාණ්ඩ (B, C, සහ D)</a>\n</h2>')
    fp.write('</div>\n')
    fp.close()


##### 26th
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    #fp.write('<br>\n')
    fp.write('<div class="normal-head">\n')
    fp.write(f'<h2>2. <a href="/KalutaraBodhiya/A_series/A_series.html">2013-2015 කළුතර බෝධි පරිශ්‍රයේදී පැවැත්වුන ප්‍රථම දේශනා මාලාව (A Series)</a></h2>\n')
    fp.write('</div>\n')
    fp.close()
    
###### 27th
id = id + 1
with open(html_file, 'a', encoding="utf-8") as fp:
    fp.write('<div class="normal-head">\n')
    #fp.write(f'<h2>{id}. <a href="/Paramartha_Video/Paramartha_Video.html">පරමාර්ථ ලෝකය දේශනා</a>\n</h2>')
    fp.write(f'<h2>1. <a href="/Paramartha_Video/Paramartha_Video.html">පරමාර්ථ ලෝකය දේශනා</a>\n</h2>')
    fp.write('</div>\n')
    fp.close()

    
######## tail #########
with open(html_file, 'a', encoding="utf-8") as fp:
#    fp.write('<h5>&emsp; F කාණ්ඩය අසම්පූර්ණයි</h5>\n')
    fp.write('<br>\n')
    # fp.write('<li><a href="/documents/NotesForDesana/NotesForDesana.html">සියලු අභිධම්ම දේශනා සඳහා සටහන්</a></li>\n')
    # fp.write('<br>\n')

    fp.write('<h3><a href="AllVideos_V2.html">සියලුම දේශනා - @WayToNibbana YouTube Channel</a></h3>\n')
    fp.write('<h3><a href="AllVideos_AA.html">සියලුම දේශනා - Abhidharma Aruth - අභිධර්ම අරුත් YouTube Channel</a></h3>\n')
    fp.close()

PrepareTail(html_file)

old_html_file = 'All_Playlists/සියුලු_දේශනා.html'
shutil.copy2(html_file, old_html_file, follow_symlinks=False)