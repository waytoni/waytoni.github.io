# import io
# import shutil
# import os
# import sys

# sys.path.append('scripts')
# sys.path.append(os.path.dirname('scripts'))

# from scripts.helpers import ReadSections
# from scripts.helpers import *


notes_file_EP = 'Abhidharma_Aruth/AA_EP_notes.txt'  
notes_file_B = 'Abhidharma_Aruth/AA_B_notes.txt'  
utube_links_EP = 'Abhidharma_Aruth/Abhidharma_Aruth_youtube_links.txt'
utube_links_B = 'Abhidharma_Aruth/Abhidharma_Aruth_B_youtube_links.txt'
html_file = 'Abhidharma_Aruth/index.html'
playlist_url_EP = ""
playlist_url_B = ""

series_title = 'අභිධර්ම අරුත් - දේශනා'

# sections_EP = ReadSections(notes_file_EP)
# sections_B = ReadSections(notes_file_B)

def PrepareHead_AA(text_filename, series_title): 
    
    with open(text_filename, 'w', encoding="utf-8") as fp:
        fp.write('<html>\n<head>\n')
    
        with open('scripts/analytics_tag.txt', 'r', encoding="utf-8") as ftag:
            tag_info = ftag.read()
            fp.write(tag_info)
            ftag.close()
            
        fp.write('<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">\n')
        fp.write('<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">\n')
        fp.write('<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">\n')
        fp.write('<link rel="manifest" href="/site.webmanifest">\n')    
        
        fp.write('\n')    
        fp.write('\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        fp.write('\t<link rel="stylesheet" type="text/css" href="../css/nav_menu.css">\n')
        fp.write('\t<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">\n')
        fp.write('\t<script src="../scripts/menu_function.js"></script>\n')
        fp.write('\t<link rel="icon" type="image/png" href="../images/favicon-16x16.png" sizes="16x16" />\n')
        title_line = '\t<title>'+ series_title + '</title>\n'
        fp.write(title_line)
        
        fp.write('</head>\n<body>\n')
    
        fp.write('<div class="topnav" id="Topnavbar">\n')
        fp.write('<a href="https://waytoni.github.io/" class="active">Home </a>\n') 
        fp.write('<a href="../All_Playlists/සියුලු_දේශනා.html">සියලුම දේශනා </a>\n')
        fp.write('<a href="../Paramartha_Video/Paramartha_Video.html">පරමාර්ථ ලෝකය දේශනා </a>\n')
        fp.write('<a href="../Anichcha_Dukka_Anathma_Series/Anichcha_Dukka_Anathma.html">අනිච්ච, දුක්ඛ, අනත්ත දේශනා </a>\n')
        fp.write('<a href="../Saturday_Abhidhamma_Lesson">තුන්කල්හි වෙනස් නොවන ලොව එකම විශ්ව දර්ශනය දේශනා</a>\n')
        fp.write('<a href="../Abhidharma_Aruth">අභිධර්ම අරුත් දේශනා</a>\n')
        fp.write('<a href="../Nivan_Maga_Udesa">නිවන් මග උදෙසා දේශනා</a>\n')
        fp.write('<a href="../Chithatha_Chithasika/Chiththa_Chithasika.html">චිත්ත සහ චෛතසික</a>\n')
        fp.write('<a href="javascript:void(0);" class="icon" onclick="navFunction()"> <i class="fa fa-bars"></i></a>\n')
        fp.write('</div>\n')
               
        fp.close()
    return None
########### PrepareHead_AA End ###################################



######## HtmlDropdownBlock_AA ######
def HtmlDropdownBlock_AA(block_id, in_file, playlist_title, outfile, playlist_url, idx_prefix):
    
    with open(in_file, 'r', encoding='utf-8') as fp:
        utubelink_lines = [line.strip().split() for line in fp.readlines()]

    idx = [row[0] for row in utubelink_lines]
    urls = [row[1] for row in utubelink_lines]
    dates = [row[2] for row in utubelink_lines]
    N = len(idx)

    option_n = []
    p4 = []
    option_text = []


    with open(outfile, 'a', encoding="utf-8") as fp:
        # fp.write('<h2>' + str(block_id) + '. ' + playlist_title + '</h2>\n')

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
            
            # print(url_val)
              
            idx_val = idx_prefix + str(idx[n-1]).zfill(3)

            if len(url_val) > 0:
                url_val_split = url_val.split('=')
                # print(len(url_val_split))
                
                if len(url_val_split) > 1:
                    url_video_val = url_val_split[1]
                else:
                    url_video_val = ''

            p0_short = f"{date_val} {playlist_title} {idx_val}"

            option_text.append(p0_short)
            # print(option_text[n-1])
            # print(' ' , idx[n-1] ,' ' , dates[n-1] ,' p0_short= ' , p0_short)
            
            if len(url_video_val) > 1:
                p1 = f'<iframe width="560" height="315" src="https://www.youtube.com/embed/{url_video_val}"'
                p2 = ' title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"'
                p3 = ' allowfullscreen></iframe>'
                p4_s = p1 + p2 + p3
            else:
                p4_s = ' '

            p4.append(p4_s)
            option_s = f'option{n}'
            option_n.append(option_s)

            if n == N:
                fp.write('\t<option value="' + option_n[n-1] +'" selected>' + option_text[n-1] +  '</option>\n')
            else:
                fp.write('\t<option value="' + option_n[n-1] +'">' + option_text[n-1] +  '</option>\n')

        fp.write('</select>\n')
        fp.write('<div id="content'+str(block_id)+'"></div>\n')
        fp.write('<div id="notes'+str(block_id)+'"></div>\n')
        fp.write('<script>\n')
        fp.write('\tconst select' + str(block_id) + ' = document.querySelector(\'#video_list' + str(block_id) + '\');\n')
        fp.write('\tconst content' + str(block_id) + ' = document.querySelector(\'#content' + str(block_id)+ '\');\n')
        fp.write('\t\t\tcontent' + str(block_id) + '.innerHTML = \'<p></p>' + p4[N-1] + '\';\n')
        
        fp.write('\tselect' + str(block_id) + '.addEventListener(\'change\', function() {\n')
        fp.write('\t\tif (this.value === \'option1\') {\n')
        fp.write('\t\t\tcontent' + str(block_id) +'.innerHTML = \'<p></p>' + p4[0] + '\';\n')
                
        for n in range(2, N+1):
            # print(n,' ',option_n[n-1])
            fp.write('\t\t} else if (this.value === \'' + option_n[n-1] + '\'){\n')
            fp.write('\t\t\tcontent' + str(block_id) + '.innerHTML = \'<p></p>' + p4[n-1] + '\';\n')

        fp.write('\t}\n')
        fp.write('});\n')
        fp.write('</script>\n')
        
        #### sections ###
        fp.write('<script>\n')
       
        fp.write('\tconst select1 = document.querySelector(\'#video_list\');\n')
        fp.write('\tconst notes = document.querySelector(\'#notes\');\n')
        
        
            
     
        fp.write('\tselect.addEventListener(\'change\', function() {\n')
        fp.write('\t\tif (this.value === \'option1\') {\n')
    
        fp.write('\t}\n')
        fp.write('});\n')
        fp.write('</script>\n')  
        
        
        fp.write('<br>\n')
        fp.close()

    return None
######## HtmlDropdownBlock_AA End ######


#### Begin code #################
PrepareHead_AA(html_file, series_title)

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


HtmlDropdownBlock_AA(1, utube_links_EP, series_title_EP, html_file, playlist_url_EP, idx_prefix)

block_id = '2'
idx_prefix = ''
series_title_B = "Abhidharma Aruth - B"


with open(html_file, 'a', encoding="utf-8") as fp:  
    fp.write('<h2>' + str(block_id) + '. ' + series_title_B + '</h2>\n\n')
    fp.close()
    
HtmlDropdownBlock_AA(2, utube_links_B, series_title_B, html_file, playlist_url_B, idx_prefix)

with open(html_file, 'a', encoding="utf-8") as fp:
    fp.write('</body>\n')
    fp.write('</html>\n')
    fp.close()

#####################################################


 
    




