# generate_series_page_helper.py
import os
import re
import datetime
import logging

def is_valid_url(url_str):
    """Check if the string is a valid HTTP/HTTPS URL."""
    if not url_str:
        return False
    return bool(re.match(r'^https?://[^\s]+$', url_str.strip(), re.IGNORECASE))

def parse_zoom_info_file(zoom_info_file_path=None):
    """
    Parse Zoom information from ZoomInfo/ZoomInfo.txt (or current/ZoomInfo/ZoomInfo.txt).
    
    Format of ZoomInfo.txt:
      A section starts after the line '## ZoomName'.
      Lines beginning with '#' are comments.
      The first non-comment line in that section is the name of the ZoomName section (e.g. basic or special).
      The next non-comment line is evaluated as the Zoom URL.
      If it is a valid URL, it is set as zoom_url and the remaining lines become zoom_content.
      If it is NOT a valid URL, that line is included in zoom_content and zoom_url is set to empty string.
    
    Returns:
        dict: { zoom_name: (zoom_url, zoom_content), ... }
    """
    if zoom_info_file_path and os.path.exists(zoom_info_file_path):
        target_path = zoom_info_file_path
    elif os.path.exists('ZoomInfo/ZoomInfo.txt'):
        target_path = 'ZoomInfo/ZoomInfo.txt'
    elif os.path.exists('current/ZoomInfo/ZoomInfo.txt'):
        target_path = 'current/ZoomInfo/ZoomInfo.txt'
    elif os.path.exists('Zoom_Info/ZoomInfo.txt'):
        target_path = 'Zoom_Info/ZoomInfo.txt'
    else:
        return {}
    
    try:
        with open(target_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception:
        return {}
    
    sections = {}
    current_name = None
    current_lines = []
    
    def store_section(name, lines_list):
        if not name:
            return
        filtered = []
        for l in lines_list:
            l_str = l.rstrip('\r\n')
            stripped = l_str.strip()
            if stripped.startswith('#'):
                continue
            if not stripped and not filtered:
                continue
            filtered.append(l_str)
            
        while filtered and not filtered[-1].strip():
            filtered.pop()
            
        if not filtered:
            sections[name] = ("", "")
            return
            
        first_line = filtered[0].strip()
        if is_valid_url(first_line):
            zoom_url = first_line
            zoom_content = '\n'.join(filtered[1:]).strip()
        else:
            zoom_url = ""
            zoom_content = '\n'.join(filtered).strip()
            
        sections[name] = (zoom_url, zoom_content)
    
    for line in lines:
        stripped = line.strip()
        
        if re.match(r'^##\s*ZoomName\b', stripped, re.IGNORECASE):
            if current_name is not None:
                store_section(current_name, current_lines)
            current_name = None
            current_lines = []
            continue
            
        if stripped.startswith('#') and not stripped.startswith('##'):
            continue
            
        if current_name is None:
            if stripped:
                current_name = stripped
                current_lines = []
        else:
            current_lines.append(line)
            
    if current_name is not None:
        store_section(current_name, current_lines)
        
    return sections

def get_zoom_info(zoom_name, zoom_info_file_path=None):
    """
    Retrieve (zoom_url, zoom_content) for a given zoom_name.
    """
    if not zoom_name:
        return "", ""
    zoom_dict = parse_zoom_info_file(zoom_info_file_path)
    clean_name = zoom_name.strip()
    if clean_name in zoom_dict:
        return zoom_dict[clean_name]
    for k, v in zoom_dict.items():
        if k.lower() == clean_name.lower():
            return v
    return "", ""

def build_zoom_info_block(zoom_name, zoom_info_file_path=None, verbose=False):
    """
    Build HTML for ZOOM_INFO_BLOCK based on zoom_name from ZoomInfo.txt.
    """
    if not zoom_name:
        return ''
    zoom_url, zoom_content = get_zoom_info(zoom_name, zoom_info_file_path)
    if verbose:
        print(f"Zoom Name: {zoom_name}")
        print(f"Zoom URL: {zoom_url}")
        print(f"Zoom Content: {zoom_content}")
    
    if not zoom_url and not zoom_content:
        return ''
        
    if zoom_url:
        return f'''
            <div class="info-card">
                <h3><i class="fa fa-video-camera"></i><a href="{zoom_url}">Zoom සජීවීව සම්බන්ධ වීමට</a></h3>
                <p>{zoom_content}</p>
            </div>'''
    else:
        return f'''
            <div class="info-card">
                <h3><i class="fa fa-video-camera"></i>Zoom සජීවීව සම්බන්ධ වීමට</h3>
                <p>{zoom_content}</p>
            </div>'''

def parse_info_file(info_file, on_going, debug_info):
    """
    Parse the info file and extract various sections.
    
    Args:
        info_file (str): Path to the info file
        on_going (bool): Whether the series is ongoing
        debug_info (bool): Whether to log debug information
    
    Returns:
        tuple: (intro_section, title_section, series_title_section, time_section, 
                location_section, contact_section, zoom_name, video_number, extra_content)
    """
    
    sections = {
        'INTRO': '',
        'TITLE': '',
        'SERIES_TITLE': '',
        'TIME': '',
        'LOCATION': '',
        'CONTACT': '',
        'ZOOM_INFO': '',
        'VIDEO_SELECTOR': '',
        'EXTRA_CONTENT': ''
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
    zoom_name = ""
    if sections['ZOOM_INFO']:
        zoom_lines = [l.strip() for l in sections['ZOOM_INFO'].split('\n') if l.strip() and not (l.strip().startswith('#') and not l.strip().startswith('##'))]
        if zoom_lines:
            raw_name = zoom_lines[-1].strip()
            raw_name = re.sub(r'^ZoomInfo_', '', raw_name, flags=re.IGNORECASE)
            raw_name = re.sub(r'\.html$', '', raw_name, flags=re.IGNORECASE)
            zoom_name = raw_name.strip()
    
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
            zoom_name, video_number, sections['EXTRA_CONTENT'])

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
    location_section, contact_section, zoom_file, video_number, extra_content = parse_info_file(
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
    template_path = os.path.join('scripts', 'templates/series_page_template.html')
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()
    except Exception as e:
        if debug_info:
            logging.error(f"Error reading template {template_path}: {e}")
        raise
    
    # Read navigation header
    nav_header_path = os.path.join('scripts/templates', 'navigation_header_template.html')
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
    
    # Replace time block කාලය 
    if on_going and time_section:
        time_block = f'''
            <div class="info-card">
                <h3><i class="fa fa-clock-o"></i>වේලාව</h3>
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
    if on_going and zoom_file:
        try:
            zoom_block = build_zoom_info_block(zoom_file, verbose=verbose)
            template_content = template_content.replace('$ZOOM_INFO_BLOCK$', zoom_block)
        except Exception as e:
            if debug_info:
                logging.warning(f"Error processing zoom info for {zoom_file}: {e}")
            template_content = template_content.replace('$ZOOM_INFO_BLOCK$', '')
    else:
        template_content = template_content.replace('$ZOOM_INFO_BLOCK$', '')
    

    # Replace EXTRA_CONTENT block
    if extra_content:
        template_content = template_content.replace('$EXTRA_CONTENT_BLOCK$', extra_content)
    else:
        template_content = template_content.replace('$EXTRA_CONTENT_BLOCK$', '')
    
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
    
    print(f'HTML file creation complete for series {series_title_section}: {base_folder}: Generated {html_file} successfully. Video number: {video_number}')
    return ytlink_file, notes_file, series_title_section

def generateSeriesPageNew(base_folder, html_file, json_file, css_file, on_going, debug_info, template_name, verbose=False):
    """
    Generate the series page HTML file.
    
    Args:
        base_folder (str): Folder containing series files
        html_file (str): Output HTML file name
        json_file (str): Output JSON file name
        css_file (str): CSS file to use
        on_going (bool): Whether series is ongoing
        debug_info (bool): Whether to log debug information
        template_name (str): Name of the template file to use
    
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
    location_section, contact_section, zoom_file, video_number, extra_content = parse_info_file(
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
    template_path = os.path.join('scripts', 'templates', template_name)
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()
    except Exception as e:
        if debug_info:
            logging.error(f"Error reading template {template_path}: {e}")
        raise
    
    # Read navigation header
    nav_header_path = os.path.join('scripts/templates', 'navigation_header_template.html')
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
    
    # Replace time block   වේලාව    කාලය  
    if on_going and time_section:
        time_block = f'''
            <div class="info-card">
                <h3><i class="fa fa-clock-o"></i> වේලාව</h3>
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
    if on_going and zoom_file:
        try:
            zoom_block = build_zoom_info_block(zoom_file, verbose=verbose)
            template_content = template_content.replace('$ZOOM_INFO_BLOCK$', zoom_block)
        except Exception as e:
            if debug_info:
                logging.warning(f"Error processing zoom info for {zoom_file}: {e}")
            template_content = template_content.replace('$ZOOM_INFO_BLOCK$', '')
    else:
        template_content = template_content.replace('$ZOOM_INFO_BLOCK$', '')
    

    # Replace EXTRA_CONTENT block
    if extra_content:
        template_content = template_content.replace('$EXTRA_CONTENT_BLOCK$', extra_content)
    else:
        template_content = template_content.replace('$EXTRA_CONTENT_BLOCK$', '')
    
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
    
    print(f'HTML file creation complete for series {series_title_section}: {base_folder}: Generated {html_file} successfully. Video number: {video_number}')
    return ytlink_file, notes_file, series_title_section
