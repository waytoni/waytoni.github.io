# gen_series.py
import os
import sys

# Add the scripts directory to the path so we can import the helper modules
sys.path.append('scripts')

from generate_series_page_helper import generateSeriesPageNew
from generate_series_page_helper import generate_series_page
from gen_json_file import BuildDropDownMenuWithNavigation

# Configuration variables
ON_GOING = True  # Set to True if series is ongoing, False if completed
DEBUG_INFO = False  # Set to True for debugging, False for production



def gen_series(template_name="series_page_template.html"):
    try:
        # Generate the series page HTML
        ytlink_file, notes_file, series_title_section = generateSeriesPageNew(
            base_folder, html_file, json_file, css_file, ON_GOING, DEBUG_INFO, template_name
        )
        
        # Generate the JSON file with video links and notes
        json_file_full_path = os.path.join(base_folder,  json_file)
        BuildDropDownMenuWithNavigation(ytlink_file, notes_file, json_file_full_path, series_title_section, verbose=DEBUG_INFO)
        
        print(f"Successfully generated {html_file} and {json_file} in {base_folder}/")
        
    except Exception as e:
        print(f"Error: {e}")
        if DEBUG_INFO:
            print("Check the log file for detailed error information.")
        sys.exit(1)

def gen_series_old(verbose_flag=False):
    try:
        # Generate the series page HTML
        ytlink_file, notes_file, series_title_section = generate_series_page(
            base_folder, html_file, json_file, css_file, ON_GOING, DEBUG_INFO, verbose=verbose_flag
        )
        
        # Generate the JSON file with video links and notes
        json_file_full_path = os.path.join(base_folder,  json_file)
        BuildDropDownMenuWithNavigation(ytlink_file, notes_file, json_file_full_path, series_title_section, verbose=DEBUG_INFO)
        
        print(f"Successfully generated {html_file} and {json_file} in {base_folder}/")
        
    except Exception as e:
        print(f"Error: {e}")
        if DEBUG_INFO:
            print("Check the log file for detailed error information.")
        sys.exit(1)


        
def gen_json_file_only(series_title_section, debug_info=False):
    # Find required files
    info_files = []
    ytlink_files = []
    notes_files = []
    
    for file in os.listdir(base_folder):
        if file.endswith('_info.txt'):
            info_files.append(file)
        elif file.endswith('_ytlinks.txt'):
            ytlink_files.append(file)
        elif file.endswith('_notes.txt'):
            notes_files.append(file)
    
        # Check for multiple files or missing files
    errors = []
    if len(info_files) != 1:
        errors.append(f"{base_folder}: Expected 1 _info.txt file, found {len(info_files)}: {info_files}")
    if len(ytlink_files) != 1:
        errors.append(f"{base_folder}: Expected 1 _ytlinks.txt file, found {len(ytlink_files)}: {ytlink_files}")
    if len(notes_files) != 1:
        errors.append(f"{base_folder}: Expected 1 _notes.txt file, found {len(notes_files)}: {notes_files}")
    
    if errors:
        error_msg = ";\n".join(errors)
        if debug_info:
            logging.error(error_msg)
        raise FileNotFoundError(error_msg)
    
    info_file = os.path.join(base_folder, info_files[0])
    ytlink_file = os.path.join(base_folder, ytlink_files[0])
    notes_file = os.path.join(base_folder, notes_files[0])
    
    # Count lines in ytlink file
    try:
        with open(ytlink_file, 'r', encoding='utf-8') as f:
            num_entries = sum(1 for line in f if line.strip())
    except Exception as e:
        if debug_info:
            logging.error(f"Error reading ytlink file {ytlink_file}: {e}")
        raise
    
    try:
        # Generate the series page HTML
        # ytlink_file, notes_file, series_title_section = generate_series_page(
        #     base_folder, html_file, json_file, css_file, ON_GOING, DEBUG_INFO, verbose=verbose_flag
        # )
        
        # Generate the JSON file with video links and notes
        json_file_full_path = os.path.join(base_folder,  json_file)
        BuildDropDownMenuWithNavigation(ytlink_file, notes_file, json_file_full_path, series_title_section, verbose=DEBUG_INFO)
        
        print(f"Successfully generated {json_file} in {base_folder}/")
        
    except Exception as e:
        print(f"Error: {e}")
        if DEBUG_INFO:
            print("Check the log file for detailed error information.")
        sys.exit(1)
    
    
