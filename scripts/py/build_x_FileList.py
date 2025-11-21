import os
import sys
sys.path.append('scripts/py')
from utilities import *

basepath = './x/NotesForDesana'
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



file_list = ['0001 ලෝක ධාතුවේ පරමාර්ථ ධර්ම.png', '0002 ප්\u200dරසාද රූප 5 සහ ගෝචර රූප 7.png', 
           '0002 රූප පරමාර්ථ.jpg', '0002A රූප පරමාර්ථ.png',
           '0003 ප්\u200dරසාද පිහිටා තිබෙන ස්ථාන.png', '0003 රූප කලාපය.jpg', 
            '0004 ආයතන ධාතු විග්\u200dරහය සහ පරමාර්ථ ධර්මයන්ගේ ආයුෂ.png', 
            '0004 ප්\u200dරසාද ඇසුරු කරගෙන පහල වන සිත් 89.png', '0004 ලෝක ධාතු.jpg', 
            '0005 ලෝක ධාතුවේ සත්ව තල පිහිටුම.png', '0005 සත්ව තල.jpg', 
            '0006 චක්ෂු සහ ශෝත ප්\u200dරසාද.jpg', '0006 නියාම ධර්මතා.png', 
            '0007 ජිහ්වා සහ ඝ්\u200dරාණ ප්\u200dරසාද.jpg', '0008 චක්ෂුර්ද්වාරික අතිමහන්තාරම්මණ වීථිය.jpg',                     
            '0009 කුසල්-අකුසල් කාම ජවන චිත්තයන් හා ප්\u200dරතිසංධි විපාක.jpg', 
            '0010 ශරීරයෙහි සියලු ප්\u200dරසාද.jpg', 
            '0010A කාමාවචර කුසල් අකුසල් සිත්.png', 
            '0010B කාමාවචර කුසල් අකුසල් සිත්.png'                           
            '0011 A චිත්ත වීති උදාහරණ 1-6 .jpg', 
            '0011 A01 සම්බුදුපියාණන්ට මුගලන් මහරහතුන්ට හා ආනන්ද හාමුදුරුවන්ට  තීර්තකයෙකු බැනීම.jpg', 
            '0011 A02 තීර්තකයෙකුට දේව්දත් තෙරට සම්බුදුපියාණන්ව දැකීම.jpg', 
            '0011 A03 සැදැහැවත් බෞද්ධයෙකු සම්බුදුපියාණන්ව දැකීම.jpg', '0011 A04 සැදැහැවත් බෞද්ධයෙකු පන්සලක් දැකීම.jpg', 
            '0011 A05 යමෙකු මළපහ ගොඩක් දැකීම.jpg', '0011 A06 යමෙකු රසවත් ආහාරයක් රස විදීම.jpg', 
            '0011 A5 යමෙකු මළපහ ගොඩක් දැකීම.jpg', '0011 B චිත්ත වීති උදාහරණ 7-14.jpg', 
            '0011 B07 සතෙකුට බියකරු හඬක් ඇසීම.jpg', '0011 B08 සතෙකුට දරුණු පහරක් වැදීම.jpg', 
            '0011 B09 යමෙකුට බියකරු හඬක් ඇසීම.jpg', '0011 B10 සතෙකුට සම්බුදුපියාණන්ව දැකීම.jpg', 
            '0011 B11 යෝනිසෝ මනසිකාර යෙදෙන යමෙකුට බියකරු හඬක් ඇසීම.jpg', 
            '0011 B12 යෝනිසෝ මනසිකාර යෙදෙන යමෙකුට දරුණු පහර රක් වැදීම.jpg', 
            '0011 B13 යෝනිසෝ මනසිකාර යෙදෙන යමෙකුට මළපහ ගොඩක් දැකීම.jpg', 
            '0011 B14 යෝනිසෝ මනසිකාර යෙදෙන යමෙකුට ආහාරයක් රස විදීම.jpg', 
            '0012 පටිච්චසමුප්පාදය.png', '0013 අකුශල කුශල අව්\u200dයාකෘත ලෝකෝත්තර ධර්ම.png', 
            '0014 A මාර්ග සහ ඵල සමාපත්ති විථී.jpg', '0014 B මාර්ග සහ ඵල සමාපත්ති විථී.jpg', 
            '0014 චෛතසික දෙපනස.jpg', '0015 A ත්\u200dරිහේතුක පෘතග්ජනයාගේ සිත් 54.jpg', 
            '0015 B1 දුර්ගති අහේතුක සිත් 37 (සතර අපා).jpg', 
            '0015 B2 සුගති අහේතුක සිත් 41 (උපතින් අන්ධ-ගොළු).jpg', 
            '0015 C චක්ෂුර්ද්වාරික අතිමහන්තාරම්මණ විථිය.jpg', '0016 A චක්ෂුර්ද්වාරික අතිමහන්තාරම්මණ වීථි හා මහන්තාරම්මණ වීථි.jpg', 
            '0016 B චක්ෂුර්ද්වාරික පරිත්තාරම්මණ වීථි සය හා අතිපරිත්තාරම්මණ වීථි සය.jpg', 
            '0016 චතුර්භූමික සිත් සහ ධර්ම.jpg', '0016 චිත්ත චෛතසික ධර්ම සම්ප්\u200dරයෝගය.jpg', 
            '0017 A චෛතසික පරමාර්ථ ධර්ම 52.png', '0017 B චෛතසික පරමාර්ථ ධර්ම 52.png', '0017 ආයතන සැකසුම.jpg',
            '0018 A රූප විභාගය සහ රූප කලාප විභාගය.jpg', '0018 පරමාර්ථ සහ පංචස්කන්ධය.jpg', 
            '0019 B සමථ භාවනා - ආනාපාන සතිය වැඩීම ආසන්නව පහල වන චිත්ත වීථි අනුව.jpg', 
            '0020 පරමාර්ථ ගති ලක්ෂණ.jpg', '0022 සිත් සතර ආකාරය.jpg', '0024 ද්වාර සංග්\u200dරහය.jpg', 'ආර්යය ලෝකය.png', 
            'කාලත්\u200dරයේම ලෝක ධාතුවේ පහලවෙන වීති හා වීතියට අදාල සිත්.jpg', 
            'චිත්ත චෛතසික ධර්ම ප්\u200dරත්\u200dයයෙන් උපදින රූප වගුව.jpg', 
            'චිත්ත චෛතසික සම්ප්\u200dරයෝගය එකචිත්තක්ඛඛණික පටිච්චසමුප්පාදය.jpg', 
            'චිත්ත චෛතසික සම්ප්‍රයෝගය පුද්ගලයන්ට ලැබෙන සිත් භුමි වලට ලැබෙන සිත්.png', 
            'ශමථ කර්මස්ථාන සතළිස විනිශ්චය.png']


print(file_list)

# Set the desired width for the resized images
width = 300

# Set the path to the folder containing the images
folder_path = './x/NotesForDesana'

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
    
 