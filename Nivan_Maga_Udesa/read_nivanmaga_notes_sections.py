  

import re

KEYWORDS = ['pdf', 'PDF', 'img', 'IMG', 'url', 'URL']

# Define a dictionary to map keywords to html tags
keyword_dict = {
    "pdf": "<a href='docs/{}'>{}</a>",
    "img": "<img src='docs/{}'>",
    "url": "<a href='{}'>{}</a>",
    "PDF": "<a href='docs/{}'>{}</a>",
    "IMG": "<img src='docs/{}'>",
    "URL": "<a href='{}'>{}</a>"
}

# Define a regular expression pattern to match any of the keywords followed by ::
pattern = r"(pdf|PDF|img|IMG|url|URL)::"

def create_hyperlink(url):
    return f'<a href="{url}">{url}</a>'

def construct_new_string(intro_text, keyword, text_related_to_keyword):
  if keyword in ['pdf', 'PDF']:
    new_string = f'{intro_text} <a href="docs/{text_related_to_keyword}">{text_related_to_keyword}</a>'
  elif keyword in ['img', 'IMG']:
    new_string = f'{intro_text} <img src="docs/{text_related_to_keyword}">'
  elif keyword in ['url', 'URL']:
    new_string = f'{intro_text} <a href="{text_related_to_keyword}">{text_related_to_keyword}</a>'
  else:
    new_string = f'{intro_text} {text_related_to_keyword}'

  return new_string


def read_sections(filename):
    sections = {}  # Dictionary to store sections

    with open(filename, 'r', encoding="utf-8") as file:
        current_section = None

        for line in file:
            line = line.strip()

            if line.startswith('#'):
                current_section = int(line[1:])  # Extract the number after '#'
                sections[current_section] = []  # Initialize the section list
            elif current_section is not None:
                line = line.strip()
                
                # Split the line by the pattern
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
                
                
                # Search for URLs in the line and create hyperlinks
                urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
                for url in urls:
                    line = line.replace(url, create_hyperlink(url))
                    
                sections[current_section].append(new_string)  # Add modified line to the current section

    return sections


# filename = 'Nivan_Maga_Udesa/Nivan_Maga_Udesa_notes.txt'  
filename = "Nivan_Maga_Udesa/search_keywords.txt"
sections = read_sections(filename)

section_number = 3  # Replace with the desired section number

if section_number in sections:
    lines = sections[section_number]
    print(f"Lines in Section {section_number}:")
    for line in lines:
        print(line)
else:
    print(f"Section {section_number} not found.")
