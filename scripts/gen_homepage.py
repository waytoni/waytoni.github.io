import os
import re

def parse_homepage_info(filename):
    """
    Parse the homepage_info.txt file and extract section blocks and zoom blocks.
    
    Args:
        filename (str): Path to the homepage_info.txt file
        
    Returns:
        tuple: (num_section_blocks, section_blocks, num_zoom_blocks, zoom_blocks)
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return None, None, None, None
    
    # Remove comments and empty lines, and process inline comments
    processed_lines = []
    for line in lines:
        # Skip empty lines
        if not line.strip():
            continue
            
        # Skip comment lines (starting with # but not ##)
        if line.strip().startswith('#') and not line.strip().startswith('##'):
            continue
            
        # Remove inline comments (when # appears after the 4th character)
        if '#' in line[4:]:
            hash_pos = line.find('#', 4)
            if hash_pos != -1:
                line = line[:hash_pos].rstrip()
                
        processed_lines.append(line.strip())
    
    # Parse fields using state machine approach
    current_field = None
    current_content = []
    all_fields = []
    
    for line in processed_lines:
        # Check for field markers
        if line.startswith('## SECTION_HEADER'):
            # Save previous field if exists
            if current_field and current_content:
                all_fields.append((current_field, '\n'.join(current_content)))
            
            current_field = 'SECTION_HEADER'
            current_content = []
            
        elif line.startswith('## SECTION_INFO'):
            if current_field and current_content:
                all_fields.append((current_field, '\n'.join(current_content)))
            
            current_field = 'SECTION_INFO'
            current_content = []
            
        elif line.startswith('## ZOOM_HEADER'):
            if current_field and current_content:
                all_fields.append((current_field, '\n'.join(current_content)))
            
            current_field = 'ZOOM_HEADER'
            current_content = []
            
        elif line.startswith('## ZOOM_MEETINGID'):
            if current_field and current_content:
                all_fields.append((current_field, '\n'.join(current_content)))
            
            current_field = 'ZOOM_MEETINGID'
            current_content = []
            
        elif line.startswith('## ZOOM_PASSCODE'):
            if current_field and current_content:
                all_fields.append((current_field, '\n'.join(current_content)))
            
            current_field = 'ZOOM_PASSCODE'
            current_content = []
            
        elif line.startswith('## ZOOM_LINK'):
            if current_field and current_content:
                all_fields.append((current_field, '\n'.join(current_content)))
            
            current_field = 'ZOOM_LINK'
            current_content = []
            
        elif line.startswith('## ZOOM_DESCRIPTION'):
            if current_field and current_content:
                all_fields.append((current_field, '\n'.join(current_content)))
            
            current_field = 'ZOOM_DESCRIPTION'
            current_content = []
            
        elif current_field and line and not line.startswith('##'):
            # Add content to current field (only first line for single-line fields)
            if current_field in ['SECTION_HEADER', 'ZOOM_HEADER', 'ZOOM_MEETINGID', 'ZOOM_PASSCODE', 'ZOOM_LINK', 'ZOOM_DESCRIPTION']:
                if not current_content:  # Only take first line for single-line fields
                    current_content.append(line)
            else:
                current_content.append(line)
    
    # Don't forget the last field
    if current_field and current_content:
        all_fields.append((current_field, '\n'.join(current_content)))
    
    # Debug: print all parsed fields
    print("Parsed fields:")
    for field_type, content in all_fields:
        print(f"  {field_type}: {content[:50]}...")
    
    # Process section blocks
    section_blocks = []
    i = 0
    while i < len(all_fields):
        field_type, content = all_fields[i]
        if field_type == 'SECTION_HEADER':
            # Look for the next SECTION_INFO
            if i + 1 < len(all_fields) and all_fields[i + 1][0] == 'SECTION_INFO':
                section_blocks.append({
                    'section_header': content.strip(),
                    'section_info': all_fields[i + 1][1].strip()
                })
                i += 2  # Skip both header and info
            else:
                i += 1
        else:
            i += 1
    
    num_section_blocks = len(section_blocks)
    
    # Process zoom blocks
    zoom_blocks = []
    i = 0
    zoom_field_sequence = ['ZOOM_HEADER', 'ZOOM_MEETINGID', 'ZOOM_PASSCODE', 'ZOOM_LINK', 'ZOOM_DESCRIPTION']
    
    while i < len(all_fields):
        field_type, content = all_fields[i]
        if field_type == 'ZOOM_HEADER':
            # Check if we have a complete zoom block
            zoom_block = {}
            complete_block = True
            
            for j, expected_field in enumerate(zoom_field_sequence):
                if i + j >= len(all_fields) or all_fields[i + j][0] != expected_field:
                    complete_block = False
                    break
                zoom_block[expected_field.lower().replace('zoom_', '')] = all_fields[i + j][1].strip()
            
            if complete_block:
                zoom_blocks.append({
                    'zoom_header': zoom_block['header'],
                    'zoom_meetingID': zoom_block['meetingid'],
                    'zoom_passcode': zoom_block['passcode'],
                    'zoom_url': zoom_block['link'],
                    'zoom_desc': zoom_block['description']
                })
                i += len(zoom_field_sequence)  # Skip all zoom fields
            else:
                print(f"Error: Incomplete zoom block starting at position {i}")
                return None, None, None, None
        else:
            i += 1
    
    num_zoom_blocks = len(zoom_blocks)
    
    # Validate we have complete zoom blocks
    if not zoom_blocks:
        print("Error: No complete zoom blocks found")
        return None, None, None, None
    
    return num_section_blocks, section_blocks, num_zoom_blocks, zoom_blocks

def generate_homepage():
    """
    Main function to generate the homepage by parsing info and replacing template placeholders.
    """
    # Define file paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    info_file = os.path.join(base_dir, 'Homepage', 'homepage_info.txt')
    template_file = os.path.join('scripts', 'templates/homepage_template.html')
    navigation_file = os.path.join(os.path.dirname(__file__), 'navigation_header.html')
    navigation_file = 'scripts/py/navigation_header.html'  # Adjusted path
    messages_file = os.path.join(base_dir, 'Homepage', 'messages_new.html')
    output_file = os.path.join(base_dir, 'index.html')
    
    # Parse homepage_info.txt
    print("Parsing homepage_info.txt...")
    num_section_blocks, section_blocks, num_zoom_blocks, zoom_blocks = parse_homepage_info(info_file)
    
    if section_blocks is None or zoom_blocks is None:
        print("Error parsing homepage_info.txt. Exiting.")
        return
    
    print(f"Found {num_section_blocks} section blocks and {num_zoom_blocks} zoom blocks.")
    
    # Read template
    try:
        with open(template_file, 'r', encoding='utf-8') as file:
            template_content = file.read()
    except FileNotFoundError:
        print(f"Error: Template file {template_file} not found.")
        return
    
    # Replace navigation header
    try:
        with open(navigation_file, 'r', encoding='utf-8') as file:
            navigation_content = file.read()
        template_content = template_content.replace('$NAVIGATION_HEADER$', navigation_content)
        print("Successfully replaced navigation header")
    except FileNotFoundError:
        print(f"Error: Navigation file {navigation_file} not found.")
        return
    
    # Replace notice box content
    try:
        with open(messages_file, 'r', encoding='utf-8') as file:
            messages_content = file.read()
        template_content = template_content.replace('$NOTICE_BOX_CONTENT$', messages_content)
        print("Successfully replaced notice box content")
    except FileNotFoundError:
        print(f"Error: Messages file {messages_file} not found.")
        return
    
    # Generate section cards
    cards_html = ""
    for block in section_blocks:
        card_html = f"""
            <div class="card">
                <div class="card-header">{block['section_header']}</div>
                <div class="card-body">
                    <ul>
                        {block['section_info']}
                    </ul>
                </div>
            </div>"""
        cards_html += card_html + "\n"
    
    template_content = template_content.replace('$CURRENT_SERIES_CARDS$', cards_html.strip())
    print("Successfully generated section cards")
    
    # Generate zoom blocks
    zoom_html = ""
    for block in zoom_blocks:
        zoom_block_html = f"""
            <h3>{block['zoom_header']}</h3>
            <ul>
                <li><strong>Meeting ID:</strong> {block['zoom_meetingID']}</li>
                <li><strong>Passcode:</strong> {block['zoom_passcode']} </li>
                <li><a href="{block['zoom_url']}"> {block['zoom_desc']}</a></li>
            </ul>"""
        zoom_html += zoom_block_html + "\n"
    
    template_content = template_content.replace('$ZOOM_INFO_BLOCK$', zoom_html.strip())
    print("Successfully generated zoom blocks")
    
    # Write output file
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(template_content)
        print(f"Successfully generated {output_file}")
    except Exception as e:
        print(f"Error writing output file: {e}")

if __name__ == "__main__":
    generate_homepage()