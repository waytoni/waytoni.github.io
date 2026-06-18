import re
import json
import sys

def main():
    try:
        with open(r'e:\src\github\waytoni_io\waytoni_desktop\waytoni.github.io\cc\MahaNidana\sutta_179.html', 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    # Next.js App Router stores state in __next_f arrays. Let's look for Sinhala text or just extract anything that looks like the Sutta paragraphs.
    # The text we are looking for is:
    # දීඝ නිකාය
    # මහා වග්ගෝ
    # 2. මහා නිදාන සුත්තං
    # 2. පසුබිමෙහි ඇති දේ ගැන වදාළ දීර්ඝ දෙසුම
    
    # Let's extract all the Sinhala text lines we can find. We might find JSON strings that contain the data.
    # Specifically, the page probably has an array of objects for the sutta content.
    
    # We can also just extract all text by parsing the self.__next_f pushes.
    
    # Another easier way is to use a web scraping library or just find the Sutta endpoint. 
    # Let's search for "මහා නිදාන සූත්‍රය" in the HTML and see where it appears.
    
    matches = re.findall(r'"([^"\\]*(?:\\.[^"\\]*)*)"', content)
    sinhala_texts = []
    for match in matches:
        # Decode unicode escapes if any
        try:
            decoded = match.encode('utf-8').decode('unicode_escape')
        except:
            decoded = match
        if any('\u0D80' <= c <= '\u0DFF' for c in decoded):
            # It's a Sinhala string
            sinhala_texts.append(decoded)
            
    # Also Next.js sometimes encodes strings in JSON or weird arrays like ["$","span",null,{"children":"..."}]
    
    with open(r'e:\src\github\waytoni_io\waytoni_desktop\waytoni.github.io\cc\MahaNidana\extracted_texts.txt', 'w', encoding='utf-8') as f:
        for t in sinhala_texts:
            f.write(t + "\n")
            
    print(f"Extracted {len(sinhala_texts)} potential Sinhala texts.")

if __name__ == "__main__":
    main()
