import os
import re
from datetime import datetime, timedelta
import json

# Configuration - Update these variables as needed
SERIES_NAME = "AbhidharmaAruth/D_series"  # Name of the series folder
HTML_FILE_NAME = "AAD_new.html"  # Output HTML file name
JSON_FILE_NAME = "AbhidharmaAruth_D.json"  # JSON file name
CSS_FILE = "series_page_style_green.css"  # CSS file to use
ON_GOING = True  # Set to False if the series is completed

# Paths
ROOT_DIR = "."  # Update if script is in different location
SCRIPTS_DIR = os.path.join(ROOT_DIR, "scripts/py")
SERIES_DIR = os.path.join(ROOT_DIR, SERIES_NAME)
CSS_DIR = os.path.join(ROOT_DIR, "css")
ZOOM_INFO_DIR = os.path.join(ROOT_DIR, "Zoom_Info")

def read_file(file_path):
    """Read file content or return None if file doesn't exist"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

def write_file(file_path, content):
    """Write content to file"""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def is_zoom_info_recent(zoom_info_file):
    """Check if ZoomInfo date is recent (future or less than 5 days in the past)"""
    # Extract date from filename (format: ZoomInfo_YYMMDD.txt)
    match = re.search(r'ZoomInfo_(\d{6})\.txt', zoom_info_file)
    if not match:
        return False
    
    date_str = match.group(1)
    try:
        # Parse date (assuming YYMMDD format)
        zoom_date = datetime.strptime(date_str, '%y%m%d')
        current_date = datetime.now()
        
        # Check if date is in future or within last 5 days
        return zoom_date >= current_date - timedelta(days=5)
    except ValueError:
        return False

def get_last_entry_index(series_dir, data_length):
    """Determine the last entry index based on ON_GOING status and current_entry.txt"""
    if not ON_GOING:
        return "0"
    
    current_entry_file = os.path.join(series_dir, "current_entry.txt")
    current_entry_content = read_file(current_entry_file)
    
    if current_entry_content is None:
        return "data[data.length - 1]"
    
    try:
        current_entry = int(current_entry_content)
        last_entry = max(0, current_entry - 1)
        return str(last_entry)
    except ValueError:
        print(f"Warning: Non-numeric content in current_entry.txt. Using last entry.")
        return "data[data.length - 1]"

def generate_series_page():
    """Main function to generate the series HTML page"""
    
    # Read template
    template_path = os.path.join(SCRIPTS_DIR, "series_page_template.html")
    template_content = read_file(template_path)
    if template_content is None:
        print(f"Error: Template file not found at {template_path}")
        return False
    
    # 1. Replace CSS file
    template_content = template_content.replace("$CSSFLE$", CSS_FILE)
    
    # 2. Replace title
    title_file = os.path.join(SERIES_DIR, "title.txt")
    title_content = read_file(title_file)
    if title_content is None:
        print(f"Error: title.txt not found in {SERIES_DIR}")
        return False
    template_content = template_content.replace("$TITLE$", title_content)
    
    # 3. Replace navigation header
    nav_header_file = os.path.join(SCRIPTS_DIR, "navigation_header.html")
    nav_header_content = read_file(nav_header_file)
    if nav_header_content is None:
        print(f"Error: navigation_header.html not found at {nav_header_file}")
        return False
    template_content = template_content.replace("$NAVIGATION_HEADER$", nav_header_content)
    
    # 4. Replace intro
    intro_file = os.path.join(SERIES_DIR, "intro.txt")
    intro_content = read_file(intro_file)
    if intro_content is None:
        print(f"Error: intro.txt not found in {SERIES_DIR}")
        return False
    template_content = template_content.replace("$INTRO$", intro_content)
    
    # 5. Handle location
    location_file = os.path.join(SERIES_DIR, "location.txt")
    location_content = read_file(location_file)
    if location_content is None:
        if ON_GOING:
            print(f"Warning: location.txt not found in {SERIES_DIR}")
        # Remove location card
        location_pattern = r'<div class="info-card">\s*<h3><i class="fa fa-map-marker"></i> ස්ථානය</h3>\s*<p>\$LOCATION\$</p>\s*</div>'
        template_content = re.sub(location_pattern, '', template_content)
    else:
        template_content = template_content.replace("$LOCATION$", location_content)
    
    # 6. Handle time
    time_file = os.path.join(SERIES_DIR, "time.txt")
    time_content = read_file(time_file)
    if not ON_GOING or time_content is None:
        if ON_GOING and time_content is None:
            print(f"Warning: time.txt not found in {SERIES_DIR}")
        # Remove time card
        time_pattern = r'<div class="info-card">\s*<h3><i class="fa fa-clock-o"></i> කාලය</h3>\s*<p>\$TIME\$</p>\s*</div>'
        template_content = re.sub(time_pattern, '', template_content)
    else:
        template_content = template_content.replace("$TIME$", time_content)
    
    # 7. Handle contact
    contact_file = os.path.join(SERIES_DIR, "contact.txt")
    contact_content = read_file(contact_file)
    if not ON_GOING or contact_content is None:
        if ON_GOING and contact_content is None:
            print(f"Warning: contact.txt not found in {SERIES_DIR}")
        # Remove contact card
        contact_pattern = r'<div class="info-card">\s*<h3><i class="fa fa-phone"></i> විමසීම්</h3>\s*<p>\$CONTACT\$</p>\s*</div>'
        template_content = re.sub(contact_pattern, '', template_content)
    else:
        template_content = template_content.replace("$CONTACT$", contact_content)
    
    # 8. Handle Zoom info
    zoom_info_content = None
    
    if ON_GOING:
        # Check for recent ZoomInfo date file
        zoom_info_files = [f for f in os.listdir(SERIES_DIR) if f.startswith("ZoomInfo_") and f.endswith(".txt")]
        recent_zoom_file = None
        
        for zoom_file in zoom_info_files:
            if is_zoom_info_recent(zoom_file):
                recent_zoom_file = zoom_file
                break
        
        if recent_zoom_file:
            zoom_info_content = read_file(os.path.join(SERIES_DIR, recent_zoom_file))
            print(f"Using recent Zoom info from {recent_zoom_file}")
        else:
            # Use basic Zoom info
            zoom_basic_file = os.path.join(ZOOM_INFO_DIR, "ZoomInfo_basic.html")
            zoom_info_content = read_file(zoom_basic_file)
            if zoom_info_content is None:
                print(f"Warning: ZoomInfo_basic.html not found at {zoom_basic_file}")
            else:
                print("Using basic Zoom info")
    
    if not ON_GOING or zoom_info_content is None:
        # Remove Zoom info box
        zoom_pattern = r'<div class="info-box">\s*\$ZOOM_INFO\$\s*</div>'
        template_content = re.sub(zoom_pattern, '', template_content)
        if ON_GOING:
            print("Warning: No Zoom info available - removing Zoom info section")
    else:
        template_content = template_content.replace("$ZOOM_INFO$", zoom_info_content)
    
    # 9. Replace JSON file
    template_content = template_content.replace("$JSON_FILE$", JSON_FILE_NAME)
    
    # 10. Determine last entry
    json_data_file = os.path.join(SERIES_DIR, JSON_FILE_NAME)
    data_length = 0
    if os.path.exists(json_data_file):
        try:
            with open(json_data_file, 'r', encoding='utf-8') as file:
                json_data = json.load(file)
                data_length = len(json_data)
        except (json.JSONDecodeError, Exception) as e:
            print(f"Warning: Could not read JSON file {json_data_file}: {e}")
            data_length = 0
    
    last_entry = get_last_entry_index(SERIES_DIR, data_length)
    template_content = template_content.replace("$LASTENTRY$", last_entry)
    
    # 11. Replace series title
    series_title_file = os.path.join(SERIES_DIR, "seriestitle.txt")
    series_title_content = read_file(series_title_file)
    if series_title_content is None:
        # Use title as fallback
        series_title_content = title_content
        print(f"Using title.txt content for series title (seriestitle.txt not found)")
    template_content = template_content.replace("$SERIESTITLE$", series_title_content)
    
    # Write the final HTML file
    output_file = os.path.join(SERIES_DIR, HTML_FILE_NAME)
    write_file(output_file, template_content)
    
    print(f"Successfully generated {output_file}")
    return True

if __name__ == "__main__":
    # Create necessary directories if they don't exist
    os.makedirs(SERIES_DIR, exist_ok=True)
    
    print(f"Generating series page with configuration:")
    print(f"  Series Name: {SERIES_NAME}")
    print(f"  HTML File: {HTML_FILE_NAME}")
    print(f"  JSON File: {JSON_FILE_NAME}")
    print(f"  CSS File: {CSS_FILE}")
    print(f"  Ongoing: {ON_GOING}")
    print("-" * 50)
    
    if generate_series_page():
        print("Series page generation completed successfully!")
    else:
        print("Series page generation failed!")