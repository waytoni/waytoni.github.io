import os
import glob

        
# Read template
with open('scripts/templates/SutraPathrika_template.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace navigation header
with open('scripts/templates/navigation_header_template.html', 'r', encoding='utf-8') as f:
    nav_header = f.read()
content = content.replace('$NAVIGATION_HEADER$', nav_header)

# Generate PDF list with hyperlinks
pdf_files = sorted(glob.glob('documents/SutraPDFs/*.pdf'))
pdf_list = '\n'.join(
    f'<li><a href="/documents/SutraPDFs/{os.path.basename(pdf)}">{os.path.basename(pdf)}</a></li>'
    for pdf in pdf_files
)
content = content.replace('$SUTRA_PDFS$', pdf_list)

# Write output
with open('documents/SutraPathrika.html', 'w', encoding='utf-8') as f:
    f.write(content)