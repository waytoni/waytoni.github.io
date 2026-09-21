import glob
import os
import fitz  # PyMuPDF
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
import io

# Locate script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
pdf_files = sorted(glob.glob(os.path.join(script_dir, '*.pdf')))

template = """<!DOCTYPE html>
<html lang="si">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>{title}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Sinhala:wght@300;400;600&display=swap" rel="stylesheet">
    
    <link rel="stylesheet" type="text/css" href="/css/nav_menu.css">
    <link rel="stylesheet" type="text/css" href="/css/series_page_style_green.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <script src="/scripts/nav_function.js"></script>
    <script src="/scripts/templates/load-template.js"></script>
    <style>
        body {{
            font-family: 'Noto Sans Sinhala', sans-serif;
            line-height: 1.8;
            color: #333;
            background-color: #f9f9f9;
            margin: 0;
            padding: 20px;
        }}
        .container {{
            max-width: 900px;
            margin: 0 auto;
            background: #ffffff;
            padding: 30px 40px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #1b5e20;
            font-size: 1.6rem;
            text-align: center;
            border-bottom: 2px solid #e0e0e0;
            padding-bottom: 15px;
            margin-bottom: 25px;
            word-wrap: break-word;
        }}
        .content-body {{
            margin-bottom: 30px;
        }}
        p {{
            margin-bottom: 12px;
        }}
        @media (max-width: 600px) {{
            .container {{
                padding: 15px 20px;
            }}
            h1 {{
                font-size: 1.3rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="topnav" id="Topnavbar">
    <!-- Content loaded dynamically by load-template.js -->
    </div>

    <div class="container">
        <h1>{title}</h1>
        <div class="slider-container" style="text-align: center; margin-top: 20px;">
            <label for="fontSizeSlider">Font size: <small>අ</small> </label>
            <input type="range" id="fontSizeSlider" min="12" max="48" value="16">
            <span style="font-size: 2em;"> අ</span>
        </div>
        <div id="content" class="content-body">
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

created_files = []

for pdf in pdf_files:
    base_name = os.path.splitext(os.path.basename(pdf))[0]
    html_path = os.path.join(script_dir, base_name + '.html')
    
    # Skip if HTML already exists (so it only processes new PDFs)
    if os.path.exists(html_path):
        continue
        
    print(f"Processing new PDF: {pdf}")

    text_pages = []
    
    try:
        doc = fitz.open(pdf)
        for page_idx, page in enumerate(doc):
            print(f"  Scanning page {page_idx + 1}...")
            pix = page.get_pixmap(dpi=300)
            img_bytes = pix.tobytes("png")
            
            # Convert bytes to PIL Image for pytesseract
            img = Image.open(io.BytesIO(img_bytes))
            
            # Read Sinhala text from image
            text = pytesseract.image_to_string(img, lang='sin')
            
            # Escape HTML and wrap paragraphs
            paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
            safe_result = [p.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;') for p in paragraphs]
            
            if safe_result:
                page_html = "<p>" + "</p>\n            <p>".join(safe_result) + "</p>"
                text_pages.append(page_html)
        
        doc.close()
        
        # Combine pages
        full_content = '\n'.join(text_pages)
        html_out = template.format(title=base_name, content=full_content)
        
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_out)
        created_files.append(html_path)
    except Exception as e:
        print(f"Failed to process {pdf}: {e}")

print(f'Successfully generated {len(created_files)} HTML files via OCR.')
