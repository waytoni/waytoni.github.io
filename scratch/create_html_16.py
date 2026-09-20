import os
import re

pdf_name = '16 ශාසනවර්ධනාරාමය හෝමාගම මහකටුවාන දේශනා අංක 016 - 2026 09 19'
html_name = pdf_name + '.html'
template_file = '15 ශාසනවර්ධනාරාමය හෝමාගම මහකටුවාන දේශනා අංක 015 - 2026 09 12.html'

with open('current/HomagamaA/docs/' + template_file, 'r', encoding='utf-8') as f:
    template = f.read()

# Replace the title and h1
new_html = re.sub(r'<title>.*?</title>', f'<title>{pdf_name}</title>', template)
new_html = re.sub(r'<h1>.*?</h1>', f'<h1>{pdf_name}</h1>', new_html)

# Clear the content body
new_html = re.sub(r'<div class="content-body">.*?</div>', '<div class="content-body">\n        </div>', new_html, flags=re.DOTALL)

with open('current/HomagamaA/docs/' + html_name, 'w', encoding='utf-8') as f:
    f.write(new_html)
