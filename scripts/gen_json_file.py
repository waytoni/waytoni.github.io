import json
import re
from datetime import datetime

# Define a dictionary to map keywords to html tags
keyword_dict = {
    "pdf": "<a href=\"{}\"  target=\"_blank\">{}</a>",
    "img": "<img src=\"{}\" width=95%>",
    "url": "<a href=\"{}\" target=\"_blank\" >{}</a>",
    "PDF": "<a href='\"docs/{}\"  target=\"_blank\">{}</a>",
    "IMG": "<img src=\"docs/{}\" width=95%>",
    "URL": "<a href=\"{}\">{}</a>"
}

# Pattern to match any of the keywords 
pattern = r"(pdf|PDF|img|IMG|url|URL)::"
def parse_utlinks(file_path):
    utlinks = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Use a regular expression to match the line structure with optional comments
            match = re.match(r'(\d+)\s+(.*?)\s*(https?://\S+)?\s+(\d{4}-[A-Za-z]{3}-\d{2})', line.strip())
            # print (match)
            if match:
                index, comment, url, date = match.groups()
                if url:  # Ignore lines without a URL
                    if not comment.strip() or comment.startswith("http"):
                        comment = ""
                    utlinks.append({
                        'index': int(index),
                        'comment': comment,
                        'url': url,
                        'date': date
                    })
    return utlinks

def parse_ytlinks(file_path):
    utlinks = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, 1):
            line = line.strip()
            if not line or line.startswith('#'):  # Skip empty lines and comments
                continue
                
            # Improved regex to handle various date formats and optional fields
            match = re.match(r'(\d+)\s+(.*?)\s*(https?://\S+)?\s+([\d\-A-Za-z]{8,})', line)
            
            if match:
                index, comment, url, date_str = match.groups()
                
                if not url:  # Skip lines without URL
                    continue
                    
                # Clean up comment field
                if not comment.strip() or comment.startswith("http"):
                    comment = ""
                
                # Parse date with multiple format support
                parsed_date = parse_flexible_date(date_str)
                
                utlinks.append({
                    'index': int(index),
                    'comment': comment.strip(),
                    'url': url,
                    'date': parsed_date,
                    'date_string': date_str,  # Keep original string for reference
                    'line_number': line_num   # For error tracking
                })
            else:
                print(f"Warning: Could not parse line {line_num}: {line}")
    
    return utlinks

def parse_flexible_date(date_str):
    """Parse dates in various formats including:
    - 2024-May-23
    - 2024-09-10
    - 10-05-2024
    - 24-05-11
    - 2024/May/23
    """
    date_formats = [
        '%Y-%b-%d',    # 2024-May-23
        '%Y-%B-%d',    # 2024-May-23 (full month name)
        '%Y-%m-%d',    # 2024-09-10
        '%d-%m-%Y',    # 10-05-2024
        '%y-%m-%d',    # 24-05-11
        '%m-%d-%Y',    # 05-23-2024
        '%Y/%b/%d',    # 2024/May/23
        '%Y/%B/%d',    # 2024/May/23 (full month name)
    ]
    
    # Try each format
    for fmt in date_formats:
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    
    # If none work, try to handle month names case-insensitively
    for fmt in ['%Y-%b-%d', '%Y-%B-%d', '%Y/%b/%d', '%Y/%B/%d']:
        try:
            # Convert to title case for month names (Mar, Apr, etc.)
            parts = re.split(r'[-/]', date_str)
            if len(parts) == 3:
                month_part = parts[1]
                if month_part.isalpha():
                    normalized_date = f"{parts[0]}-{month_part.title()}-{parts[2]}"
                    separator = '-' if '-' in date_str else '/'
                    normalized_date = normalized_date.replace('-', separator)
                    return datetime.strptime(normalized_date, fmt).date()
        except (ValueError, IndexError):
            continue
    
    print(f"Warning: Could not parse date: {date_str}")
    return None




def parse_notes(file_path, verbose=False):
    notes = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        current_index = None
        current_notes = []
        for line in file:
            line = line.strip()
            if line.startswith('#'):
                if current_index is not None:
                    notes[current_index] = "\n".join(current_notes)
                current_index = int(line[1:])
                current_notes = []
            else:
                #current_notes.append(line)
                
                parts = re.split(pattern, line)
                
                # Check if there are more than one part
                if len(parts) > 1:
                    # Get the intro text as the first element of the list
                    intro_text = "<p>" + parts[0].strip()
                    # Initialize an empty string for the new string
                    new_string = intro_text
                    # Loop through the rest of the parts in pairs of keyword and text related to keyword
                    for i in range(1, len(parts), 2):
                        # Get the keyword and the text related to keyword
                        keyword = parts[i].strip()
                        text_related_to_keyword = parts[i+1].strip()
                        # Check if the keyword is a valid keyword
                        if keyword in keyword_dict:
                            # Get the html tag for the keyword
                            html_tag = keyword_dict[keyword]
                            # Format the html tag with the text related to keyword
                            html_tag = html_tag.format(text_related_to_keyword, text_related_to_keyword)
                            # Append a space and the html tag to the new string
                            new_string += " " + html_tag + "</p>"
                        else:
                            # If the keyword is not a valid keyword, append a space and the original pair of parts to the new string
                            new_string += " " + keyword + "::" + text_related_to_keyword + "</p>"
                else:
                    # If there is only one part, use it as the new string
                    new_string = "<p>" + parts[0] + "</p>"
                # Print the new string
                if verbose:
                    print(new_string)
                current_notes.append(new_string)
                
        if current_index is not None:
            notes[current_index] = "\n".join(current_notes)
    return notes




def BuildDropDownMenuWithNavigation(utlinks_file, notes_file, json_file, verbose=False):

    utlinks = parse_ytlinks(utlinks_file)
    notes = parse_notes(notes_file, verbose=verbose)

    #print(utlinks)
    for utlink in utlinks:
        utlink['notes'] = notes.get(utlink['index'], "")

    for item in utlinks:
        if item['date']:
            item['date'] = item['date'].isoformat()

    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(utlinks, file, indent=4, ensure_ascii=False)

    print(f"Data processing complete. {json_file} file has been created.")
