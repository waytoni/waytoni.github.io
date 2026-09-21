import os
import glob

docs_dir = r"e:\src\github\waytoni_io\waytoni_desktop\waytoni.github.io\current\HomagamaA\docs"
html_files = glob.glob(os.path.join(docs_dir, "*.html"))

head_add = """    
    <link rel="stylesheet" type="text/css" href="/css/nav_menu.css">
    <link rel="stylesheet" type="text/css" href="/css/series_page_style_green.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <script src="/scripts/nav_function.js"></script>
    <script src="/scripts/templates/load-template.js"></script>"""

body_add = """    <div class="topnav" id="Topnavbar">
    <!-- Content loaded dynamically by load-template.js -->
    </div>
"""

for filepath in html_files:
    # Skip the 16th file since it's already modified
    if "016" in filepath:
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    if 'id="Topnavbar"' in content:
        continue

    # Insert into head
    target_head = '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Sinhala:wght@300;400;600&display=swap" rel="stylesheet">'
    if target_head in content:
        content = content.replace(target_head, target_head + "\n" + head_add)
        
    # Insert into body
    target_body = '<body>\n'
    if target_body in content:
        content = content.replace(target_body, target_body + body_add)
    else:
        # Sometimes body has attributes or no newline
        target_body = '<body>'
        if target_body in content:
            content = content.replace(target_body, target_body + "\n" + body_add)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
print("Updated all html files successfully.")
