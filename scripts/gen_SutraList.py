import os
import glob
import re
import unicodedata

template_file = 'scripts/templates/SutraPathrika_template.html'

def normalize_sinhala(text):
    """Normalize Sinhala text for better sorting"""
    # Normalize to NFC form (canonical decomposition followed by canonical composition)
    normalized = unicodedata.normalize('NFC', text)
    return normalized

def extract_link_text(html):
    """Extract text from HTML link for sorting"""
    # Remove HTML tags and get just the text
    text = re.sub(r'<[^>]+>', '', html)
    # Remove common prefixes if present
    text = text.strip()
    return text

def sort_sinhala_key(item):
    """Create a sorting key for Sinhala text"""
    # Extract the text part from the HTML
    text = extract_link_text(item)
    # Normalize the text for consistent sorting
    return normalize_sinhala(text)

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
    anchor_tags = re.findall(r'<a\s+[^>]*href="[^"]+"[^>]*>.*?</a>', shared_content, re.DOTALL)
    
    for anchor in anchor_tags:
        # Clean up the anchor tag and wrap in li
        cleaned_anchor = anchor.strip()
        if cleaned_anchor:
            pdf_list_items.append(f'<li>{cleaned_anchor}</li>')

# Sort all items by Sinhala text
pdf_list_items.sort(key=sort_sinhala_key)

# Combine all items
pdf_list = '\n'.join(pdf_list_items)

content = content.replace('$SUTRA_PDFS$', pdf_list)

# Write output
with open('documents/SutraPathrika.html', 'w', encoding='utf-8') as f:
    f.write(content)