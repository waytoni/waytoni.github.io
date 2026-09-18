import glob
import os
import pypdf

# Locate script directory so it converts PDF files in the directory it resides in (or works relative to it)
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
        .page-block {{
            margin-bottom: 30px;
        }}
        .page-num {{
            font-weight: bold;
            color: #2e7d32;
            background: #e8f5e9;
            padding: 4px 10px;
            border-radius: 4px;
            display: inline-block;
            margin-bottom: 12px;
        }}
        p {{
            margin-bottom: 12px;
            text-align: justify;
            white-space: pre-wrap;
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
    <div class="container">
        <h1>{title}</h1>
        {content}
    </div>
</body>
</html>"""

created_files = []
for pdf in pdf_files:
    base_name = os.path.splitext(os.path.basename(pdf))[0]
    html_path = os.path.join(script_dir, base_name + '.html')
    
    reader = pypdf.PdfReader(pdf)
    content_blocks = []
    
    for idx, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ''
        # Escape basic HTML special chars
        safe_text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        block = f'<div class="page-block">\n<span class="page-num">පිටුව {idx}</span>\n<p>{safe_text}</p>\n</div>'
        content_blocks.append(block)
    
    full_content = '\n'.join(content_blocks)
    html_out = template.format(title=base_name, content=full_content)
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_out)
    created_files.append(html_path)

print(f'Successfully generated {len(created_files)} HTML files.')
