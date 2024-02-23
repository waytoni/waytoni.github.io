import io
import shutil
import sys
sys.path.append('scripts')
from dropdown_block_working import *

def prepare_html_block(block_id, in_file, playlist_title, outfile, playlist_url, idx_prefix):
    
    with open(in_file, 'r', encoding='utf-8') as fp:
        utubelink_lines = [line.strip().split() for line in fp.readlines()]

    idx = [row[0] for row in utubelink_lines]
    urls = [row[1] for row in utubelink_lines]
    dates = [row[2] for row in utubelink_lines]
    N = len(idx)

    # print(N)
    
    option_n = []
    p4 = []
    option_text = []


    with open(outfile, 'a', encoding="utf-8") as fp:
        fp.write('<h2>' + str(block_id) + '. ' + playlist_title + '</h2>\n')

        fp.write('<p></p>\n')

        if len(playlist_url) > 1:
            fp.write(f'<a href="{playlist_url}">Watch full playlist in YouTube</a>\n')
        
        fp.write('<p></p>\n<p>Select a video from the dropdown menu</p>    <p></p>\n')
        
        # fp.write('<p></p>\n<p>පතන මෙනුවෙන් වීඩියෝවක් තෝරන්න</p>    <p></p>\n')
        

        fp.write('<select id="video_list' + str(block_id) + '">\n')
    
        for n in range(1, N+1):
            # print(n)
            url_val = urls[n-1]
            date_val = dates[n-1]
            url_video_val = ''
            #idx_val = idx[n-1]
            noVideo = False
              
            idx_val = idx_prefix + str(idx[n-1]).zfill(3)

            if len(url_val) > 0:
                url_val_split = url_val.split('=')
                # print(len(url_val_split))
                
                if len(url_val_split) > 1:
                    url_video_val = url_val_split[1]
                else:
                    url_video_val = url_val
                    noVideo = True

            p0_short = f"{date_val} {playlist_title} {idx_val}"

            option_text.append(p0_short)
            # print(option_text[n-1])
            # print(' ' , idx[n-1] ,' ' , dates[n-1] ,' p0_short= ' , p0_short)
            
            if len(url_video_val) > 1 and noVideo == False:
                p1 = f'<iframe width="560" height="315" src="https://www.youtube.com/embed/{url_video_val}"'
                p2 = ' title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"'
                p3 = ' allowfullscreen></iframe>'
                p4_s = p1 + p2 + p3
            else:
                p4_s = url_video_val

            # print(p4_s)
            
            p4.append(p4_s)
            option_s = f'option{n}'
            option_n.append(option_s)

            if n == N:
                fp.write('\t<option value="' + option_n[n-1] +'" selected>' + option_text[n-1] +  '</option>\n')
            else:
                fp.write('\t<option value="' + option_n[n-1] +'">' + option_text[n-1] +  '</option>\n')

        fp.write('</select>\n')
        fp.write('<div id="content'+str(block_id)+'"></div>\n')
        fp.write('<script>\n')
        fp.write('\tconst select' + str(block_id) + ' = document.querySelector(\'#video_list' + str(block_id) + '\');\n')
        fp.write('\tconst content' + str(block_id) + ' = document.querySelector(\'#content' + str(block_id)+ '\');\n')
        fp.write('\t\t\tcontent' + str(block_id) + '.innerHTML = \'<p></p>' + p4[N-1] + '\';\n')
        
        fp.write('\tselect' + str(block_id) + '.addEventListener(\'change\', function() {\n')
        fp.write('\t\tif (this.value === \'option1\') {\n')
        fp.write('\t\t\tcontent' + str(block_id) +'.innerHTML = \'<p></p>' + p4[0] + '\';\n')
                
        #with open('utube_html_dropdown.txt', 'a', encoding="utf-8") as fp:
        for n in range(2, N+1):
            # print(n,' ',option_n[n-1])
            fp.write('\t\t} else if (this.value === \'' + option_n[n-1] + '\'){\n')
            fp.write('\t\t\tcontent' + str(block_id) + '.innerHTML = \'<p></p>' + p4[n-1] + '\';\n')

        fp.write('\t}\n')
        fp.write('});\n')
        fp.write('</script>\n')
        
        fp.write('<br>\n')
        fp.close()

    return None
