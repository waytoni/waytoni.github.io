import os
import re
import shutil

def parse_siyuludesana_info(filename):
    """
    Parse the SiyuluDesana_info.txt file to extract current and past series lines.
    
    Args:
        filename (str): Path to the SiyuluDesana_info.txt file
        
    Returns:
        tuple: (num_current_lines, current_series_lines, num_past_blocks, past_series_lines)
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return 0, [], 0, []
    
    current_series_lines = []
    past_series_lines = []
    
    current_section = None  # 'current', 'past', or None
    
    for line in lines:
        # Remove leading/trailing whitespace
        line = line.strip()
        #print(line)
        # Skip empty lines
        if not line:
            continue
            
        # Skip comment lines (starting with # as the first character)
        if line.startswith('#') and not line.startswith('##'):
            continue
            
        # Check for section headers
        if line.startswith('## CURRENT'):
            current_section = 'current'
            continue
        elif line.startswith('## PAST'):
            current_section = 'past'
            continue
            
        # Remove comments after the fourth character
        if '#' in line[4:]:
            line = line.split('#', 1)[0].strip()
            
        # Skip empty lines after comment removal
        if not line:
            continue
            
        # Add to appropriate section
        if current_section == 'current':
            current_series_lines.append(line)
        elif current_section == 'past':
            past_series_lines.append(line)
    
    num_current_lines = len(current_series_lines)
    num_past_lines = len(past_series_lines)
    
    return num_current_lines, current_series_lines, num_past_lines, past_series_lines

def generate_siyuludesana_html():
    """
    Generate the SiyuluDesana.html file by parsing the info file and using the template.
    """
    # File paths
    base_dir = "All_Playlists"
    info_file = os.path.join(base_dir, "SiyaluDesana_info.txt")
    template_file = os.path.join("scripts/templates", "SiyaluDesana_template.html")
    output_file = os.path.join(base_dir, "SiyaluDesana.html")
    nav_header_file = os.path.join("scripts/py", "navigation_header.html")
    
    # Parse the info file
    num_current_lines, current_series_lines, num_past_lines, past_series_lines = parse_siyuludesana_info(info_file)
    
    print(f"Parsed {num_current_lines} current series lines and {num_past_lines} past series lines.")
    
    # Read the template
    try:
        with open(template_file, 'r', encoding='utf-8') as file:
            template_content = file.read()
    except FileNotFoundError:
        print(f"Error: Template file {template_file} not found.")
        return
    
    # Read and replace navigation header
    try:
        with open(nav_header_file, 'r', encoding='utf-8') as file:
            nav_header_content = file.read()
        template_content = template_content.replace('$NAVIGATION_HEADER$', nav_header_content)
    except FileNotFoundError:
        print(f"Error: Navigation header file {nav_header_file} not found.")
        return
    
    # Generate current series blocks
    current_blocks = []
    for line in current_series_lines:
        block = f'''        <div class="series-card" data-category="current">
            <div class="series-content">
                {line}
            </div>
        </div>'''
        current_blocks.append(block)
    
    current_series_content = '\n'.join(current_blocks)
    template_content = template_content.replace('$CURRENT_SERIES$', current_series_content)
    
    # Generate past series blocks
    past_blocks = []
    for line in past_series_lines:
        block = f'''        <div class="series-card" data-category="current">
            <div class="series-content">
                {line}
            </div>
        </div>'''
        past_blocks.append(block)
    
    past_series_content = '\n'.join(past_blocks)
    template_content = template_content.replace('$PAST_SERIES$', past_series_content)
    
    # Write the output file
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(template_content)
        print(f"Successfully generated {output_file}")
        print(f"Current series: {num_current_lines} items")
        print(f"Past series: {num_past_lines} items")
        
        old_html_file = 'All_Playlists/සියුලු_දේශනා.html'
        shutil.copy2(output_file, old_html_file, follow_symlinks=False)
        
    except Exception as e:
        print(f"Error writing output file: {e}")


    
if __name__ == "__main__":
    generate_siyuludesana_html()
    
