import os
import glob
import re

dirs = [
    r"e:\src\github\waytoni_io\waytoni_desktop\waytoni.github.io\current\HomagamaA\docs",
    r"e:\src\github\waytoni_io\waytoni_desktop\waytoni.github.io\current\KalutaraBodhiyaM\docs",
]

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
            }
"""

for docs_dir in dirs:
    html_files = sorted(glob.glob(os.path.join(docs_dir, "*.html")))
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

        if "</style>" in content_new:
            content_new = content_new.replace("</style>", css_addition + "        </style>", 1)
        else:
            skipped.append((name, "no </style> tag"))
            continue

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content_new)
        updated.append(name)

    print(f"[{os.path.basename(os.path.dirname(docs_dir))}] Updated: {len(updated)}, Skipped: {len(skipped)}")
