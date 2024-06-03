import os
import sys
sys.path.append('scripts/py')
from utilities import *

basepath = './documents'
html_file = os.path.join(basepath,'file_list.html')
files = os.listdir(basepath)
series_title = 'සියලු අභිධම්ම දේශනා සඳහා සටහන්'
Filelist_styles = """
    <link rel="stylesheet" type="text/css" href="file_list.css">
"""

print(html_file)
PrepareHeadTop(html_file, series_title, Filelist_styles)

FileList_intro = """
    <div>
    <center>
    <h2>රේරුකානේ චන්දවිමල හිමියන්ගේ <a href="./අභිධර්ම මාර්ගය.pdf" target="blank">අභිධර්ම මාර්ගය</a> පොත</h2>
    <h2>රේරුකානේ චන්දවිමල හිමියන්ගේ <a href="https://www.ogatharana.org/bookDownCounter.php?booknumber=15" target="blank">අභිධර්මයේ මූලික කරුණු</a> පොත</h2>
    <h2>රේරුකානේ චන්දවිමල හිමියන්ගේ <a href="https://www.ogatharana.org/bookDownCounter.php?booknumber=17" target="blank">පටිච්ච සමුප්පාද විවරණය</a> පොත</h2>
    <h2>රේරුකානේ චන්දවිමල හිමියන්ගේ <a href="https://www.ogatharana.org/" target="_blank">සියුලු පොත් සඳහා</a></h2>
    <h2><a href="http://dr.lib.sjp.ac.lk/handle/123456789/2139" target="_blank"> විභංගප්පකරණ (1)</a> [click on View/Open to download the pdf version]
    <h2><a href="./විභඞ්ගප්පකරණං V 1.05 Final.pdf" target="_blank">ගුරුතුමා විසින් පටිච‍්චසමුප‍්පාද විභඞ්ගය අධ්යයනය සඳහා සකස්කරන ලද විශේෂ සටහන</a></h2>
    </center>
    </div>
"""


with open(html_file, 'a', encoding="utf-8") as f:
    f.write(FileList_intro)
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


    
    
 