import os
import sys
sys.path.append('scripts/py')
from utilities import *

basepath = './documents/NotesForDesana'
intro_file = os.path.join(basepath, 'NotesForDesana_intro.html')
html_file = os.path.join(basepath,'NotesForDesana.html')
files = os.listdir(basepath)
series_title = 'සියලු දේශනා සඳහා සටහන්'
Filelist_styles = """
    <link rel="stylesheet" type="text/css" href="/css/file_list.css">
"""
styles_file ='css/file_list.css'

print(html_file)
PrepareHeadSimpleStyles(html_file, series_title, Filelist_styles)

FileList_intro = """
    <div>
    <center>
    <h2>රේරුකානේ චන්දවිමල හිමියන්ගේ අභිධර්ම මාර්ගය පොත <a href="https://tipitaka.lk/library/484" target="_blank">PDF ලෙස</a> 
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
    <h2><a href="/documents/දර්ශන ඥානය මූලික සූත්‍ර 01.pdf" target="_blank">දේශනා සඳහා භාවිතා කරන ලද මූලික සූත්‍ර</a></h2>
    <h2><a href="/documents/pdfs/Pragna Paramithawa.pdf" target="_blank">ප්‍රඥා පාරමිතාව</a> [දේශනා වලට සම්බන්ධ වන විට මෙම ලේඛනය A3 පොතක් ලෙස මුද්‍රණය කර පන්තියට රැගෙන එන්න.]</h2>
    </center>
    </div>
"""

with open(html_file, 'a', encoding='utf-8') as fp:
    with open(intro_file, 'r', encoding='utf-8') as fintro:
        page_intro = fintro.read()
        fp.write(page_intro)
        fintro.close()
        fp.close()
        
with open(html_file, 'a', encoding="utf-8") as f:
    # f.write(FileList_intro)
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


from PIL import Image
import os

# Set the desired width for the resized images
width = 300

# Set the path to the folder containing the images
folder_path = './documents/NotesForDesana'

# Loop through all the files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an image
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
        # Open the image file
        with Image.open(os.path.join(folder_path, filename)) as img:
            # Calculate the height of the resized image to maintain aspect ratio
            height = int((float(img.size[1]) * float(width / float(img.size[0]))))
            # Resize the image
            img = img.resize((width, height))
            # Save the resized image with a new filename
            #img.save(os.path.join(folder_path+'/'+'thumbnails', f'{filename[:-4]}_resized.jpg'))
            img.save(os.path.join(folder_path+'/'+'thumbnails', f'{filename}'))    
    
 