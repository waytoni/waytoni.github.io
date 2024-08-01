import json
import re

# Define a dictionary to map keywords to html tags
keyword_dict = {
    "pdf": "<a href=\"{}\"  target=\"_blank\">{}</a>",
    "img": "<img src=\"docs/{}\" width=95%>",
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

def parse_notes(file_path):
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
                    intro_text = parts[0].strip()
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
                            new_string += " " + html_tag
                        else:
                            # If the keyword is not a valid keyword, append a space and the original pair of parts to the new string
                            new_string += " " + keyword + "::" + text_related_to_keyword
                else:
                    # If there is only one part, use it as the new string
                    new_string = parts[0]
                # Print the new string
                print(new_string)
                current_notes.append(new_string)
                
        if current_index is not None:
            notes[current_index] = "\n".join(current_notes)
    return notes




def BuildDropDownMenuWithNavigation(utlinks_file, notes_file, json_file):

    utlinks = parse_utlinks(utlinks_file)
    notes = parse_notes(notes_file)


    for utlink in utlinks:
        utlink['notes'] = notes.get(utlink['index'], "")

    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(utlinks, file, indent=4, ensure_ascii=False)

    print(f"Data processing complete. {json_file} file has been created.")
