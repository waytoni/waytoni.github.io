  

import re

def create_hyperlink(url):
    return f'<a href="{url}">{url}</a>'

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
                # Search for URLs in the line and create hyperlinks
                urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
                for url in urls:
                    line = line.replace(url, create_hyperlink(url))
                sections[current_section].append(line)  # Add modified line to the current section

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
