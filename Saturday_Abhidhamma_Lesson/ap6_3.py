import re

html_head = """

<!DOCTYPE html>
<html lang="en">
<head>

    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=GT-MBNDJTD"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){
            dataLayer.push(arguments);
        }
        gtag('js', new Date());
	
  	  gtag('config', 'GT-MBNDJTD');
    </script>
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
	<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
	<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
	<link rel="icon" type="image/png" href="../images/favicon-16x16.png" sizes="16x16" />
	<link rel="manifest" href="/site.webmanifest">   
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	<link rel="stylesheet" type="text/css" href="../css/nav_menu.css">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<script src="../scripts/nav_function.js"></script>
 
    <!--========== BOX ICONS ==========-->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/boxicons@latest/css/boxicons.min.css">
    <!--========== CSS ==========-->
    <link rel="stylesheet" href="ap6-styles.css">
    <title>ප්‍රතීත්‍යසමුත්පාද විභඞ්ගය සඳහා සටහන්</title>
    <style>
        .c2 {
            color: darkblue;
        }
        .c3 {
            color: blue;
        }
    </style>
</head>
<body>
    <!--========== HEADER ==========-->
    <header class="header">
        <div class="header__container">
            <img src="../logo.svg" alt="" class="header__img"><a href="#" class="header__logo">ප්‍රතීත්‍යසමුත්පාද විභඞ්ගය සඳහා සටහන්</a>
            <!--
                <div class="header__search">
                    <input type="search" placeholder="Search" class="header__input">
                    <i class='bx bx-search header__icon'></i>
                </div>
            -->
            <div class="header__toggle">
                <i class='bx bx-menu' id="header-toggle"></i>
            </div>
        </div>
    </header>
    <!--========== NAV ==========-->
    <div class="nav" id="navbar">
        <nav class="nav__container">
            <div>
                <a href="#" class="nav__link nav__logo">
                    <i class='bx bx-home nav__icon'></i>
                    <span class="nav__logo-name">6. ප්‍රතීත්‍යසමුත්පාද විභඞ්ගය</span>
                </a>
                <div class="nav__list">
                    <div class="nav__items">
                        
                            <h3 class="nav__subtitle">අන්තර්ගතය</h3>
                            
                        <a href="#සූත්‍රාන්තභාජනිය" class="nav__link active">
                            <i class='bx bx-book-content nav__icon'></i>
                            <span class="nav__name">සූත්‍රාන්තභාජනිය</span>
                        </a>
                        <a href="#AbhidhammaBhajaniya" class="nav__link active">
                            <i class='bx bx-book-content nav__icon'></i>
                            <span class="nav__name">අභිධම‍්මභාජනියං ආරම්භය</span>
                        </a>
                        <a href="#මාතිකා" class="nav__link active">
                            <i class='bx bx-book-content nav__icon'></i>
                            <span class="nav__name">මාතිකා</span>
                        </a>
                        <a href="#පච‍්චයචතුක‍්කංමාතිකා" class="nav__link active">
                            <i class='bx bx-book-content nav__icon'></i>
                            <span class="nav__name">පච‍්චයචතුක‍්කං මාතිකා ආරම්භය</span>
                        </a>
                        <a href="#හෙතුචතුක‍්කං" class="nav__link">
                            <i class='bx bx-book-content nav__icon'></i>
                            <span class="nav__name">හෙතුචතුක‍්කං</span>
                        </a>
                        <a href="#සම‍්පයුත‍්තචතුක‍්කං" class="nav__link active">
                            <i class='bx bx-book-content nav__icon'></i>
                            <span class="nav__name">සම‍්පයුත‍්තචතුක‍්කං</span>
                        </a>
                        <a href="#අඤ‍්ඤමඤ‍්ඤචතුක‍්කං" class="nav__link">
                            <i class='bx bx-book-content nav__icon'></i>
                            <span class="nav__name">අඤ‍්ඤමඤ‍්ඤචතුක‍්කං</span>
                        </a>
                        <a href="#NawaMulaPadaMathika" class="nav__link">
                            <i class='bx bx-book-content nav__icon'></i>
                            <span class="nav__name">නව (9) මූල පද මාතිකා</span>
                        </a>
                        <!--
                        <a href="#අඤ‍්ඤමඤ‍්ඤචතුක‍්කං2" class="nav__link">
                            <i class='bx bx-book-content nav__icon'></i>
                            <span class="nav__name">අඤ‍්ඤමඤ‍්ඤචතුක‍්කං</span>
                        </a>
                        <a href="#අකුසලනිද‍්දෙසො" class="nav__link">
                            <i class='bx bx-book-content nav__icon'></i>
                            <span class="nav__name">අකුසල නිද‍්දෙසො</span>
                        </a>
                        <a href="#කුසලනිද‍්දෙසො" class="nav__link">
                            <i class='bx bx-book-content nav__icon'></i>
                            <span class="nav__name">කුසල නිද‍්දෙසො</span>
                        </a>
                        <a href="#අව්‍යාකතනිද‍්දෙසො" class="nav__link">
                            <i class='bx bx-book-content nav__icon'></i>
                            <span class="nav__name">අව්‍යාකතනිද‍්දෙසො</span>
                        </a>
                        <a href="#කුසලවිපාකමූලකං නිට‍්ඨිතං" class="nav__link">
                            <i class='bx bx-book-content nav__icon'></i>
                            <span class="nav__name">කුසලවිපාකමූලකං නිට‍්ඨිතං</span>
                        </a> 
                        <a href="#අකුසලවිපාකමූලකං නිට‍්ඨිතං" class="nav__link">
                            <i class='bx bx-book-content nav__icon'></i>
                            <span class="nav__name">අකුසලවිපාකමූලකං නිට‍්ඨිතං</span>
                        </a>  
                    -->
                        <!--
                            <div class="nav__dropdown">
                                <a href="#" class="nav__link">
                                    <i class='bx bx-book-open nav__icon' ></i>
                                    <span class="nav__name">Profile</span>
                                    <i class='bx bx-chevron-down nav__icon nav__dropdown-icon'></i>
                                </a>

                                <div class="nav__dropdown-collapse">
                                    <div class="nav__dropdown-content">
                                        <a href="#" class="nav__dropdown-item">Passwords</a>
                                        <a href="#" class="nav__dropdown-item">Mail</a>
                                        <a href="#" class="nav__dropdown-item">Accounts</a>
                                    </div>
                                </div>
                            </div>
                        
                        
                        <a href="#about" class="nav__link">
                            <i class='bx bx-book-content nav__icon'></i>
                            <span class="nav__name">About</span>
                        </a>

                        <a href="#contents" class="nav__link">
                            <i class='bx bx-bookmarks nav__icon'></i>
                            <span class="nav__name">පටුන</span>
                        </a>
                        -->
                    </div>
                    <div class="nav__items">
                        <!--
                            <h3 class="nav__subtitle">Menu</h3>
                            -->
                        <div class="nav__dropdown">
                            <a href="#" class="nav__link">
                                <i class='bx bx-book-open nav__icon'></i>
                                <span class="nav__name">ඡේද</span>
                                <i class='bx bx-chevron-down nav__icon nav__dropdown-icon'></i>
                            </a>
                            <div class="nav__dropdown-collapse">
                                <div class="nav__dropdown-content">
                                    <a href="#id347" class="nav__dropdown-item">347</a>
                                    <a href="#id348" class="nav__dropdown-item">348</a>
                                    <a href="#id365" class="nav__dropdown-item">365 Page 249</a>
                                    <a href="#id366" class="nav__dropdown-item">366 Page 252</a>
                                    <a href="#id367" class="nav__dropdown-item">367 Page 253</a>
                                    <a href="#id368" class="nav__dropdown-item">368 Page 255</a>
                                    <a href="#id369" class="nav__dropdown-item">369 Page 257</a>
                                    <a href="#p1018_end" class="nav__dropdown-item"></a>
                                </div>
                            </div>
                        </div>
                        <!--
                            <a href="#" class="nav__link">
                                <i class='bx bx-compass nav__icon' ></i>
                                <span class="nav__name">Explore</span>
                            </a>
                        
                        <a href="#sponsor" class="nav__link">
                            <i class='bx bxs-institution nav__icon'></i>
                            <span class="nav__name">අනුග්‍රහය</span>
                        </a>
                        <a href="#contact" class="nav__link">
                            <i class='bx bxs-contact nav__icon'></i>
                            <span class="nav__name">Contact</span>
                        </a>
                        -->
                    </div>
                </div>
            </div>
            <!--
                <a href="#contact" class="nav__link nav__logout">
                    <i class='bx bx-contact nav__icon' ></i>
                    <span class="nav__name">Contact X</span>
                </a>
            -->
        </nav>
    </div>
  <body>  
   
  <h1>ප්‍රතීත්‍යසමුත්පාද විභඞ්ගය සඳහා සටහන්</h1>
  <h2>Warning: මෙය ගුරුතුමා විසින් සකස් කරන ලද සටහනක් නොවේ. මෙහි වැරදි ගොඩක් අන්තර්ගතව ඇත.</h2>
  <div id="contents"></div>

  <h3>පටිච‍්චසමුප‍්පාද විභඞ‍්ගො (pages 245 - 339)</h3>
  <h3>සුත‍්තන‍්තභාජනියං (pages 244 - 249)</h3>
  <h3><a href="#AbhidhammaBhajaniya">අභිධම‍්මභාජනියං ආරම්භය  (pages 249 - 339)</a></h3>
  <h3><a href="#මාතිකා">මාතිකා (pages 249 - 257)</a></h3>
  <h3><a href="#පච‍්චයචතුක‍්කංමාතිකා">පච‍්චයචතුක‍්කං මාතිකා ආරම්භය 365 (pages 249 - 251)</a></h3>
  <h3><a href="#හෙතුචතුක‍්කං">හෙතුචතුක‍්කං 366 (pages 252 - 253)</a></h3>
  <h3><a href="#සම‍්පයුත‍්තචතුක‍්කං">සම‍්පයුත‍්තචතුක‍්කං 367 (pages 253 - 255)</a></h3>
  <h3><a href="#අඤ‍්ඤමඤ‍්ඤචතුක‍්කං">අඤ‍්ඤමඤ‍්ඤචතුක‍්කං 368 (pages 255 - 257)</a></h3>
  <h3><a href="#NawaMulaPadaMathika">නව (9) මූල පද මාතිකා</a></h3>

  <h3>පච‍්චයචතුක‍්කං</h3>
  <h3>හෙතුචතුක‍්කං</h3>
  <h3>සම‍්පයුත‍්තචතුක‍්කං</h3>
  <h3>අඤ‍්ඤමඤ‍්ඤචතුක‍්කං</h3>
  <h3>අකුසල නිද‍්දෙසො</h3>
  <h3>කුසල නිද‍්දෙසො</h3>
  <h3>අව්‍යාකතනිද‍්දෙසො</h3>
  <h3>කුසලවිපාකමූලකං නිට‍්ඨිතං</h3>
  <h3>අකුසලවිපාකමූලකං නිට‍්ඨිතං</h3>                            
                              
            
"""
def read_file_contents(input_file_s, input_file_p):
    with open(input_file_s, 'r', encoding='utf-8') as fs:
        #content_s = fs.read()
        contents_s_lines = [line.strip().split() for line in fs.readlines()]
    
    with open(input_file_p, 'r', encoding='utf-8') as fp:
        content_p = fp.read()
    return contents_s_lines, content_p
        

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regular expression to find the pattern "number." followed by any text until the next number
    pattern = r'(\d+\.\s.*?)(?=\d+\.)'

    # Find all matches
    matches = re.findall(pattern, content, re.DOTALL)

    # Write matches to new file with desired format
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_head)
        last_end = 0
        for idx, match in enumerate(matches, 1):
            start = content.find(match, last_end)
            if start > last_end:
                # Write text before numbered block in simple <p> section
                f.write(f'<p>{content[last_end:start].strip()}</p>\n')
            
            # Split multi-line match and write first line within chedaya block
            lines = match.strip().split('\n')
            # lines = match.splitlines()
            
            para_num = idx + 345
            if para_num > 401:
                para_num = para_num + 1
            
            first_line = lines[0].strip();
            (firstWord, rest) = first_line.split(maxsplit=1)

            # f.write(f'<p class="chedaya" id="id{para_num}">{lines[0].strip()}</p>\n')
            f.write(f'<p class="chedaya" id="id{para_num}"><b>{firstWord}</b> {rest}</p>\n')
            
            print(firstWord)
            print(rest)

            # Write subsequent lines within chedaya2 block
            for line in lines[1:]:
                if len(line.split()) > 5:
                    f.write(f'<p class="chedaya2">{line.strip()}</p>\n')
                else:
                    print(len(line.split()))
                    f.write(f'<h3 class="c3"><a href="#">{line.strip()}</a>   <span class="pull-right"><a href="#contents">top</a></span></h3>\n')
                
            last_end = start + len(match)
        
        # Write any remaining text after the last numbered block
        if last_end < len(content):
            f.write(f'<p>{content[last_end:].strip()}</p>\n')

# Example usage:
input_file_s= 'ap6_new.txt'
input_file_p= 'ap6_new.txt'
output_file = 'ap6_3_new.html'

contents_s_lines, contents_p = read_file_contents(input_file_s, input_file_p)

print(len(contents_s_lines))

for n in range(90, 100):
    print(contents_s_lines[n])

#contents_s_lines = [line.strip().split() for line in contents_s.readlines()]

#process_file(input_file_s, output_file)

# with open(output_file, 'a', encoding='utf-8') as f:
#     f.write('<script src="../scripts/sidebar_nav.js"></script>\n ')
#     f.write('</body>\n')
#     f.write('</html>\n')