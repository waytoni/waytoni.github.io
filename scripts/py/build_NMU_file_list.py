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
    <h2>රේරුකානේ චන්දවිමල හිමියන්ගේ අභිධර්ම මාර්ගය පොත <a href="./අභිධර්ම මාර්ගය.pdf" target="_blank">PDF ලෙස</a> 
    හෝ <a  href="https://tipitaka.lk/library/463" target="_blank">වෙබ් පිටුවක් ලෙස</a></h2>
    <h2>රේරුකානේ චන්දවිමල හිමියන්ගේ අභිධර්මයේ මූලික කරුණු පොත <a href="https://www.ogatharana.org/bookDownCounter.php?booknumber=15" target="_blank">PDF ලෙස</a>
    හෝ <a  href="https://tipitaka.lk/library/464" target="_blank">වෙබ් පිටුවක් ලෙස</a></h2>
    <h2>රේරුකානේ චන්දවිමල හිමියන්ගේ චතුරාර්‍ය්‍ය සත්‍යය පොත <a href="https://www.ogatharana.org/bookDownCounter.php?booknumber=9" target="_blank">PDF ලෙස</a> 
    හෝ <a  href="https://tipitaka.lk/library/470" target="_blank">වෙබ් පිටුවක් ලෙස</a></h2>
    <h2>රේරුකානේ චන්දවිමල හිමියන්ගේ පටිච්ච සමුප්පාද විවරණය පොත <a href="https://www.ogatharana.org/bookDownCounter.php?booknumber=17" target="_blank">PDF ලෙස</a> 
    හෝ <a  href="https://tipitaka.lk/library/474" target="_blank">වෙබ් පිටුවක් ලෙස</a></h2>
    <h2>රේරුකානේ චන්දවිමල හිමියන්ගේ පොහොය දිනය පොත <a href="https://tipitaka.lk/library/498" target="_blank">PDF ලෙස</a> හෝ  <a href="https://tipitaka.lk/library/475">වෙබ් පිටුවක් ලෙස</a></h2>
    <h2>රේරුකානේ චන්දවිමල හිමියන්ගේ සියුලු පොත් සඳහා: <a href="https://www.ogatharana.org/" target="_blank">https://www.ogatharana.org/</a> 
    හෝ <a href="https://tipitaka.lk/library/462" target="_blank">https://tipitaka.lk/library/462</a></h2>
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


    
    
 