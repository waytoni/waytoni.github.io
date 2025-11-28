# gen_series.py
import os
import sys

# Add the scripts directory to the path so we can import the helper modules
sys.path.append('scripts')

from generate_series_page_helper import generate_series_page
from gen_json_file import BuildDropDownMenuWithNavigation

# Configuration variables
ON_GOING = True  # Set to True if series is ongoing, False if completed
DEBUG_INFO = False  # Set to True for debugging, False for production

# Define file paths

def gen_series(verbose_flag=False):
    try:
        # Generate the series page HTML
        ytlink_file, notes_file = generate_series_page(
            base_folder, html_file, json_file, css_file, ON_GOING, DEBUG_INFO, verbose=verbose_flag
        )
        
        # Generate the JSON file with video links and notes
        json_file_full_path = os.path.join(base_folder,  json_file)
        BuildDropDownMenuWithNavigation(ytlink_file, notes_file, json_file_full_path, verbose=verbose_flag)
        
        print(f"Successfully generated {html_file} and {json_file} in {base_folder}/")
        
    except Exception as e:
        print(f"Error: {e}")
        if DEBUG_INFO:
            print("Check the log file for detailed error information.")
        sys.exit(1)


    
# RuwanweliMahaSeya
base_folder = "VisheshaDesana/RuwanweliMahaSeya"  # Replace with your series folder name
html_file = "RuwanweliMahaSeya.html"  # Output HTML file name
css_file = "series_page_style_green.css"  # CSS file to use
json_file = "RuwanweliMahaSeya.json"  # Output JSON file name

gen_series()

# L_series
base_folder = "KalutaraBodhiya/L_series"  # Replace with your series folder name
html_file = "L_series.html"  # Output HTML file name
css_file = "series_page_style_green.css"  # CSS file to use
json_file = "L_series.json"  # Output JSON file name

gen_series()

# AbhidharmaAruthD
base_folder = "AbhidharmaAruth/D_series"  # Replace with your series folder name
html_file = "AbhidharmaAruthD.html"  # Output HTML file name
css_file = "series_page_style_green.css"  # CSS file to use
json_file = "AbhidharmaAruthD.json"  # Output JSON file name
gen_series()

# ThalawathugodaB
base_folder = "NivanMagaUdesaDesana/ThalawathugodaB/"  # Replace with your series folder name
html_file = "ThalawathugodaB.html"  # Output HTML file name
css_file = "series_page_style_green.css"  # CSS file to use
json_file = "ThalawathugodaB.json"  # Output JSON file name
gen_series()

# MaharagamaA
base_folder = "NivanMagaUdesaDesana/MaharagamaA"  # Replace with your series folder name
html_file = "MaharagamaA.html"  # Output HTML file name
css_file = "series_page_style_green.css"  # CSS file to use
json_file = "MaharagamaA.json"  # Output JSON file name
gen_series()