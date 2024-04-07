import io
import shutil

import re

# Define a dictionary to map keywords to html tags
keyword_dict = {
    "pdf": "<a href=\"{}\">{}</a>",
    "img": "<img src=\"docs/{}\" width=95%>",
    "url": "<a href=\"{}\" target=\"_blank\" >{}</a>",
    "PDF": "<a href='\"docs/{}\">{}</a>",
    "IMG": "<img src=\"docs/{}\" width=95%>",
    "URL": "<a href=\"{}\">{}</a>"
}

# Pattern to match any of the keywords 
pattern = r"(pdf|PDF|img|IMG|url|URL)::"


def ReadSections(filename):
    sections = {}  

    with open(filename, 'r', encoding="utf-8") as file:
        current_section = None

        for line in file:
            line = line.strip()

            if line.startswith('#'):
                current_section = int(line[1:])  # Extract the number after '#'
                sections[current_section] = []  # Initialize the section list
            elif current_section is not None:
                line = line.strip()
                
                # Split the line by the pattern
                parts = re.split(pattern, line)
                
                # Check if there are more than one part
                if len(parts) > 1:
                    # Get the intro text as the first element of the list
                    intro_text = parts[0].strip()
                    # Initialize an empty string for the new string
                    new_string = intro_text
                    # Loop through the rest of the parts in pairs of keyword and text related to keyword
                    for i in range(1, len(parts), 2):
                        # Get the keyword and the text related to keyword
                        keyword = parts[i].strip()
                        text_related_to_keyword = parts[i+1].strip()
                        # Check if the keyword is a valid keyword
                        if keyword in keyword_dict:
                            # Get the html tag for the keyword
                            html_tag = keyword_dict[keyword]
                            # Format the html tag with the text related to keyword
                            html_tag = html_tag.format(text_related_to_keyword, text_related_to_keyword)
                            # Append a space and the html tag to the new string
                            new_string += " " + html_tag
                        else:
                            # If the keyword is not a valid keyword, append a space and the original pair of parts to the new string
                            new_string += " " + keyword + "::" + text_related_to_keyword
                else:
                    # If there is only one part, use it as the new string
                    new_string = parts[0]
                # Print the new string
                print(new_string)
                
                sections[current_section].append(new_string)  # Add modified line to the current section

    return sections


######## HtmlDropdownBlock ######
def HtmlDropdownBlock(block_id, in_file, playlist_title, outfile, playlist_url, idx_prefix, sections):
    
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
        
        fp.write('<center>\n')

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
        
        fp.write('</center>\n')
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
        
        try:
            lines = sections[n]
        except:
            notes_present = False
            lines = []
        else:
            notes_present = True    

        print(n, ' *0*0*0*0*0*0*0*0*0*0*0*0*0*0*0*0*0*0*0*0*0*0*0*0*0*0*0* ', '\n'  )
    
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
            # lines = sections[n]
            
            try:
                lines = sections[n]
            except:
                notes_present = False
                lines = []
            else:
                notes_present = True  
            
            if len(lines) > 0:
                # print(f"section has content {n}  {len(lines)}")
            
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
        
        
        fp.write('<br>\n')
        fp.close()

    return None
######## HtmlDropdownBlock End ######


######## PrepareHead Testing ##########
def PrepareHead(text_filename, series_title): 
    
    with open(text_filename, 'w', encoding="utf-8") as fp:
        fp.write('<html>\n<head>\n')
    
        with open('assets/py/analytics_tag.txt', 'r', encoding="utf-8") as ftag:
            tag_info = ftag.read()
            fp.write(tag_info)
            ftag.close()
        
        with open('assets/py/page_head.txt', 'r', encoding="utf-8") as fhead:
            head_info = fhead.read()
            fp.write(head_info)
            fhead.close()   
             
        fp.write('\n')    
        
        title_line = '\t<title>'+ series_title + '</title>\n'
        fp.write(title_line)
        
        fp.write('</head>\n')
        fp.write('<body ata-spy="scroll" data-target=".navbar" data-offset="40" id="home">\n')
        
        with open('assets/py/navigation_header_1stLevel.txt', 'r', encoding="utf-8") as fnavbar:
            navbar_info = fnavbar.read()
            fp.write(navbar_info)
            fnavbar.close()
        
        fp.close()
    return None
########### PrepareHead End ###################################


######## PrepareHead_2ndLevel Testing ##########
def PrepareHead_2ndLevel(text_filename, series_title): 
    
    with open(text_filename, 'w', encoding="utf-8") as fp:
        fp.write('<html>\n<head>\n')
    
        with open('assets/py/analytics_tag.txt', 'r', encoding="utf-8") as ftag:
            tag_info = ftag.read()
            fp.write(tag_info)
            ftag.close()
        
        with open('assets/py/page_head.txt', 'r', encoding="utf-8") as fhead:
            head_info = fhead.read()
            fp.write(head_info)
            fhead.close()   
             
        fp.write('\n')    
        
        title_line = '\t<title>'+ series_title + '</title>\n'
        fp.write(title_line)
        
        fp.write('</head>\n')
        fp.write('<body ata-spy="scroll" data-target=".navbar" data-offset="40" id="home">\n')
        
        with open('assets/py/navigation_header_2ndLevel.txt', 'r', encoding="utf-8") as fnavbar:
            navbar_info = fnavbar.read()
            fp.write(navbar_info)
            fnavbar.close()
        
        fp.close()
    return None
########### PrepareHead_2ndLevel End ###################################


######## PrepareTail ##########
def PrepareTail(text_filename): 
    with open(text_filename, 'a', encoding="utf-8") as fp:
        fp.write('<script src="../assets/vendors/jquery/jquery-3.4.1.js"></script>\n')
        fp.write('<script src="../assets/vendors/bootstrap/bootstrap.bundle.js"></script>\n')
        fp.write('<script src="../assets/js/waytoni.js"></script>\n')
        fp.write('</body>\n')
        fp.write('</html>\n')
        fp.close()
    return None
########### PrepareTail End ###################################


######## PrepareTail - 2nd level ##########
def PrepareTail_2ndLevel(text_filename): 
    with open(text_filename, 'a', encoding="utf-8") as fp:
        fp.write('<script src="../../assets/vendors/jquery/jquery-3.4.1.js"></script>\n')
        fp.write('<script src="../../assets/vendors/bootstrap/bootstrap.bundle.js"></script>\n')
        fp.write('<script src="../../assets/js/waytoni.js"></script>\n')
        fp.write('</body>\n')
        fp.write('</html>\n')
        fp.close()
    return None
    
##############################################################################