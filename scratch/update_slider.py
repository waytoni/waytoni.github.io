import os
import glob

docs_dir = r"e:\src\github\waytoni_io\waytoni_desktop\waytoni.github.io\current\HomagamaA\docs"
html_files = glob.glob(os.path.join(docs_dir, "*.html"))

slider_html = """        <div class="slider-container" style="text-align: center; margin-top: 20px;">
        <label for="fontSizeSlider">Font size: <small>අ</small> </label>
        <input type="range" id="fontSizeSlider" min="12" max="48" value="16">
        <span style="font-size: 2em;"> අ</span>
    </div>"""

script_html = """
    <script>
    const fontSizeSlider = document.getElementById('fontSizeSlider');
    const textContent = document.getElementById('content');

    fontSizeSlider.addEventListener('input', function () {
        const newFontSize = `${fontSizeSlider.value}px`;
        textContent.style.fontSize = newFontSize;
    });
    </script>
"""

for filepath in html_files:
    # Skip the 16th file since it already has it
    if "016" in filepath:
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    if 'id="fontSizeSlider"' in content:
        continue

    # Update content-body to have id="content"
    content = content.replace('<div class="content-body">', '<div id="content" class="content-body">')
    
    # Insert slider HTML after </h1>. To be safe, we replace id="content" line by prepending slider_html to it.
    target_div = '<div id="content" class="content-body">'
    if target_div in content:
        content = content.replace(target_div, slider_html + "\n" + target_div)
    
    # Insert script block right before </body>
    if '</body>' in content:
        content = content.replace('</body>', script_html + '</body>')

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
print("Updated all html files with the slider successfully.")