##############################################################################


text_filename = 'All_Playlists/utube_html_dropdown_1.txt'

# Uncomment the following line only if everything is okay
html_filename = 'All_Playlists/සියුලු_දේශනා.html'

############ top #########

with open(text_filename, 'w', encoding="utf-8") as fp:
    fp.write('<html>\n<head>\n')
    
    with open('scripts/analytics_tag.txt', 'r', encoding="utf-8") as ftag:
        tag_info = ftag.read()
        fp.write(tag_info)
        ftag.close()
    
    fp.write('\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    fp.write('\t<link rel="stylesheet" type="text/css" href="../css/nav_menu.css">\n')
    fp.write('\t<link rel="stylesheet" type="text/css" href="../css/dp_block.css">\n')
    #fp.write('\t<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">\n')
    fp.write('\t<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css" integrity="sha512-+4zCK9k+qNFUR5X+cKL9EIR+ZOhtIloNl9GIKS57V1MyNsYpYcUrUeQc9vNfzsWfV28IaLL3i96P9sdNyeRssA==" crossorigin="anonymous" />\n')
    fp.write('\t<script src="../scripts/menu_function.js"></script>\n')
    fp.write('\t<script src="../scripts/jquery-3.7.1.min.js"></script>\n')
    fp.write('\t<script src="../scripts/dp_function.js"></script>\n')
    fp.write('\t<body style="font-family:calibri;"></body>\n')
    fp.write('\t<link rel="icon" type="image/png" href="../images/favicon-16x16.png" sizes="16x16" />\n')
    fp.write('\t<title>අභිධම්ම දේශනා  - සියල්ල</title>\n')
    
    fp.write('</head>\n<body>\n')
    
    fp.write('<div class="topnav" id="Topnavbar">\n')
    fp.write('<a href="https://waytoni.github.io/" class="active">Home </a>\n') 
    fp.write('<a href="../All_Playlists/සියුලු_දේශනා.html">සියලුම දේශනා </a>\n')
    fp.write('<a href="../Paramartha_Video/Paramartha_Video.html">පරමාර්ථ ලෝකය දේශනා </a>\n \
        <a href="../Anichcha_Dukka_Anathma_Series/Anichcha_Dukka_Anathma.html">අනිච්ච, දුක්ඛ, අනත්ත දේශනා </a>\n')
    fp.write('<a href="../Saturday_Abhidhamma_Lesson/index.html">තුන්කල්හි වෙනස් නොවන ලොව එකම විශ්ව දර්ශනය දේශනා</a>\n \
        <a href="../Abhidharma_Aruth/index.html">අභිධර්ම අරුත් දේශනා</a>\n')
    fp.write('<a href="../Nivan_Maga_Udesa/index.html">නිවන් මග උදෙසා දේශනා</a>\n')
    fp.write('<a href="../Chithatha_Chithasika/Chiththa_Chithasika.html">චිත්ත සහ චෛතසික</a>\n')
    fp.write('<a href="javascript:void(0);" class="icon" onclick="navFunction()"> <i class="fa fa-bars"></i></a>\n')
    fp.write('</div>\n')
    
    fp.write('<h1>අභිධම්ම දේශනා  - සියල්ල</h1>\n')
    
    # fp.write('<br>\n')
    fp.write('<h2><li><a href="../documents/file_list.html">සියලු අභිධම්ම දේශනා සඳහා සටහන්</a></li></h2>\n')
    # fp.write('<br>\n')
    
    fp.close()


#### set up playlist selection ######### 
    
playlist_url_0 = "https://www.youtube.com/playlist?list=PLqESXbJ82aIip-TA7Efg5JjwmEDJ95kAx"
playlist_0 = 'Saturday_Abhidhamma_Lesson/saturday_abhidhamma_lesson_youtube_links.txt'
playlist_title_0 = "තුන්කල්හි වෙනස් නොවන ලොව එකම විශ්ව දර්ශනය"
idx_prefix_0 = 'A'

#prepare_html_block(1, playlist_0, playlist_title_0, text_filename, playlist_url_0, idx_prefix_0)
DropdownBlockWorking(1, playlist_0, playlist_title_0, text_filename, '', idx_prefix_0)

playlist_url_2 = 'https://www.youtube.com/playlist?list=PLqESXbJ82aIgflkHivXH-cYXlz1onvNCi'
playlist_2 = 'Nivan_Maga_Udesa/nivan_maga_udesa_youtube_links.txt'
playlist_title_2 = "නිවන් මග උදෙසා දර්ශන ඥාණය (A කණ්ඩායම)"
#prepare_html_block(2, playlist_2, playlist_title_2, text_filename, playlist_url_2, '')
DropdownBlockWorking(2, playlist_2, playlist_title_2, text_filename, '', '')

with open(text_filename, 'a', encoding="utf-8") as fp:
    fp.write('<a id="I_series">\n')
    fp.write('<div class="normal-head">\n')
    fp.write('<h2>කළුතර බෝධි පරිශ්‍රයේදී පැවෙත්වෙන 9වෙනි දේශනා මාලාව (I Series)</h2>\n')
    fp.write('</div>\n')
#    fp.write('<h2>සෑම ඉරිදාවකම ප.ව. 2:00 සිට ප.ව. 4:00 දක්වා</h2>\n')
#    fp.write('<h2>WhatsApp සම්බන්ධ වීමට සහ විමසීම්: 071 - 8896727</h3>\n')
    fp.close()
    
playlist_url_3 = 'https://www.youtube.com/playlist?list=PLqESXbJ82aIjuYvXqOWBWMs-moFFukBbN'
playlist_3 = 'All_Playlists/I_Series.txt'
playlist_title_3 = "Abhidhamma lesson Kalutara Bodhiya I"
#prepare_html_block(3, playlist_3, playlist_title_3, text_filename, playlist_url_3, '')
DropdownBlockWorking(3, playlist_3, playlist_title_3, text_filename, '', '')

playlist_4 = 'Abhidharma_Aruth/Abhidharma_Aruth_youtube_links.txt'
playlist_title_4 = "Abhidharma Aruth"
#prepare_html_block(4, playlist_4, playlist_title_4, text_filename, '', 'EP')
DropdownBlockWorking(4, playlist_4, playlist_title_4, text_filename, '', 'EP')

playlist_5 = 'Abhidharma_Aruth/Abhidharma_Aruth_B_youtube_links.txt'
playlist_title_5 = "Abhidharma Aruth - B"
#prepare_html_block(5, playlist_5, playlist_title_5, text_filename, '', '')
DropdownBlockWorking(5, playlist_5, playlist_title_5, text_filename, '', '')

playlist_url_6 = ''
playlist_6 = 'Suthamaya/suthamaya_eththapana.txt'
playlist_title_6 = "සුතමයඤාණං - ඉත්තෑපාන අක්කර"
#prepare_html_block(6, playlist_6, playlist_title_6, text_filename, playlist_url_6, '')
DropdownBlockWorking(6, playlist_6, playlist_title_6, text_filename, '', '')

#playlist_url_7 = ''
#playlist_7 = 'විශේෂ දේශනා/special_desana_links.txt'
#playlist_title_7 = "විශේෂ දේශනා"
#prepare_html_block(7, playlist_7, playlist_title_7, text_filename, playlist_url_7, '')

with open(text_filename, 'a', encoding="utf-8") as fp:
        #fp.write('<br>\n')
        fp.write('<div class="normal-head">\n')
        fp.write('<h2>7. විශේෂ දේශනා</h2>\n')
        fp.write('</div>\n')
        fp.write('<div class="dp-head">\n')
        fp.write('<h3>2024-02-17 සෙනසුරාදා වීදියගොඩ රාජ මහ විහාරස්ථානයේ දී පැවැත්වූ දේශනාව</h3>\n')
        fp.write('<span><i class = "fas fa-plus"></i></span>\n')
        fp.write('</div>\n')
        fp.write('<div class = "dp-content">\n')
        fp.write('<iframe width="560" height="315" src="https://www.youtube.com/embed/_gIfkc0Hifw?si=ruS-MUtqrzHHwAQe" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>\n')
        fp.write('</div>\n')
        fp.close()
        

playlist_url_8 = 'https://www.youtube.com/playlist?list=PLqESXbJ82aIgmWdPzXFdJplUOPJgRXpZN'
playlist_8 = 'Suthamaya/suthamaya_mathugama.txt'
playlist_title_8 = "සුතමයඤාණං - Sri Sudharshanarama Maha Viharaya Mathugama"
#prepare_html_block(8, playlist_8, playlist_title_8, text_filename, playlist_url_8, '')

DropdownBlockWorking(8, playlist_8, playlist_title_8, text_filename, '', '')

playlist_9 = 'All_Playlists/H_Series.txt'
playlist_title_9 = "Kalutara Bodhiya H Series"
# prepare_html_block(9, playlist_9, playlist_title_9, text_filename, '', '')
DropdownBlockWorking(9, playlist_9, playlist_title_9, text_filename, '', '')

playlist_10 = 'All_Playlists/G_Series.txt'
playlist_title_10 = "Kalutara Bodhiya G Series"
#prepare_html_block(10, playlist_10, playlist_title_10, text_filename, '', '')
DropdownBlockWorking(10, playlist_10, playlist_title_10, text_filename, '', '')

playlist_11 = 'All_Playlists/F_Series.txt'
playlist_title_11 = "Kalutara Bodhiya F Series"
#prepare_html_block(11, playlist_11, playlist_title_11, text_filename, '', '')
DropdownBlockWorking(11, playlist_11, playlist_title_11, text_filename, '', '')

playlist_12 = 'All_Playlists/E_Series.txt'
playlist_title_12 = "Kalutara Bodhiya E Series"
#prepare_html_block(12, playlist_12, playlist_title_12, text_filename, '', '')
DropdownBlockWorking(12, playlist_12, playlist_title_12, text_filename, '', '')

with open(text_filename, 'a', encoding="utf-8") as fp:
    #fp.write('<br>\n')
    fp.write('<div class="normal-head">\n')
    fp.write('<h2>13. <a href="B_C_D_Batches.html">මුල් අභිධම්ම දේශනා කාණ්ඩ  B, C, සහ D</a>\n</h2>')
    fp.write('</div>\n')
    fp.write('<a id="A_series">\n')
    fp.write('<div class="normal-head">\n')
    fp.write('<h2>කළුතර බෝධි පරිශ්‍රයේදී පැවෙත්වුන මුල්ම දේශනා මාලාව (A Series)</h2>\n')
    fp.write('</div>\n')
    fp.close()
    
playlist_14 = 'All_Playlists/ParamarthaLokayaKalutharaBodhiya.txt'
playlist_title_14 = "Paramartha Lokaya Kalutara Bodhiya A"
#prepare_html_block(14, playlist_14, playlist_title_14, text_filename, '', '')
DropdownBlockWorking(14, playlist_14, playlist_title_14, text_filename, '', '')

######## tail #########
with open(text_filename, 'a', encoding="utf-8") as fp:
#    fp.write('<h5>&emsp; F කාණ්ඩය අසම්පූර්ණයි</h5>\n')
    fp.write('<br>\n')
    fp.write('<li><a href="../documents/file_list.html">සියලු අභිධම්ම දේශනා සඳහා සටහන්</a></li>\n')
    fp.write('<br>\n')

    fp.write('<h3><a href="all_videos.html">සියලුම දේශනා - @WayToNibbana YouTube Channel</a></h3>\n')
    
    fp.write('</body>\n')
    fp.write('</html>\n')
    fp.close()


shutil.copy2(text_filename, html_filename, follow_symlinks=False)