# RuwanweliMahaSeya
base_folder = "VisheshaDesana/RuwanweliMahaSeya"  # Replace with your series folder name
html_file = "RuwanweliMahaSeya.html"  # Output HTML file name
css_file = "series_page_style_green_RuwanweliSaya.css"  # CSS file to use
json_file = "RuwanweliMahaSeya.json"  # Output JSON file name
gen_series(template_name='SeriesPageTemplateWithControls.html')

# L_series
base_folder = "KalutaraBodhiya/L_series"  # Replace with your series folder name
html_file = "L_series.html"  # Output HTML file name
css_file = "series_page_style_green_Kaluthara.css"  # CSS file to use
json_file = "L_series.json"  # Output JSON file name
gen_series(template_name='SeriesPageTemplateWithControls.html')

# M_series
base_folder = "KalutaraBodhiya/M_series"  # Replace with your series folder name
html_file = "M_series.html"  # Output HTML file name
css_file = "series_page_style_green_Kaluthara.css"  # CSS file to use
json_file = "M_series.json"  # Output JSON file name
gen_series(template_name='SeriesPageTemplateWithControls.html')


# M_series
base_folder = "KalutaraBodhiya/M_series"  # Replace with your series folder name
html_file = "M_series.html"  # Output HTML file name
css_file = "series_page_style_green_Kaluthara.css"  # CSS file to use
json_file = "M_series.json"  # Output JSON file name

gen_series(template_name='SeriesPageTemplateWithControls.html')


# AbhidharmaAruthE
base_folder = "AbhidharmaAruth/E_series"  # Replace with your series folder name
html_file = "AbhidharmaAruthE.html"  # Output HTML file name
css_file = "series_page_style_green.css"  # CSS file to use
json_file = "AbhidharmaAruthE.json"  # Output JSON file name
gen_series(template_name='SeriesPageTemplateWithControls.html')

# ThalawathugodaB
base_folder = "NivanMagaUdesaDesana/ThalawathugodaB/"  # Replace with your series folder name
html_file = "ThalawathugodaB.html"  # Output HTML file name
css_file = "series_page_style_green_Ganelanda.css"  # CSS file to use
json_file = "ThalawathugodaB.json"  # Output JSON file name
gen_series(template_name='SeriesPageTemplateWithControls.html')

# MaharagamaB
base_folder = "NivanMagaUdesaDesana/MaharagamaB"  # Replace with your series folder name
html_file = "MaharagamaB.html"  # Output HTML file name
css_file = "series_page_style_green.css"  # CSS file to use
json_file = "MaharagamaB.json"  # Output JSON file name
gen_series(template_name='SeriesPageTemplateWithControls.html')

# HomagamaA
base_folder = "NivanMagaUdesaDesana/HomagamaA"  # Replace with your series folder name
html_file = "HomagamaA.html"  # Output HTML file name
css_file = "series_page_style_green.css"  # CSS file to use
json_file = "HomagamaA.json"  # Output JSON file name
Homagamaga_series_title = "හෝමාගම ශ්‍රී ශාසනවර්ධනාරාම විහාරයේ ආරම්භ වෙන නිවන් මග උදෙසා දර්ශන ඥානය දේශනා මාලාව"  # Series title to use in the JSON file
# gen_json_file_only(Homagamaga_series_title)
gen_series(template_name='SeriesPageTemplateWithControls.html')

# AnuradhapuraA
base_folder = "NivanMagaUdesaDesana/AnuradhapuraA"  # Replace with your series folder name
html_file = "AnuradhapuraA.html"  # Output HTML file name
css_file = "series_page_style_green.css"  # CSS file to use
json_file = "AnuradhapuraA.json"  # Output JSON file name
gen_series(template_name='SeriesPageTemplateWithControls.html')