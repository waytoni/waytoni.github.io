import os
import re
import html
from datetime import datetime

def parse_info_file(info_file_path):
    """Parse the info.txt file and extract sermon data"""
    sermons = []
    
    with open(info_file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    current_sermon = {}
    current_field = None
    field_value = []
    
    for line_num, line in enumerate(lines, 1):
        line = line.rstrip('\n')  # Keep trailing spaces for now
        original_line = line
        
        # Skip comment lines (starting with '# ')
        if line.startswith('# '):
            continue
            
        # Skip empty lines
        if not line.strip():
            continue
            
        # Check for new card
        if line == '## CARDINFO':
            if current_sermon:
                # Save previous field if exists
                if current_field and field_value:
                    # Handle multiple youtube_links by making them a list
                    if current_field == 'youtube_link' and 'youtube_link' in current_sermon:
                        if isinstance(current_sermon['youtube_link'], list):
                            current_sermon['youtube_link'].append('\n'.join(field_value).strip())
                        else:
                            # Convert existing single link to list
                            current_sermon['youtube_link'] = [current_sermon['youtube_link'], '\n'.join(field_value).strip()]
                    else:
                        current_sermon[current_field] = '\n'.join(field_value).strip()
                sermons.append(current_sermon)
            current_sermon = {}
            current_field = None
            field_value = []
            continue
            
        # Check for field markers
        if line.startswith('## '):
            # Save previous field if exists
            if current_field and field_value:
                # Handle multiple youtube_links by making them a list
                if current_field == 'youtube_link' and 'youtube_link' in current_sermon:
                    if isinstance(current_sermon['youtube_link'], list):
                        current_sermon['youtube_link'].append('\n'.join(field_value).strip())
                    else:
                        # Convert existing single link to list
                        current_sermon['youtube_link'] = [current_sermon['youtube_link'], '\n'.join(field_value).strip()]
                else:
                    current_sermon[current_field] = '\n'.join(field_value).strip()
            
            # Parse new field
            field_parts = line.split(' ', 2)
            field_name = field_parts[1] if len(field_parts) > 1 else ''
            
            # Handle field name variations
            if field_name == 'DATE':
                current_field = 'date'
            elif field_name == 'TITLE':
                current_field = 'title'
            elif field_name == 'YOUTUBE_LINK':
                current_field = 'youtube_link'
            elif field_name in ['NOTES_DESCRIPTION', 'NOTESDESCRIPTION']:
                # Handle multiple notes sections by numbering them
                if 'notes_description' in current_sermon:
                    # This is a second notes description
                    notes_count = 1
                    while f'notes_description_{notes_count}' in current_sermon:
                        notes_count += 1
                    current_field = f'notes_description_{notes_count}'
                else:
                    current_field = 'notes_description'
            elif field_name in ['NOTES_LOCATION', 'NOTESLOCATION']:
                # Handle multiple notes locations by numbering them
                if 'notes_location' in current_sermon:
                    # This is a second notes location
                    notes_count = 1
                    while f'notes_location_{notes_count}' in current_sermon:
                        notes_count += 1
                    current_field = f'notes_location_{notes_count}'
                else:
                    current_field = 'notes_location'
            elif field_name == 'ZOOMINFO':
                current_field = 'zoominfo'
            else:
                current_field = None
            
            field_value = []
            # Extract value if it's on the same line
            if len(field_parts) > 2:
                field_value.append(field_parts[2].strip())
        elif current_field:
            # Continue adding to current field
            field_value.append(line.strip())
    
    # Don't forget the last sermon
    if current_sermon:
        if current_field and field_value:
            # Handle multiple youtube_links by making them a list
            if current_field == 'youtube_link' and 'youtube_link' in current_sermon:
                if isinstance(current_sermon['youtube_link'], list):
                    current_sermon['youtube_link'].append('\n'.join(field_value).strip())
                else:
                    # Convert existing single link to list
                    current_sermon['youtube_link'] = [current_sermon['youtube_link'], '\n'.join(field_value).strip()]
            else:
                current_sermon[current_field] = '\n'.join(field_value).strip()
        sermons.append(current_sermon)
    
    # Debug output
    print(f"DEBUG: Found {len(sermons)} sermons")
    for i, sermon in enumerate(sermons):
        print(f"DEBUG: Sermon {i+1}:")
        for key, value in sermon.items():
            if key == 'youtube_link' and isinstance(value, list):
                print(f"  {key}: {len(value)} video(s)")
                for j, link in enumerate(value):
                    print(f"    Video {j+1}: {link[:50]}..." if len(link) > 50 else f"    Video {j+1}: {link}")
            elif isinstance(value, str) and len(value) > 50:
                print(f"  {key}: {value[:50]}...")
            else:
                print(f"  {key}: {value}")
    
    # Sort by date (newest first)
    sermons.sort(key=lambda x: x.get('date', ''), reverse=True)
    
    return sermons

def read_template_file(template_file_path):
    """Read the HTML template file"""
    with open(template_file_path, 'r', encoding='utf-8') as f:
        return f.read()

def read_navigation_file(nav_file_path):
    """Read the navigation header template"""
    with open(nav_file_path, 'r', encoding='utf-8') as f:
        return f.read()

def is_valid_youtube_url(url):
    """Check if the URL is a valid YouTube URL"""
    if not url:
        return False
    
    # Check for valid YouTube patterns
    youtube_patterns = [
        r'^https?://(www\.)?youtube\.com/embed/[a-zA-Z0-9_-]+',
        r'^https?://(www\.)?youtube\.com/watch\?v=[a-zA-Z0-9_-]+',
        r'^https?://youtu\.be/[a-zA-Z0-9_-]+',
        r'^https?://(www\.)?youtube\.com/v/[a-zA-Z0-9_-]+'
    ]
    
    for pattern in youtube_patterns:
        if re.match(pattern, url):
            return True
    
    return False

def extract_youtube_id(url):
    """Extract YouTube video ID from URL"""
    patterns = [
        r'youtube\.com/embed/([a-zA-Z0-9_-]+)',
        r'youtube\.com/watch\?v=([a-zA-Z0-9_-]+)',
        r'youtu\.be/([a-zA-Z0-9_-]+)',
        r'youtube\.com/v/([a-zA-Z0-9_-]+)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    return None

def process_youtube_content(youtube_content, video_title_prefix=""):
    """Process YouTube content and return HTML for videos or messages"""
    html_content = ""
    
    # Handle single string or list of strings
    if isinstance(youtube_content, str):
        youtube_items = [youtube_content]
    elif isinstance(youtube_content, list):
        youtube_items = youtube_content
    else:
        return ""
    
    for i, item in enumerate(youtube_items):
        item = item.strip()
        if not item:
            continue
            
        if is_valid_youtube_url(item):
            youtube_id = extract_youtube_id(item)
            if youtube_id:
                # Add video number to title if multiple videos
                title_suffix = f" - Video {i+1}" if len(youtube_items) > 1 else ""
                video_title = f"{video_title_prefix}{title_suffix}" if video_title_prefix else f"Video {i+1}"
                
                html_content += f'''
                        <div class="video-container" style="margin-top: {'1rem' if i > 0 else '0'}">
                            <iframe src="https://www.youtube.com/embed/{youtube_id}"
                                title="{html.escape(video_title)}"
                                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                                allowfullscreen>
                            </iframe>
                        </div>'''
        elif item.startswith('https://'):
            # Extract message text from invalid YouTube link
            # Remove "https://" and replace underscores with spaces
            message_text = item[8:].replace('_', ' ')
            if message_text:
                html_content += f'''
                        <div class="resources" style="margin-top: {'1rem' if i > 0 else '0'}">
                            <h3>{'නිවේදන' if i > 0 else 'නිවේදනයක්'}:</h3>
                            <div style="padding: 1rem; background: #e8f4ff; border-radius: 5px; border-left: 4px solid #2d8cff; color: #000;">
                                {html.escape(message_text)}
                            </div>
                        </div>'''
    
    return html_content

def generate_card_html(sermon, card_number):
    """Generate HTML for a single sermon card"""
    card_id = f"card{card_number}"
    
    # Get and clean date
    date_str = sermon.get('date', '')
    
    # Clean up title - remove date prefix if present
    title = sermon.get('title', '')
    
    # Fix common title issues
    if title.startswith('025-12-03'):
        title = title.replace('025-12-03', '').strip()
    elif date_str and title.startswith(date_str):
        title = title.replace(date_str, '').strip()
    
    # Get YouTube content (could be string or list)
    youtube_content = sermon.get('youtube_link', '')
    
    # Generate video title prefix
    video_title_prefix = f"{title} - {date_str}" if date_str else title
    
    # Build the card HTML
    card_html = f'''
            <!-- Card {card_number} -->
            <div class="card">
                <span class="date-badge">{date_str}</span>
                <h2>
                    <button class="card-link collapsed" onclick="toggleCard('{card_id}', this)">
                        {title}
                    </button>
                </h2>
                <div id="{card_id}" class="collapse-content">
                    <div class="card-content">'''
    
    # Add video or message content
    if youtube_content:
        youtube_html = process_youtube_content(youtube_content, video_title_prefix)
        if youtube_html:
            card_html += youtube_html
    
    # Collect all notes descriptions and locations
    notes_data = []
    
    # Find all notes_description fields (including numbered ones)
    notes_desc_fields = []
    notes_loc_fields = []
    
    for key in sermon.keys():
        if key.startswith('notes_description'):
            notes_desc_fields.append(key)
        elif key.startswith('notes_location'):
            notes_loc_fields.append(key)
    
    # Sort fields to match them in order
    notes_desc_fields.sort()
    notes_loc_fields.sort()
    
    # Match descriptions with locations
    for i in range(max(len(notes_desc_fields), len(notes_loc_fields))):
        desc_key = notes_desc_fields[i] if i < len(notes_desc_fields) else None
        loc_key = notes_loc_fields[i] if i < len(notes_loc_fields) else None
        
        desc = sermon.get(desc_key, '') if desc_key else ''
        loc = sermon.get(loc_key, '') if loc_key else ''
        
        if desc or loc:
            notes_data.append({
                'description': desc,
                'location': loc
            })
    
    # Generate resources section if there are notes
    if notes_data:
        card_html += '''
                        
                        <div class="resources">
                            <h3>දේශනා සඳහා සටහන් / පත්‍රිකා :</h3>'''
        
        for i, note in enumerate(notes_data):
            desc = note['description'].strip()
            loc = note['location'].strip()
            
            if loc and loc.lower() not in ['none', '']:
                # Has location - create hyperlink
                link_text = desc if desc else "දේශනා සඳහා සටහන් / පත්‍රිකා:"
                card_html += f'''
                            <a href="{loc}" 
                               target="_blank" 
                               class="resource-link">
                                {html.escape(link_text)}
                            </a>'''
            elif desc:
                # Has description but no location - show as text
                card_html += f'''
                            <div style="padding: 0.8rem; margin: 0.3rem 0; background: #f0f0f0; border-radius: 5px; border-left: 3px solid #ccc;">
                                {html.escape(desc)}
                            </div>'''
        
        # Add Zoom info if available
        zoominfo = sermon.get('zoominfo', '')
        
        if zoominfo and zoominfo.lower() not in ['none', '']:
            # Extract Zoom link and details
            zoom_link = ''
            zoom_id = ''
            passcode = ''
            
            # Look for Zoom link
            zoom_link_match = re.search(r'https://[^\s]+', zoominfo)
            if zoom_link_match:
                zoom_link = zoom_link_match.group(0)
            
            # Look for Zoom ID
            zoom_id_match = re.search(r'Zoom ID:\s*(\d[\d\s]+\d)', zoominfo, re.IGNORECASE)
            if zoom_id_match:
                zoom_id = zoom_id_match.group(1).replace(' ', '')
            
            # Look for passcode
            passcode_match = re.search(r'Passcode:\s*(\S+)', zoominfo, re.IGNORECASE)
            if passcode_match:
                passcode = passcode_match.group(1)
            
            if zoom_link or zoom_id:
                card_html += f'''
                            <h3 style="margin-top: 15px;">Zoom සම්බන්ධතා:</h3>'''
                
                if zoom_link:
                    card_html += f'''
                            <a href="{zoom_link}" 
                               target="_blank" 
                               class="resource-link" style="background: #2d8cff;">
                                Zoom සම්බන්ධ වීමට
                            </a>'''
                
                if zoom_id:
                    card_html += f'''
                            <div class="zoom-info">
                                <strong>Zoom ID:</strong> {zoom_id}<br>'''
                    
                    if passcode:
                        card_html += f'''<strong>Passcode:</strong> {passcode}'''
                    
                    card_html += '''
                            </div>'''
        
        card_html += '''
                        </div>'''
    
    card_html += '''
                    </div>
                </div>
            </div>'''
    
    return card_html

def generate_html_file(template_path, nav_path, info_path, output_path):
    """Generate the complete HTML file"""
    print(f"Reading template from: {template_path}")
    print(f"Reading navigation from: {nav_path}")
    print(f"Reading sermon info from: {info_path}")
    
    # Read all necessary files
    template = read_template_file(template_path)
    navigation = read_navigation_file(nav_path)
    sermons = parse_info_file(info_path)
    
    print(f"Found {len(sermons)} sermons")
    
    if not sermons:
        print("ERROR: No sermons found in info file!")
        return False
    
    # Replace navigation in template - handle the placeholder
    if '$NAVIGATION_HEADER$' in template:
        template = template.replace('$NAVIGATION_HEADER$', navigation)
        print("Navigation replaced (using placeholder)")
    else:
        # Try to find and replace the navigation section
        nav_start = template.find('<div class="topnav" id="Topnavbar">')
        if nav_start != -1:
            nav_end = template.find('</div>', nav_start) + 6
            if nav_end > nav_start:
                template = template[:nav_start] + navigation + template[nav_end:]
                print("Navigation replaced (found and replaced section)")
            else:
                print("WARNING: Could not properly locate navigation section end")
        else:
            print("WARNING: Could not find navigation section in template")
    
    # Generate cards HTML
    cards_html = ''
    for i, sermon in enumerate(sermons, 1):
        print(f"\nGenerating card {i}...")
        cards_html += generate_card_html(sermon, i)
    
    # Find and replace the cards container
    container_pattern = r'<div class="card-container" id="sermons-container">'
    container_start = template.find(container_pattern)
    
    if container_start == -1:
        print("ERROR: Could not find sermons container in template!")
        return False
    
    # Find the matching closing div
    search_pos = container_start + len(container_pattern)
    div_count = 1
    container_end = -1
    
    while search_pos < len(template) and div_count > 0:
        next_div = template.find('<div', search_pos)
        next_close = template.find('</div>', search_pos)
        
        # Handle case where neither is found
        if next_div == -1 and next_close == -1:
            break
        
        # Determine which comes first
        if next_div == -1 or (next_close != -1 and next_close < next_div):
            # Closing div comes first
            search_pos = next_close + 6
            div_count -= 1
            if div_count == 0:
                container_end = next_close + 6
                break
        else:
            # Opening div comes first
            search_pos = next_div + 4
            div_count += 1
    
    if container_end == -1:
        print("ERROR: Could not find matching closing div for sermons container!")
        return False
    
    # Create the new container content
    new_container = f'''        <div class="card-container" id="sermons-container">
{cards_html}
        </div>'''
    
    # Replace the old container with the new one
    template = template[:container_start] + new_container + template[container_end:]
    
    print("Cards container replaced successfully")
    
    # Write the output file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(template)
    
    print(f"\nGenerated HTML file: {output_path}")
    print(f"Total sermons processed: {len(sermons)}")
    
    return True

def main():
    # Define file paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Script is in scripts folder
    templates_dir = os.path.join(script_dir, 'templates')
    root_dir = os.path.dirname(script_dir)  # Go up one level to project root
    vishesha_dir = os.path.join(root_dir, 'VisheshaDesana')
    
    template_path = os.path.join(templates_dir, 'vi_template.html')
    nav_path = os.path.join(templates_dir, 'navigation_header_template.html')
    info_path = os.path.join(vishesha_dir, 'vishesha_desana_info.txt')
    output_path = os.path.join(vishesha_dir, 'index.html')
    
    print(f"Script directory: {script_dir}")
    print(f"Templates directory: {templates_dir}")
    print(f"Root directory: {root_dir}")
    print(f"Vishesha directory: {vishesha_dir}")
    
    # Check if files exist
    for path, desc in [(template_path, 'template'), 
                       (nav_path, 'navigation template'), 
                       (info_path, 'info file')]:
        if not os.path.exists(path):
            print(f"Error: {desc} not found: {path}")
            return False
        else:
            print(f"Found {desc}: {path}")
    
    # Generate the HTML file
    success = generate_html_file(template_path, nav_path, info_path, output_path)
    
    if not success:
        print("Failed to generate HTML file!")
        return False
    
    # Also create a backup of the original complete file if it exists
    # complete_path = os.path.join(vishesha_dir, 'vi_complete.html')
    # if os.path.exists(complete_path):
    #     backup_path = os.path.join(vishesha_dir, f'vi_complete_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.html')
    #     import shutil
    #     shutil.copy2(complete_path, backup_path)
    #     print(f"Backup created: {backup_path}")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        import sys
        sys.exit(1)