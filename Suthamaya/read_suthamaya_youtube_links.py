import io
import shutil

with open('Suthamaya/suthamaya.txt', 'r') as fp:
    utubelink_lines = [line.strip().split() for line in fp.readlines()]

idx = [row[0] for row in utubelink_lines]
urls = [row[1] for row in utubelink_lines]
dates = [row[2] for row in utubelink_lines]
N = len(idx)

option_n = []
p4 = []
option_text = []

text_filename = 'Suthamaya/suthamaya_working.txt'


# Uncomment the following line only if everything is okay
html_filename = 'Suthamaya/Suthamaya_A.html'

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
    fp.write('\t<title>සුතමයඤාණං - දේශනා</title>\n')
    
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
    
    fp.write('<h1>සුතමයඤාණං - දේශනා</h1>\n')

    fp.write('<p></p>\n')

    #fp.write('<a href="https://www.youtube.com/playlist?list=PLqESXbJ82aIip-TA7Efg5JjwmEDJ95kAx">Watch full playlist in YouTube</a>\n')
    
    fp.write('<p></p>\n<p>Select a video from the dropdown menu</p>    <p></p>\n')
    
    # fp.write('<p></p>\n<p>පතන මෙනුවෙන් වීඩියෝවක් තෝරන්න</p>    <p></p>\n')
    

    fp.write('<select id="video_list">\n')
    
    for n in range(1, N+1):
        url_val = urls[n-1]
        date_val = dates[n-1]
        url_video_val = ''
        idx_val = idx[n-1]
        
        idx_val = str(idx[n-1]).zfill(3)

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
    
    fp.write('<br>\n')
#    fp.write('<li><a href="../documents/file_list.html">අභිධම්ම දේශනා සඳහා සටහන්</a></li>\n')
    
    fp.write('</body>\n')
    fp.write('</html>\n')
    fp.close()

shutil.copy2(text_filename, html_filename, follow_symlinks=False)
