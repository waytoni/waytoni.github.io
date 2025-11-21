# generate_series_page_helper.py
import os
import re
import datetime
import logging

def parse_info_file(info_file, on_going, debug_info):
    """
    Parse the info file and extract various sections.
    
    Args:
        info_file (str): Path to the info file
        on_going (bool): Whether the series is ongoing
        debug_info (bool): Whether to log debug information
    
    Returns:
        tuple: (intro_section, title_section, series_title_section, time_section, 
                location_section, contact_section, zoom_section, video_number)
    """
    
    sections = {
        'INTRO': '',
        'TITLE': '',
        'SERIES_TITLE': '',
        'TIME': '',
        'LOCATION': '',
        'CONTACT': '',
        'ZOOM_INFO': '',
        'VIDEO_SELECTOR': ''
    }
    
    current_section = None
    section_content = []
    
    try:
        with open(info_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        if debug_info:
            logging.error(f"Error reading info file {info_file}: {e}")
        raise
    
    for line in lines:
        line = line.rstrip('\n\r')
        
        # Skip comment lines and empty lines
        if line.strip().startswith('#') and not line.strip().startswith('##'):
            continue
        if not line.strip():
            continue
        
        # Check for section headers
        section_match = re.match(r'^##\s*([A-Z_]+)\s*#*', line)
        if section_match:
            # Save previous section content
            if current_section and section_content:
                sections[current_section] = '\n'.join(section_content).strip()
            
            # Start new section
            current_section = section_match.group(1)
            section_content = []
        elif current_section:
            section_content.append(line)
    
    # Save the last section
    if current_section and section_content:
        sections[current_section] = '\n'.join(section_content).strip()
    
    # Validate required sections
    missing_sections = []
    if not sections['INTRO']:
        missing_sections.append('INTRO')
    if not sections['TITLE']:
        missing_sections.append('TITLE')
    
    if missing_sections:
        error_msg = f"Missing required sections in {info_file}: {', '.join(missing_sections)}"
        if debug_info:
            logging.error(error_msg)
        raise ValueError(error_msg)
    
    # Validate ongoing series requirements
    if on_going and not sections['TIME']:
        error_msg = f"TIME section is required for ongoing series in {info_file}"
        if debug_info:
            logging.error(error_msg)
        raise ValueError(error_msg)
    
    # Set series title to title if not provided
    if not sections['SERIES_TITLE']:
        sections['SERIES_TITLE'] = sections['TITLE']
    
    # Process ZOOM_INFO section
    zoom_file = "ZoomInfo_basic.html"
    if sections['ZOOM_INFO']:
        zoom_lines = sections['ZOOM_INFO'].strip().split('\n')
        if len(zoom_lines) == 2:
            date_str = zoom_lines[0].strip()
            zoom_filename = zoom_lines[1].strip()
            
            # Validate date format
            try:
                zoom_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
                current_date = datetime.datetime.now().date()
                
                # Check if date is within 5 days
                if (zoom_date - current_date).days >= -5:
                    # Check if zoom file exists
                    zoom_file_path = os.path.join('Zoom_Info', zoom_filename)
                    if os.path.exists(zoom_file_path):
                        zoom_file = zoom_filename
                    else:
                        if debug_info:
                            logging.warning(f"Zoom file {zoom_file_path} not found")
                        sections['ZOOM_INFO'] = ""
                else:
                    sections['ZOOM_INFO'] = ""
                    
            except ValueError:
                if debug_info:
                    logging.warning(f"Invalid date format in ZOOM_INFO: {date_str}")
                sections['ZOOM_INFO'] = ""
        else:
            if debug_info:
                logging.warning("ZOOM_INFO section should have exactly 2 lines")
            sections['ZOOM_INFO'] = ""
    
    # Process VIDEO_SELECTOR section
    video_number = None
    if sections['VIDEO_SELECTOR']:
        try:
            video_number = int(sections['VIDEO_SELECTOR'].strip())
        except ValueError:
            if debug_info:
                logging.warning(f"Invalid video number: {sections['VIDEO_SELECTOR']}")
            video_number = None
    
    return (sections['INTRO'], sections['TITLE'], sections['SERIES_TITLE'],
            sections['TIME'], sections['LOCATION'], sections['CONTACT'],
            zoom_file, video_number)

def generate_series_page(base_folder, html_file, json_file, css_file, on_going, debug_info, verbose=False):
    """
    Generate the series page HTML file.
    
    Args:
        base_folder (str): Folder containing series files
        html_file (str): Output HTML file name
        json_file (str): Output JSON file name
        css_file (str): CSS file to use
        on_going (bool): Whether series is ongoing
        debug_info (bool): Whether to log debug information
    
    Returns:
        tuple: (ytlink_file, notes_file) paths
    """
    
    if verbose:
        print(f"Generating series page in {base_folder}...")   
    
    
    # Setup logging if debug_info is True
    if debug_info:
        log_filename = f"log_{datetime.datetime.now().strftime('%y%m%d_%H%M%S')}.txt"
        logging.basicConfig(filename=log_filename, level=logging.DEBUG,
                          format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Check if base folder exists
    if not os.path.exists(base_folder):
        error_msg = f"Base folder does not exist: {base_folder}"
        if debug_info:
            logging.error(error_msg)
        raise FileNotFoundError(error_msg)
    
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
    
    # Parse info file
    intro_section, title_section, series_title_section, time_section, \
    location_section, contact_section, zoom_file, video_number = parse_info_file(
        info_file, on_going, debug_info)
    
    # Process video number
    if video_number is None:
        video_number = num_entries
    elif video_number > num_entries:
        video_number = num_entries
    elif video_number <= 0:
        video_number = 1
    
    if verbose:
        print(f"{base_folder}: Video number set to: {video_number}")
    
      
    # Read template
    template_path = os.path.join('scripts', 'series_page_template.html')
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()
    except Exception as e:
        if debug_info:
            logging.error(f"Error reading template {template_path}: {e}")
        raise
    
    # Read navigation header
    nav_header_path = os.path.join('scripts/py', 'navigation_header.html')
    try:
        with open(nav_header_path, 'r', encoding='utf-8') as f:
            nav_header_content = f.read()
    except Exception as e:
        if debug_info:
            logging.error(f"Error reading navigation header {nav_header_path}: {e}")
        raise
    
    # Replace CSS file
    template_content = template_content.replace('$CSSFILE$', css_file)
    
    # Replace title
    template_content = template_content.replace('$TITLE$', title_section)
    
    # Replace navigation header
    template_content = template_content.replace('$NAVIGATION_HEADER$', nav_header_content)
    
    # Replace intro section
    template_content = template_content.replace('$INTRO_SECTION$', intro_section)
    
    # Replace time block
    if on_going and time_section:
        time_block = f'''
            <div class="info-card">
                <h3><i class="fa fa-clock-o"></i> කාලය</h3>
                <p>{time_section}</p>
            </div>'''
        template_content = template_content.replace('$TIME_BLOCK$', time_block)
    else:
        template_content = template_content.replace('$TIME_BLOCK$', '')
    
    # Replace location block
    if location_section:
        location_block = f'''
            <div class="info-card">
                <h3><i class="fa fa-map-marker"></i> ස්ථානය</h3>
                <p>{location_section}</p>
            </div>'''
        template_content = template_content.replace('$LOCATION_BLOCK$', location_block)
    else:
        template_content = template_content.replace('$LOCATION_BLOCK$', '')
    
    # Replace contact block
    if contact_section:
        contact_block = f'''
            <div class="info-card">
                <h3><i class="fa fa-phone"></i> විමසීම්</h3>
                <p>{contact_section}</p>
            </div>'''
        template_content = template_content.replace('$CONTACT_BLOCK$', contact_block)
    else:
        template_content = template_content.replace('$CONTACT_BLOCK$', '')
    
    # Replace zoom info block
    if on_going:
        try:
            zoom_file_path = os.path.join('Zoom_Info', zoom_file)
            with open(zoom_file_path, 'r', encoding='utf-8') as f:
                zoom_content = f.read()
            first_newline_index = zoom_content.find('\n')
            zoom_content = zoom_content[first_newline_index+1:].strip()
            
            if verbose:
                print(zoom_content)
        #     zoom_block = f'''
        # <div class="info-box">
        #     {zoom_content}
        # </div>'''
            zoom_block = f'''
            <div class="info-card">
                <h3><i class="fa fa-video-camera"></i> Zoom සජීවීව සම්බන්ධ වීමට</h3>
                <p>{zoom_content}</p>
            </div>'''

            template_content = template_content.replace('$ZOOM_INFO_BLOCK$', zoom_block)
        except Exception as e:
            if debug_info:
                logging.warning(f"Error reading zoom file {zoom_file_path}: {e}")
            template_content = template_content.replace('$ZOOM_INFO_BLOCK$', '')
    else:
        template_content = template_content.replace('$ZOOM_INFO_BLOCK$', '')
    
    # Replace JSON file
    template_content = template_content.replace('$JSON_FILE$', json_file)
    
    # Replace video number (in the JavaScript section)
    template_content = template_content.replace('$LASTENTRY$', f'data[{video_number-1}]')
    
    # Replace series title
    template_content = template_content.replace('$SERIESTITLE$', series_title_section)
    
    #print(f"ZZZZZ Writing HTML file to {base_folder}...{debug_info}")
    # Write HTML file if not in debug mode
    if not debug_info:
        html_file_path = os.path.join(base_folder, html_file)
        # print(f"XXXXXX Writing HTML file to {html_file_path}...")
        try:
            with open(html_file_path, 'w', encoding='utf-8') as f:
                f.write(template_content)
        except Exception as e:
            if debug_info:
                logging.error(f"Error writing HTML file {html_file_path}: {e}")
            raise
    
    print(f'HTML file creation complete: {base_folder}: Generated {html_file} successfully. Video number: {video_number}')
    return ytlink_file, notes_file