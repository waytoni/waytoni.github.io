import os
import sys
sys.path.append('scripts/py')
from utilities import *

basepath = './Nivan_Maga_Udesa/docs/combined_notes'
html_file = os.path.join(basepath,'NMU_file_list.html')
files = os.listdir(basepath)
series_title = 'නිවන් මග උදෙසා දේශනා සඳහා සටහන්'
NMU_styles = """
    <link rel="stylesheet" type="text/css" href="file_list.css">
"""

print(html_file)
PrepareHeadTop(html_file, series_title, NMU_styles)

NMU_intro = """
    <div>
    <center>
    <h2>රේරුකානේ චන්දවිමල හිමියන්ගේ අභිධර්ම මාර්ගය පොත <a href="./අභිධර්ම මාර්ගය.pdf" target="blank">PDF ලෙස</a> 
    හෝ <a  href="https://tipitaka.sgp1.digitaloceanspaces.com/library/%E0%B6%BB%E0%B7%9A%E0%B6%BB%E0%B7%94%E0%B6%9A%E0%B7%8F%E0%B6%B1%E0%B7%9A%20%E0%B6%A0%E0%B6%B1%E0%B7%8A%E0%B6%AF%E0%B7%8A%E2%80%8D%E0%B6%BB%E0%B7%80%E0%B7%92%E0%B6%B8%E0%B6%BD%20%E0%B7%84%E0%B7%92%E0%B6%B8%E0%B7%92%7B462%7D/%E0%B6%85%E0%B6%B7%E0%B7%92%E0%B6%B0%E0%B6%BB%E0%B7%8A%E0%B6%B8%20%E0%B6%B8%E0%B7%8F%E0%B6%BB%E0%B7%8A%E0%B6%9C%E0%B6%BA%7B463%7D.html?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=DO00W6TA6TFMRGYL3VCD%2F20240702%2Funused%2Fs3%2Faws4_request&X-Amz-Date=20240702T064753Z&X-Amz-Expires=3600&X-Amz-Signature=dffe267db8b96f4031c6b65151634140b6421b891f12b2143c2c3e41506843c4&X-Amz-SignedHeaders=host&x-id=GetObject">වෙබ් පිටුවක් ලෙස</a></h2>
    <h2>රේරුකානේ චන්දවිමල හිමියන්ගේ අභිධර්මයේ මූලික කරුණු පොත <a href="https://www.ogatharana.org/bookDownCounter.php?booknumber=15" target="blank">PDF ලෙස</a>
    හෝ <a  href="https://tipitaka.lk/library/464">වෙබ් පිටුවක් ලෙස</a></h2>
    <h2>රේරුකානේ චන්දවිමල හිමියන්ගේ පටිච්ච සමුප්පාද විවරණය පොත <a href="https://www.ogatharana.org/bookDownCounter.php?booknumber=17" target="blank">PDF ලෙස</a> 
    හෝ <a  href="https://tipitaka.lk/library/474">වෙබ් පිටුවක් ලෙස</a></h2>
    <h2>රේරුකානේ චන්දවිමල හිමියන්ගේ පොහොය දිනය පොත <a href="https://tipitaka.lk/library/498">PDF ලෙස</a> හෝ  <a href="https://tipitaka.lk/library/475">වෙබ් පිටුවක් ලෙස</a></h2>
    <h2>රේරුකානේ චන්දවිමල හිමියන්ගේ සියුලු පොත් සඳහා: <a href="https://www.ogatharana.org/" target="blank">https://www.ogatharana.org/</a> 
    හෝ <a href="https://tipitaka.lk/library/462" target="blank">https://tipitaka.lk/library/462</a></h2>
    <h2><a href="/documents/දර්ශන ඥාණය මූලික සූත්‍ර 01.pdf" target="_blank">නිවන් මග උදෙසා දර්ශන ඥාණය සඳහා මූලික සූත්‍ර</a></h2>
    </center>
    </div>
"""


with open(html_file, 'a', encoding="utf-8") as f:
    f.write(NMU_intro)
    # iterate over all the files
    f.write('\t<div class="grid-container">\n')
    for file in files:
        # check if the file extension is .jpg, .png or .jpeg
        if file.endswith(('jpg', 'jpeg', 'png')):
            # write the image file names to the file
            f.write("\t\t<div class=""grid-item"">\n")
            f.write('\t\t<a href="' + file + '"><img src="thumbnails/' + file + '" alt="' + file + '"></a>')
            f.write('\t\t<p>' + file + '</p>\n')
            f.write('\t\t</div>\n')
    f.write('\t</div>\n')
    f.write('</body>\n')
    f.write('</html>\n')


    
    
 