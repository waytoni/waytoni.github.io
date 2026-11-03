import os
import glob
import re

docs_dir = r"e:\src\github\waytoni_io\waytoni_desktop\waytoni.github.io\current\HomagamaA\docs"
html_files = sorted(glob.glob(os.path.join(docs_dir, "*.html")))

css_addition = """            .slider-container {
                position: fixed;
                bottom: 15px;
                left: 50%;
                transform: translateX(-50%);
                z-index: 20;
                background-color: #FFD700;
                padding: 5px 15px;
                border-radius: 5px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
                display: flex;
                gap: 10px;
                align-items: center;
                white-space: nowrap;
                line-height: 1.2;
            }
            .slider-container label {
                font-weight: bold;
            }
            .slider-container input[type="range"] {
                cursor: pointer;
            }
            body {
                padding-bottom: 80px;
            }"""

updated = []
skipped = []

for filepath in html_files:
    name = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if "slider-container" not in content:
        skipped.append((name, "no slider-container"))
        continue

    if "position: fixed;" in content and ".slider-container {" in content:
        skipped.append((name, "already updated"))
        continue

    content_new = content.replace(
        '<div class="slider-container" style="text-align: center; margin-top: 20px;">',
        '<div class="slider-container">',
    )

    pattern = r"(\.content-body\s*\{\s*margin-bottom:\s*30px;\s*\})"
    if re.search(pattern, content_new):
        content_new = re.sub(pattern, r"\1\n" + css_addition, content_new, count=1)
    else:
        skipped.append((name, "pattern not matched"))
        continue

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content_new)
    updated.append(name)

print(f"Updated {len(updated)} files:")
for u in updated:
    print(f"  + {u}")
print(f"Skipped {len(skipped)} files:")
for s, reason in skipped:
    print(f"  - {s} ({reason})")
