# gen_series.py
import os
import sys

# Add the scripts directory to the path so we can import the helper modules
sys.path.append('scripts')

from generate_series_page_helper import generate_series_page
from gen_json_file import BuildDropDownMenuWithNavigation

# Configuration variables
ON_GOING = True  # Set to True if series is ongoing, False if completed
DEBUG_INFO = False # Set to True for debugging, False for production

# Define file paths

def gen_series():
    try:
        # Generate the series page HTML
        ytlink_file, notes_file, series_title_section = generate_series_page(
            base_folder, html_file, json_file, css_file, ON_GOING, DEBUG_INFO
        )
        
        # Generate the JSON file with video links and notes
        json_file_full_path = os.path.join(base_folder,  json_file)
        BuildDropDownMenuWithNavigation(ytlink_file, notes_file, json_file_full_path, 
                                        series_title_section, verbose=DEBUG_INFO)
        
        print(f"Successfully generated {html_file} and {json_file} in {base_folder}/")
        
    except Exception as e:
        print(f"Error: {e}")
        if DEBUG_INFO:
            print("Check the log file for detailed error information.")
        sys.exit(1)


# ThalawathugodaB
base_folder = "NivanMagaUdesaDesana/ThalawathugodaB/"  # Replace with your series folder name
html_file = "ThalawathugodaB.html"  # Output HTML file name
css_file = "series_page_style_green.css"  # CSS file to use
json_file = "ThalawathugodaB.json"  # Output JSON file name
gen_series()
