import re

html_head = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!--========== BOX ICONS ==========-->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/boxicons@latest/css/boxicons.min.css">
    <!--========== CSS ==========-->
    <link rel="stylesheet" href="ap6-styles.css">
    <title>ප්‍රතීත්‍යසමුත්පාද විභඞ්ගය සඳහා සටහන්</title>
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
                            
                        <a href="#intro" class="nav__link active">
                            <i class='bx bx-home-alt-2 nav__icon'></i>
                            <span class="nav__name">හැදින්වීම</span>
                        </a>
                        <!--
                            <div class="nav__dropdown">
                                <a href="#" class="nav__link">
                                    <i class='bx bx-user nav__icon' ></i>
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
                        -->
                        <a href="#vishaya_karunu" class="nav__link">
                            <i class='bx bx-bookmark nav__icon'></i>
                            <span class="nav__name">විෂය කරුණු</span>
                        </a>
                        <a href="#about" class="nav__link">
                            <i class='bx bx-book-content nav__icon'></i>
                            <span class="nav__name">About</span>
                        </a>
                        <a href="#download" class="nav__link">
                            <i class='bx bx-download nav__icon'></i>
                            <span class="nav__name">Download</span>
                        </a>
                        <a href="#contents" class="nav__link">
                            <i class='bx bx-bookmarks nav__icon'></i>
                            <span class="nav__name">පටුන</span>
                        </a>
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
                                    <a href="#id366" class="nav__dropdown-item">366 Page 251</a>
                                    <a href="#p472_616" class="nav__dropdown-item">ප - බ කොටස් </a>
                                    <a href="#p616_750" class="nav__dropdown-item">භ - ල කොටස්</a>
                                    <a href="#p750_968" class="nav__dropdown-item">ඉ - ඤ කොටස්</a>
                                    <a href="#p968_1017" class="nav__dropdown-item">ව - හ කොටස්</a>
                                    <a href="#p1018_end" class="nav__dropdown-item">උපග්‍රන්ථ සහ සිතියම්</a>
                                </div>
                            </div>
                        </div>
                        <!--
                            <a href="#" class="nav__link">
                                <i class='bx bx-compass nav__icon' ></i>
                                <span class="nav__name">Explore</span>
                            </a>
                        -->
                        <a href="#sponsor" class="nav__link">
                            <i class='bx bxs-institution nav__icon'></i>
                            <span class="nav__name">අනුග්‍රහය</span>
                        </a>
                        <a href="#contact" class="nav__link">
                            <i class='bx bxs-contact nav__icon'></i>
                            <span class="nav__name">Contact</span>
                        </a>
                    </div>
                </div>
            </div>
            <!---
                <a href="#contact" class="nav__link nav__logout">
                    <i class='bx bx-contact nav__icon' ></i>
                    <span class="nav__name">Contact</span>
                </a>
            -->
        </nav>
    </div>
  <body>  
   
  <p>ප්‍රතීත්‍යසමුත්පාද විභඞ්ගය</p>
    සූත්‍රාන්තභාජනිය 
    සූත්‍රාන්තභාජනිය අවසානය.
    හේතුචතුෂ්ක යි.
    සම්ප්‍රයුක්තචතුෂ්ක යි.
    අන්‍යෝන්‍යචතුෂ්ක යි.
    මාතෘකා යි.
    ප්‍රත්‍යයචතුෂ්ක යි.
    හේතුචතුෂ්ක යි.
    සම්ප්‍රයුක්තචතුෂ්ක යි.
    අන්‍යෝන්‍යචතුෂ්ක යි
    අකුශලනිර්දේශ යි.
    කුශලනිර්දේශ යි.
    කුශලවිපාකසඞ්ඛාරමූලකය නිමි.
 <p>   අකුසලවිපාකසඞ්ඛාරමූලකය නිමි.</p>
    ක්‍රියාසංස්කාරමූලකය නිමි
    අව්‍යාකෘතනිර්දේශ යි.
    කුශලවිපාකමූලකය නිමි.
    කුසලමූලක විපාකනිර්දේශ යි
    අකුශලවිපාකමූලකය නිමි.
අභිධර්‍මභාජනිය නිමි.
<p>ප්‍රතීත්‍යසමුත්පාදවිභඞ්ගය නිමි.</p>
"""
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
                
            f.write(f'<p class="chedaya" id="id{para_num}">{lines[0].strip()}</p>\n')
            
            # Write subsequent lines within chedaya2 block
            for line in lines[1:]:
                if len(line.split()) > 5:
                    f.write(f'<p class="chedaya2">{line.strip()}</p>\n')
                else:
                    print(len(line.split()))
                    f.write(f'<h3 class="c3">{line.strip()}</h3>\n')
                
            last_end = start + len(match)
        
        # Write any remaining text after the last numbered block
        if last_end < len(content):
            f.write(f'<p>{content[last_end:].strip()}</p>\n')

# Example usage:
input_file = 'ap6_new.txt'
output_file = 'ap6_new.html'
process_file(input_file, output_file)

with open(output_file, 'a', encoding='utf-8') as f:
    f.write('</body>\n')
    f.write('</html>\n')