import os
import shutil

import re

def create_hyperlink(url):
    return f'<a href="{url}" target="_blank">{url}</a>'

def read_sections(filename):
    sections = {}  # Dictionary to store sections

    with open(filename, 'r', encoding="utf-8") as file:
        current_section = None

        for line in file:
            line = line.strip()

            if line.startswith('#'):
                current_section = int(line[1:])  # Extract the number after '#'
                sections[current_section] = []  # Initialize the section list
            elif current_section is not None:
                # Search for URLs in the line and create hyperlinks
                urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
                for url in urls:
                    line = line.replace(url, create_hyperlink(url))
                sections[current_section].append(line)  # Add modified line to the current section

    return sections

filename = 'Nivan_Maga_Udesa/Nivan_Maga_Udesa_notes.txt'  
sections = read_sections(filename)


with open('Nivan_Maga_Udesa/nivan_maga_udesa_youtube_links.txt', 'r') as fp:
    utubelink_lines = [line.strip().split() for line in fp.readlines()]

idx = [row[0] for row in utubelink_lines]
urls = [row[1] for row in utubelink_lines]
dates = [row[2] for row in utubelink_lines]
N = len(idx)

##



##

option_n = []
p4 = []
option_text = []

text_filename = 'Nivan_Maga_Udesa/nivan_maga_udesa_working_B.txt'


# Uncomment the following line only if everything is okay
html_filename = 'Nivan_Maga_Udesa/index.html'

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
    fp.write('\t<title>නිවන් මග උදෙසා දර්ශන ඥාණය - දේශනා</title>\n')
    
    fp.write('</head>\n<body>\n')
    
    fp.write('<div class="topnav" id="Topnavbar">\n')
    fp.write('<a href="https://waytoni.github.io/" class="active">Home </a>\n') 
    fp.write('<a href="../All_Playlists/සියුලු_දේශනා.html">අභිධම්ම දේශනා </a>\n')
    
    fp.write('<a href="../Paramartha_Video/Paramartha_Video.html">පරමාර්ථ ලෝකය දේශනා </a>\n \
        <a href="../Anichcha_Dukka_Anathma_Series/Anichcha_Dukka_Anathma.html">අනිච්ච, දුක්ඛ, අනත්ත දේශනා </a>\n \
        <a href="../Zoom_Info/zoom_info.html">Join Zoom Live Class </a>\n \
        <a href="../Chithatha_Chithasika/Chiththa_Chithasika.html">චිත්ත සහ චෛතසික</a>\n')
    fp.write('<a href="javascript:void(0);" class="icon" onclick="navFunction()"> <i class="fa fa-bars"></i></a>\n')
    fp.write('</div>\n')
    
    fp.write('<h1>නිවන් මග උදෙසා දර්ශන ඥාණය - දේශනා</h1>\n')

    fp.write('<p></p>\n')
    fp.write('<p>සිකුරාදා සවස 6.00 සිට 8:00 දක්වා</p>\n')
    fp.write('<p><a href="zoom_details.html">Zoom සජීවීව සම්බන්ධ වීමට</a></p>\n')

    #fp.write('<a href="https://www.youtube.com/playlist?list=PLqESXbJ82aIip-TA7Efg5JjwmEDJ95kAx">Watch full playlist in YouTube</a>\n')
    
    fp.write('<p></p>\n<p>Select a video from the dropdown menu</p>    <p></p>\n')
    
    # fp.write('<p></p>\n<p>පතන මෙනුවෙන් වීඩියෝවක් තෝරන්න</p>    <p></p>\n')
    

    fp.write('<select id="video_list">\n')
    
    for n in range(1, N+1):
        url_val = urls[n-1]
        date_val = dates[n-1]
        url_video_val = ''
        idx_val = idx[n-1]

        if len(idx_val) > 2:
            idx_val = 'A' + idx_val
        elif len(idx_val) > 1:
            idx_val = 'A0' + idx_val
        else:
            idx_val = 'A00' + idx_val

        if len(url_val) > 0:
            url_val_split = url_val.split('=')
            url_video_val = url_val_split[1]

        p0_short = f"{date_val} නිවන් මග උදෙසා දර්ශන ඥාණය - දේශනා අංක {idx_val}"

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
    
    fp.write('<div id="content"></div>\n')
    fp.write('<div id="notes"></div>\n')
    
    
    #####  --- videos
    fp.write('<script>\n')
    fp.write('\tconst select = document.querySelector(\'#video_list\');\n')
    fp.write('\tconst content = document.querySelector(\'#content\');\n')
    fp.write('\t\t\tcontent.innerHTML = \'<p></p>' + p4[N-1] + '\';\n')
    
    fp.write('\tselect.addEventListener(\'change\', function() {\n')
    fp.write('\t\tif (this.value === \'option1\') {\n')
    fp.write('\t\t\tcontent.innerHTML = \'<p></p>' + p4[0] + '\';\n')
            
    for n in range(2, N+1):
        # print(n,' ',option_n[n-1])
        fp.write('\t\t} else if (this.value === \'' + option_n[n-1] + '\'){\n')
        fp.write('\t\t\tcontent.innerHTML = \'<p></p>' + p4[n-1] + '\';\n')

    fp.write('\t}\n')
    fp.write('});\n')
    fp.write('</script>\n')
    
    ##### --- notes
    fp.write('<script>\n')
    fp.write('\tconst select1 = document.querySelector(\'#video_list\');\n')
    fp.write('\tconst notes = document.querySelector(\'#notes\');\n')
    lines = sections[n]

    
    fp.write('\t\t\tnotes.innerHTML = \'') 
    fp.write('<p>'+'දේශනාව සඳහා සටහන්'+'</p>')
    for line in lines:
            fp.write('<p>'+line+'</p>')
    fp.write('\';\n')
            
     
    fp.write('\tselect.addEventListener(\'change\', function() {\n')
    fp.write('\t\tif (this.value === \'option1\') {\n')
    
    lines = sections[1]
    #fp.write('\t\t\tnotes.innerHTML = \'<p>'+ lines[0] + '</p>' + '\';\n')
    
    fp.write('\t\t\tnotes.innerHTML = \'') 
    fp.write('<p>'+'දේශනාව සඳහා සටහන්'+'</p>')
    for line in lines:
        fp.write('<p>'+line+'</p>')
    fp.write('\';\n')
            
    for n in range(2, N+1):
        # print(n,' ',option_n[n-1])
        
        fp.write('\t\t} else if (this.value === \'' + option_n[n-1] + '\'){\n')
        lines = sections[n]
        
        if len(lines) > 0:
            print(f"section has content {n}  {len(lines)}")
        
            fp.write('\t\t\tnotes.innerHTML = \'') 
            fp.write('<p>'+'දේශනාව සඳහා සටහන්'+'</p>\';\n')
            for line in lines:
                fp.write('\t\t\tnotes.innerHTML +=\'<p>'+line+'</p>\';\n')
            fp.write('\n')
        
        else:
            fp.write('\t\t\tnotes.innerHTML = \'\';\n') 
        # fp.write('\t\t\tnotes.innerHTML = \'<p></p>' + lines[0] + '\';\n')

    fp.write('\t}\n')
    fp.write('});\n')
    fp.write('</script>\n')
    
    
    #####
    
    fp.write('<br>\n')
#    fp.write('<li><a href="../documents/file_list.html">අභිධම්ම දේශනා සඳහා සටහන්</a></li>\n')
    
    fp.write('</body>\n')
    fp.write('</html>\n')
    fp.close()

shutil.copy2(text_filename, html_filename, follow_symlinks=False)
os.remove(text_filename)
