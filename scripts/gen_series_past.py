# gen_series.py
import os
import sys

# Add the scripts directory to the path so we can import the helper modules
sys.path.append('scripts')

from generate_series_page_helper import generate_series_page
from gen_json_file import BuildDropDownMenuWithNavigation

# Configuration variables
ON_GOING = False  # Set to True if series is ongoing, False if completed
DEBUG_INFO = False  # Set to True for debugging, False for production

# Define file paths

def gen_series():
    try:
        # Generate the series page HTML
        ytlink_file, notes_file = generate_series_page(
            base_folder, html_file, json_file, css_file, ON_GOING, DEBUG_INFO
        )
        
        # Generate the JSON file with video links and notes
        json_file_full_path = os.path.join(base_folder,  json_file)
        BuildDropDownMenuWithNavigation(ytlink_file, notes_file, json_file_full_path)
        
        print(f"Successfully generated {html_file} and {json_file} in {base_folder}/")
        
    except Exception as e:
        print(f"Error: {e}")
        if DEBUG_INFO:
            print("Check the log file for detailed error information.")
        sys.exit(1)

    
# K_series
base_folder = "KalutaraBodhiya/K_series"  # Replace with your series folder name
html_file = "K_series.html"  # Output HTML file name
css_file = "series_page_style_green.css"  # CSS file to use
json_file = "K_series.json"  # Output JSON file name
gen_series()

# J_series
base_folder = "KalutaraBodhiya/J_series"  # Replace with your series folder name
html_file = "J_series.html"  # Output HTML file name
css_file = "series_page_style_green.css"  # CSS file to use
json_file = "J_series.json"  # Output JSON file name
gen_series()

# I_series
base_folder = "KalutaraBodhiya/I_series"  # Replace with your series folder name
html_file = "I_series.html"  # Output HTML file name
css_file = "series_page_style_green.css"  # CSS file to use
json_file = "I_series.json"  # Output JSON file name
gen_series()

# AbhidharmaAruthC
base_folder = "AbhidharmaAruth/C_series"  # Replace with your series folder name
html_file = "AbhidharmaAruthC.html"  # Output HTML file name
css_file = "series_page_style_green.css"  # CSS file to use
json_file = "AbhidharmaAruthC.json"  # Output JSON file name
gen_series()
    
# AbhidharmaAruthB2
base_folder = "AbhidharmaAruth/B2_series"  # Replace with your series folder name
html_file = "AbhidharmaAruthB2.html"  # Output HTML file name
css_file = "series_page_style_green.css"  # CSS file to use
json_file = "AbhidharmaAruthB2.json"  # Output JSON file name
gen_series()

# AbhidharmaAruthB1
base_folder = "AbhidharmaAruth/B1_series"  # Replace with your series folder name
html_file = "AbhidharmaAruthB1.html"  # Output HTML file name
css_file = "series_page_style_green.css"  # CSS file to use
json_file = "AbhidharmaAruthB1.json"  # Output JSON file name
gen_series()

# AbhidharmaAruthEP
base_folder = "AbhidharmaAruth/EP_series"  # Replace with your series folder name
html_file = "AbhidharmaAruthEP.html"  # Output HTML file name
css_file = "series_page_style_green.css"  # CSS file to use
json_file = "AbhidharmaAruthEP.json"  # Output JSON file name
gen_series()
    
# Thalawathugoda
base_folder = "NivanMagaUdesaDesana/Thalawathugoda/"  # Replace with your series folder name
html_file = "Thalawathugoda.html"  # Output HTML file name
css_file = "series_page_style_green.css"  # CSS file to use
json_file = "Thalawathugoda.json"  # Output JSON file name
gen_series()

# YouthForTruth
base_folder = "NivanMagaUdesaDesana/YouthForTruth"  # Replace with your series folder name
html_file = "YouthForTruth.html"  # Output HTML file name
css_file = "series_page_style_green.css"  # CSS file to use
json_file = "YouthForTruth.json"  # Output JSON file name
gen_series()