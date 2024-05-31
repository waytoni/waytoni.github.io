
import re

def parse_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    sections = re.split(r'(\d+\.)', content)
    sections = [s.strip() for s in sections if s.strip()]  # Remove empty strings and strip whitespace
    section_dict = {}
    for i in range(0, len(sections), 2):
        number = sections[i].rstrip('.')
        text = sections[i + 1]
        section_dict[int(number)] = text
    return section_dict

def wrap_lines_in_p_tags(text):
    lines = text.split('\n')
    wrapped_lines = ''.join(f'<p>{line.strip()}</p>' for line in lines if line.strip())
    return wrapped_lines

def merge_sections(a_sections, b_sections):
    all_sections = sorted(set(a_sections.keys()).union(b_sections.keys()))
    merged_content = []

    for number in all_sections:
        if number in a_sections:
            pali_heading = f'<span class="headingpali">{number}.</span>'
            pali_text = f'<div class="pali">{pali_heading} {wrap_lines_in_p_tags(a_sections[number])}</div>'
            merged_content.append(pali_text)
        if number in b_sections:
            sinh_heading = f'<span class="headingsinh">{number}.</span>'
            sinh_text = f'<div class="sinh">{sinh_heading} {wrap_lines_in_p_tags(b_sections[number])}</div>'
            merged_content.append(sinh_text)
    
    return merged_content

def main():
    a_sections = parse_file('ap6_pali.txt')
    b_sections = parse_file('ap6_new.txt')

    merged_content = merge_sections(a_sections, b_sections)
    
    with open('ap-vp6-merged.html', 'w', encoding='utf-8') as output_file:
        for line in merged_content:
            output_file.write(line + '\n')

if __name__ == "__main__":
    main()
