import os
import re
import sys
import glob

def update_file_format(file_path):
    print(f"Processing {file_path}...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        new_lines = []
        changes_made = 0
        
        for line in lines:
            # Look for lines that start with # followed immediately by numbers
            # e.g., #10 becomes ## 10
            new_line = re.sub(r'^#(\d+)', r'## \1', line)
            
            if new_line != line:
                changes_made += 1
                
            new_lines.append(new_line)
            
        if changes_made > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            print(f"  -> Updated {changes_made} section headers in {file_path}")
        else:
            print(f"  -> No changes needed in {file_path}")
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python update_notes_format.py <file_path_or_directory>")
        print("Example 1: python update_notes_format.py completed/Suthamaya/Mathugama/suthamaya_mathugama_notes.txt")
        print("Example 2: python update_notes_format.py completed/Suthamaya/Mathugama/")
        sys.exit(1)
        
    target_path = sys.argv[1]
    
    if os.path.isfile(target_path):
        if target_path.endswith('_notes.txt'):
            update_file_format(target_path)
        else:
            print(f"File {target_path} does not end with '_notes.txt'. Skipping.")
    elif os.path.isdir(target_path):
        search_pattern = os.path.join(target_path, '**', '*_notes.txt')
        files = glob.glob(search_pattern, recursive=True)
        if not files:
            print(f"No *_notes.txt files found in directory {target_path}")
        for file in files:
            update_file_format(file)
    else:
        print(f"Path not found: {target_path}")

if __name__ == '__main__':
    main()
