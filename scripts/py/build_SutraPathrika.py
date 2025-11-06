import os
import re
from utilities import *
from build_series_menu import *

pdf_folder = 'documents/pdfs'
output_file = 'documents/SutraPathrika.html'

series_title = 'සූත්‍ර පැහැදිලි කිරීමට භාවිතා කරන ලද පත්‍රිකා'

Sutra_styles = """
   	<style>
        body {
            font-family: Arial, sans-serif;
            margin: 0px;
            line-height: 1.6;
        }
        h1 {
            color: #333;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin: 10px 10px;
            padding: 8px;
            background-color: #f9f9f9;
            border-left: 4px solid #007acc;
        }
        a {
            text-decoration: none;
            color: #007acc;
            font-weight: bold;
        }
        a:hover {
            color: #005a9e;
            text-decoration: underline;
        }
        .count {
            margin-bottom: 20px;
            color: #666;
        }
	</style>
"""

PrepareHeadTop(output_file, series_title, Sutra_styles)

def find_pdfs_with_sinhala_phrases():
    
    # Sinhala phrases to search for
    phrases = ['සුත්තං', 'සූත්‍ර']
    
    # Create a regex pattern to match filenames containing any of the phrases
    # Using re.escape to handle special characters and joining with | for OR condition
    pattern = '|'.join(re.escape(phrase) for phrase in phrases)
    
    # List to store matching PDF files
    matching_pdfs = []
    
    # Check if the PDF folder exists
    if not os.path.exists(pdf_folder):
        print(f"Error: Folder '{pdf_folder}' does not exist.")
        return
    
    # Scan through all files in the PDF folder
    for filename in os.listdir(pdf_folder):
        if filename.lower().endswith('.pdf'):
            # Check if the filename contains any of the Sinhala phrases
            if re.search(pattern, filename):
                matching_pdfs.append(filename)
    
    # Create the HTML file
    with open(output_file, 'a', encoding='utf-8') as html_file:
        # Write HTML header
        html_file.write('''<!DOCTYPE html>
<html lang="si">

    <h1>සූත්‍ර පැහැදිලි කිරීමට භාවිතා කරන ලද පත්‍රිකා</h1>
''')
        
        # Write the count of matching files
        html_file.write(f'    <div class="count">Found {len(matching_pdfs)} PDF file(s)</div>\n')
        
        # Write the list of PDF files as hyperlinks
        if matching_pdfs:
            html_file.write('    <ul>\n')
            for pdf_file in sorted(matching_pdfs):
                # Create relative path for the hyperlink
                file_path = f'pdfs/{pdf_file}'
                html_file.write(f'        <li><a href="{file_path}" target="_blank">{pdf_file}</a></li>\n')
            html_file.write('    </ul>\n')
        else:
            html_file.write('    <p>No matching PDF files found.</p>\n')
        
        # Write HTML footer
        html_file.write('''</body>
</html>''')
    
    print(f"HTML file created successfully: {output_file}")
    print(f"Found {len(matching_pdfs)} matching PDF file(s)")

if __name__ == "__main__":
    find_pdfs_with_sinhala_phrases()