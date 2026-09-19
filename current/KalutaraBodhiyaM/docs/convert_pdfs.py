import os
import pdfplumber
import glob

html_template = """<!DOCTYPE html>
<html lang="si">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>

    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-B9ZTNLS3FQ"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){{dataLayer.push(arguments);}}
        gtag('js', new Date());
        gtag('config', 'G-B9ZTNLS3FQ');
    </script>

    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="manifest" href="/site.webmanifest">   

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Sinhala:wght@300;400;600;700&display=swap" rel="stylesheet">

    <link rel="stylesheet" type="text/css" href="/css/nav_menu.css">
    <link rel="stylesheet" type="text/css" href="/css/series_page_style_green.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <script src="/scripts/nav_function.js"></script>
    <script src="/scripts/templates/load-template.js"></script>

    <style>
        body {{
            font-family: 'Noto Sans Sinhala', sans-serif;
            line-height: 1.8;
        }}
        .container {{ display: flex; justify-content: center; padding: 20px 10px; }}
        .pagewidth {{ max-width: 900px; width: 95%; }}
        .doc-header {{ text-align: center; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 2px solid rgba(56, 189, 248, 0.3); }}
        .doc-header h2 {{ margin-top: 10px; color: #38bdf8; }}
        .yt-box {{ background: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 8px; padding: 15px 20px; margin-top: 30px; text-align: center; }}
        .yt-box a {{ color: #f87171; font-weight: bold; word-break: break-all; }}
    </style>
</head>
<body>
    <div class="topnav" id="Topnavbar"></div>

    <div class="slider-container" style="text-align: center; margin-top: 20px;">
        <label for="fontSizeSlider">Font size: <small>අ</small> </label>
        <input type="range" id="fontSizeSlider" min="12" max="48" value="16">
        <span style="font-size: 2em;"> අ</span>
    </div>

    <div id="content" class="container">
        <div class="pagewidth">
            <div class="doc-header">
                <p style="font-weight: bold; font-size: 1.2em; color: #fbbf24;">නමෝ තස්ස භගවතෝ අරහතෝ සම්මා සම්බුද්ධස්ස.... !!!</p>
                <h2>{title}</h2>
            </div>
{content}
        </div>
    </div>
    <script>
        const fontSizeSlider = document.getElementById('fontSizeSlider');
        const textContent = document.getElementById('content');
        fontSizeSlider.addEventListener('input', function () {{
            const newFontSize = `${{fontSizeSlider.value}}px`;
            textContent.style.fontSize = newFontSize;
        }});
    </script>
</body>
</html>"""

pdf_files = glob.glob('current/KalutaraBodhiyaM/docs/M 0[1-6]*.pdf')
for pdf_file in pdf_files:
    title = os.path.basename(pdf_file).replace('.pdf', '')
    content_html = ''
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                for line in text.split('\\n'):
                    if line.strip():
                        # skip namo tassa line as it is in header
                        if 'නම ො' in line and 'තස්ස' in line:
                            continue
                        if title in line:
                            continue
                        if 'YouTube' in line or 'youtube.com' in line:
                            link = line.split()[-1]
                            if not link.startswith('http'):
                                link = 'https://www.youtube.com'
                            content_html += f'            <div class="yt-box"><p><i class="fa fa-youtube-play" style="color: #ef4444; font-size: 1.2em; margin-right: 5px;"></i> <strong>දේශනාවේ YouTube සබැඳියාව:</strong> <a href="{link}" target="_blank">{link}</a></p></div>\n'
                        else:
                            content_html += f'            <p>{line.strip()}</p>\n'
                            
    out_file = pdf_file.replace('.pdf', '.html')
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(html_template.format(title=title, content=content_html))

