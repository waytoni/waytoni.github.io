import re

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regular expression to find the pattern "number." followed by any text until the next number
    pattern = r'(\d+\.\s.*?)(?=\d+\.)'

    # Find all matches
    matches = re.findall(pattern, content, re.DOTALL)

    # Write matches to new file with desired format
    with open(output_file, 'w', encoding='utf-8') as f:
        last_end = 0
        for idx, match in enumerate(matches, 1):
            print('match words = ' , len(match.split()) , ' match lines =', len(match.splitlines())  ,' idx  =' , idx+346)
            start = content.find(match, last_end)
            if start > last_end:
                # Write text before numbered block in simple <p> section
                f.write(f'<p>{content[last_end:start].strip()}</p>\n')
            f.write(f'<p class="chedaya" id="id{idx + 346}">{match.strip()}</p>\n')
            last_end = start + len(match)
            print('start = ', start, ' last_end = ', last_end, ' num lines = ', len(match.splitlines()))
            
            for line in match.splitlines():
                print (line)
        # Write any remaining text after the last numbered block
        if last_end < len(content):
            f.write(f'<p>{content[last_end:].strip()}</p>\n')
        
# Example usage:
input_file = 'ap6_new.txt'
output_file = 'ap6.html'
process_file(input_file, output_file)
