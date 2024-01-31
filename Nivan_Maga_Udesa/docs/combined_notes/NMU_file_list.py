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

    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="../../../css/nav_menu.css">
    <link rel="stylesheet" type="text/css" href="file_list.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <script src="../../../scripts/menu_function.js"></script>
    <link rel="icon" type="image/png" href="../../../images/favicon-16x16.png" sizes="16x16" />
    <title>නිවන් මග උදෙසා දේශනා සඳහා සටහන් ... </title>
</head>

<body>  
    <div class="topnav" id="Topnavbar">
        <a href="https://waytoni.github.io/" class="active">Home </a>
        <a href="../../../All_Playlists/සියුලු_දේශනා.html">සියලුම දේශනා </a>
        <a href="../../../Paramartha_Video/Paramartha_Video.html">පරමාර්ථ ලෝකය දේශනා </a>
        <a href="../../../Anichcha_Dukka_Anathma_Series/Anichcha_Dukka_Anathma.html">අනිච්ච, දුක්ඛ, අනත්ත දේශනා</a>
		<a href="../../../Saturday_Abhidhamma_Lesson">තුන්කල්හි වෙනස් නොවන ලොව එකම විශ්ව දර්ශනය දේශනා</a>
		<a href="../../../Abhidharma_Aruth/index.html">අභිධර්ම අරුත් දේශනා</a>
        <a href="../../../Nivan_Maga_Udesa">නිවන් මග උදෙසා දේශනා</a>
        <a href="../../../Chithatha_Chithasika/Chiththa_Chithasika.html">චිත්ත සහ චෛතසික </a>
        <a href="javascript:void(0);" class="icon" onclick="navFunction()">
            <i class="fa fa-bars"></i>
        </a>
    </div>
    
    <div>
    <h2><center>රේරුකානේ චන්දවිමල හිමියන්ගේ <a href="./අභිධර්ම මාර්ගය.pdf" target="blank">අභිධර්ම මාර්ගය</a>පොත
    </center></h2>
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
    
    
 