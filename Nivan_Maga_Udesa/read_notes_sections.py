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
                sections[current_section].append(line)  # Add line to the current section

    return sections

filename = 'Nivan_Maga_Udesa/notes.txt'  
sections = read_sections(filename)

for section_number, lines in sections.items():
    print(f"Section {section_number}:")
    for line in lines:
        print(line)
    print()

section_number = 4

if section_number in sections:
    lines = sections[section_number]
    print(f"Lines in Section {section_number}:")
    for line in lines:
        print(line)
else:
    print(f"Section {section_number} not found.")