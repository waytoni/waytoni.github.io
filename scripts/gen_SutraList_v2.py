import os
import glob

template_file = 'scripts/templates/SutraPathrika_template.html'
        
# Read template
try:
    with open(template_file, 'r', encoding='utf-8') as f:
        template_content = f.read()
except FileNotFoundError:
    print(f"Error: Template file {template_file} not found.")
    exit(1)

# Replace navigation header
with open('scripts/templates/navigation_header_template.html', 'r', encoding='utf-8') as f:
    nav_header = f.read()
content = template_content.replace('$NAVIGATION_HEADER$', nav_header)

# Generate PDF list with hyperlinks from local PDFs
pdf_files = sorted(glob.glob('documents/SutraPDFs/*.pdf'))
pdf_list_items = [
    f'<li><a href="/documents/SutraPDFs/{os.path.basename(pdf)}">{os.path.basename(pdf)}</a></li>'
    for pdf in pdf_files
]

# Read and add shared PDF links from SharedPDFs.html
shared_pdfs_file = 'documents/SutraPDFs/SharedPDFs.html'
if os.path.exists(shared_pdfs_file):
    with open(shared_pdfs_file, 'r', encoding='utf-8') as f:
        shared_content = f.read()
    
    # Parse the shared content to extract links
    # Assuming each link is in a separate <a> tag
    # We'll wrap each link in <li> tags
    import re
    # Find all anchor tags
    anchor_tags = re.findall(r'<a\s+[^>]*href="[^"]+"[^>]*>.*?</a>', shared_content, re.DOTALL)
    
    for anchor in anchor_tags:
        # Clean up the anchor tag and wrap in li
        cleaned_anchor = anchor.strip()
        if cleaned_anchor:
            pdf_list_items.append(f'<li>{cleaned_anchor}</li>')

# Combine all items
pdf_list = '\n'.join(pdf_list_items)

content = content.replace('$SUTRA_PDFS$', pdf_list)

# Write output
with open('documents/SutraPathrika.html', 'w', encoding='utf-8') as f:
    f.write(content)