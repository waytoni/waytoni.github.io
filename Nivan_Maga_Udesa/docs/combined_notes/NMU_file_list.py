import os

# directory path
dir_path = './Nivan_Maga_Udesa/docs/combined_notes'

# get all files in the directory
files = os.listdir(dir_path)

file_header = """<!DOCTYPE html>
<html lang="en">

<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=GT-MBNDJTD"></script>
    <script>
        window.dataLayer = window.dataLayer || [];

        function gtag() {
            dataLayer.push(arguments);
        }
        gtag('js', new Date());

        gtag('config', 'GT-MBNDJTD');
    </script>

    <link rel="icon" type="image/png" href="images/favicon-16x16.png" sizes="16x16" />
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="manifest" href="/site.webmanifest">
    
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <link rel="stylesheet" type="text/css" href="../../../css/nav_menu.css">
    <link rel="stylesheet" type="text/css" href="file_list.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <script src="../../../scripts/nav_function.js"></script>
    <title>නිවන් මග උදෙසා දේශනා සඳහා සටහන් ... </title>
</head>

<body>  
    <div class="topnav" id="Topnavbar">
        <a href="https://waytoni.com/" class="active"><i style="font-size:24px" class="fa">&#xf015;</i></a>
        <a href="/All_Playlists/SiyaluDesana.html">පසුගිය සහ සියලුම දේශනා</a>
        <a href="/Paramartha_Video/Paramartha_Video.html">පරමාර්ථ ලෝකය දේශනා </a>
        <a href="/Anichcha_Dukka_Anathma_Series/Anichcha_Dukka_Anathma.html">අනිච්ච, දුක්ඛ, අනත්ත දේශනා </a>
        <a href="/Chithatha_Chithasika/Chiththa_Chithasika.html">චිත්ත සහ චෛතසික</a>
        <div class="dropdown">
          <button class="dropbtn">දැනට පැවැත්වෙන දේශනා
            <i class="fa fa-caret-down"></i>
          </button>
          <div class="dropdown-content">
            <a href="/Nivan_Maga_Udesa/index.html">නිවන් මග උදෙසා දර්ශන ඥාණය</a>
            <a href="/Saturday_Abhidhamma_Lesson">තුන්කල්හි වෙනස් නොවන ලොව එකම විශ්ව දර්ශනය දේශනා</a>
            <a href="/Abhidharma_Aruth">අභිධර්ම අරුත් දේශනා</a>
            <a href="/Suthamaya/index.html">සුතමයඤාණං දේශනා</a>
            <a href="/VisheshaDesana/VisheshaDesana.html">විශේෂ දේශනා</a>
            <a href="/KalutaraBodhiya/I_series/I_series.html">කළුතර බෝධි පරිශ්‍රයේදී පැවැත්වුන 9වෙනි දේශනා මාලාව</a>
          </div>
        </div> 
        <a href="javascript:void(0);" style="font-size:15px;" class="icon" onclick="navFunction()">&#9776;</a>
    </div>
    
    <div>
   
    <center>
    <h2>රේරුකානේ චන්දවිමල හිමියන්ගේ අභිධර්ම මාර්ගය පොත <a href="./අභිධර්ම මාර්ගය.pdf" target="blank">PDF ලෙස</a> 
    හෝ <a  href="https://tipitaka.lk/library/463">වෙබ් පිටුවක් ලෙස</a></h2>
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
# create file for writing
with open(dir_path+'/NMU_file_list.html', 'w', encoding="utf-8") as f:
    # iterate over all the files
    f.write(file_header)
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
    
    
 