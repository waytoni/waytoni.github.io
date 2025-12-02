
"""
Image Splitter for Excel-like Freeze Pane Viewer
This script splits the header and body images into sections for frozen panes.
"""

from PIL import Image
import os
import argparse

def split_images(header_path, body_path, left_column_width=300, header_height=989):
    """
    Split header and body images into sections for frozen pane viewer.
    
    Args:
        header_path: Path to header image (cc_h.jpg)
        body_path: Path to body image (cc_b.jpg)
        left_column_width: Width of the frozen left column (in pixels)
        header_height: Height of the header (in pixels)
    """
    
    # Create output directory
    output_dir = "split_images"
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Splitting images with left column width: {left_column_width}px")
    print(f"Header height: {header_height}px")
    print(f"Output directory: {output_dir}")
    print("-" * 50)
    
    # Load images
    try:
        header_img = Image.open(header_path)
        body_img = Image.open(body_path)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return
    
    # Get image dimensions
    header_width, header_height_actual = header_img.size
    body_width, body_height = body_img.size
    
    print(f"Header image: {header_width}x{header_height_actual}")
    print(f"Body image: {body_width}x{body_height}")
    
    # Verify dimensions match
    if header_width != body_width:
        print(f"Warning: Header width ({header_width}) doesn't match body width ({body_width})")
    
    if header_height_actual != header_height:
        print(f"Warning: Header height is {header_height_actual}px, but using {header_height}px for splitting")
        header_height = header_height_actual
    
    # Calculate split points
    total_width = body_width
    total_height = body_height
    
    print(f"\nTotal dimensions: {total_width}x{total_height}")
    print(f"Left column: {left_column_width}px wide")
    print(f"Right part: {total_width - left_column_width}px wide")
    print(f"Header: {header_height}px tall")
    print(f"Body: {total_height - header_height}px tall")
    
    # 1. Split HEADER image (cc_h.jpg)
    print(f"\n1. Splitting HEADER image ({header_path}):")
    
    # Extract corner from header (top-left: left_column_width x header_height)
    corner_box = (0, 0, left_column_width, header_height)
    if left_column_width > 0 and left_column_width <= header_width:
        corner_img = header_img.crop(corner_box)
        corner_path = os.path.join(output_dir, "corner.jpg")
        corner_img.save(corner_path)
        print(f"   - Corner: {corner_box} -> {corner_path}")
    else:
        print(f"   - Corner: Skipped (left_column_width {left_column_width} is invalid)")
    
    # Extract right part of header (header without left column)
    header_right_box = (left_column_width, 0, header_width, header_height)
    if header_width - left_column_width > 0:
        header_right_img = header_img.crop(header_right_box)
        header_right_path = os.path.join(output_dir, "header_right.jpg")
        header_right_img.save(header_right_path)
        print(f"   - Header right: {header_right_box} -> {header_right_path}")
    else:
        print(f"   - Header right: Skipped (no width left)")
    
    # 2. Split BODY image (cc_b.jpg)
    print(f"\n2. Splitting BODY image ({body_path}):")
    
    # Extract left column from body (full height)
    left_column_full_box = (0, 0, left_column_width, body_height)
    if left_column_width > 0 and left_column_width <= body_width:
        left_column_full_img = body_img.crop(left_column_full_box)
        left_column_full_path = os.path.join(output_dir, "body_left_full.jpg")
        left_column_full_img.save(left_column_full_path)
        print(f"   - Left column (full): {left_column_full_box} -> {left_column_full_path}")
    else:
        print(f"   - Left column: Skipped (left_column_width {left_column_width} is invalid)")
    
    # Extract right part from body (full height)
    body_right_full_box = (left_column_width, 0, body_width, body_height)
    if body_width - left_column_width > 0:
        body_right_full_img = body_img.crop(body_right_full_box)
        body_right_full_path = os.path.join(output_dir, "body_right_full.jpg")
        body_right_full_img.save(body_right_full_path)
        print(f"   - Body right (full): {body_right_full_box} -> {body_right_full_path}")
    else:
        print(f"   - Body right: Skipped (no width left)")
    
    # 3. Further split body sections (remove header)
    print(f"\n3. Creating final sections (excluding header):")
    
    # Left column (body part only - excluding header)
    left_column_body_box = (0, header_height, left_column_width, body_height)
    if left_column_width > 0 and left_column_width <= body_width and body_height > header_height:
        left_column_body_img = body_img.crop(left_column_body_box)
        left_column_body_path = os.path.join(output_dir, "body_left.jpg")
        left_column_body_img.save(left_column_body_path)
        print(f"   - Left column (body only): {left_column_body_box} -> {left_column_body_path}")
        
        # Also create left column header for completeness
        left_column_header_box = (0, 0, left_column_width, header_height)
        left_column_header_img = body_img.crop(left_column_header_box)
        left_column_header_path = os.path.join(output_dir, "body_left_header.jpg")
        left_column_header_img.save(left_column_header_path)
        print(f"   - Left column (header part): {left_column_header_box} -> {left_column_header_path}")
    else:
        print(f"   - Left column body: Skipped (invalid dimensions)")
    
    # Main content (right part, body only - excluding header)
    main_content_box = (left_column_width, header_height, body_width, body_height)
    if body_width - left_column_width > 0 and body_height > header_height:
        main_content_img = body_img.crop(main_content_box)
        main_content_path = os.path.join(output_dir, "body_right.jpg")
        main_content_img.save(main_content_path)
        print(f"   - Main content: {main_content_box} -> {main_content_path}")
        
        # Also create main content header for completeness
        main_header_box = (left_column_width, 0, body_width, header_height)
        main_header_img = body_img.crop(main_header_box)
        main_header_path = os.path.join(output_dir, "body_right_header.jpg")
        main_header_img.save(main_header_path)
        print(f"   - Main content header: {main_header_box} -> {main_header_path}")
    else:
        print(f"   - Main content: Skipped (invalid dimensions)")
    
    # 4. Create visualization of the split
    print(f"\n4. Creating visualization of the split:")
    create_split_visualization(body_width, body_height, left_column_width, header_height, output_dir)
    
    # 5. Create HTML test file
    print(f"\n5. Creating HTML test file:")
    create_html_test_file(output_dir, body_width, body_height, left_column_width, header_height)
    
    print(f"\n" + "=" * 50)
    print(f"All images have been split successfully!")
    print(f"Output directory: {os.path.abspath(output_dir)}")
    print(f"\nFiles created:")
    for file in os.listdir(output_dir):
        if file.endswith(('.jpg', '.png', '.html')):
            filepath = os.path.join(output_dir, file)
            filesize = os.path.getsize(filepath) / 1024  # KB
            print(f"  - {file} ({filesize:.1f} KB)")
    
    print(f"\nRequired files for the freeze pane viewer:")
    print(f"  1. header_right.jpg - Right part of header")
    print(f"  2. body_left.jpg    - Left column (body part only)")
    print(f"  3. body_right.jpg   - Main content area")

def create_split_visualization(total_width, total_height, left_width, header_height, output_dir):
    """Create a visual representation of how the image is split."""
    from PIL import ImageDraw, ImageFont
    
    # Create a blank image for visualization
    vis_width = min(800, total_width // 10)
    vis_height = min(600, total_height // 10)
    
    vis_img = Image.new('RGB', (vis_width, vis_height), color='white')
    draw = ImageDraw.Draw(vis_img)
    
    # Calculate scaled dimensions
    scale_x = vis_width / total_width
    scale_y = vis_height / total_height
    
    left_scaled = int(left_width * scale_x)
    header_scaled = int(header_height * scale_y)
    
    # Draw grid
    draw.rectangle([0, 0, vis_width, vis_height], outline='black', width=2)
    
    # Draw vertical line for left column
    if left_scaled > 0:
        draw.line([left_scaled, 0, left_scaled, vis_height], fill='red', width=2)
    
    # Draw horizontal line for header
    if header_scaled > 0:
        draw.line([0, header_scaled, vis_width, header_scaled], fill='blue', width=2)
    
    # Label the sections
    try:
        font = ImageFont.truetype("arial.ttf", 12)
    except:
        font = ImageFont.load_default()
    
    # Top-left corner
    if left_scaled > 10 and header_scaled > 10:
        draw.text((5, 5), "Corner", fill='black', font=font)
    
    # Top-right (header)
    if left_scaled < vis_width - 60 and header_scaled > 10:
        draw.text((left_scaled + 5, 5), "Header", fill='black', font=font)
    
    # Bottom-left (left column)
    if left_scaled > 10 and header_scaled < vis_height - 20:
        draw.text((5, header_scaled + 5), "Left Column", fill='black', font=font)
    
    # Bottom-right (main content)
    if left_scaled < vis_width - 100 and header_scaled < vis_height - 20:
        draw.text((left_scaled + 5, header_scaled + 5), "Main Content", fill='black', font=font)
    
    # Add dimension labels
    draw.text((vis_width // 2 - 30, vis_height - 15), f"{total_width} x {total_height}", fill='gray', font=font)
    
    # Save visualization
    vis_path = os.path.join(output_dir, "split_visualization.png")
    vis_img.save(vis_path)
    print(f"   - Visualization saved to: {vis_path}")

def create_html_test_file(output_dir, total_width, total_height, left_width, header_height):
    """Create an HTML file to test the split images."""
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Split Images Test</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        .container {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }}
        .section {{ border: 1px solid #ddd; padding: 10px; background: #f9f9f9; }}
        h2 {{ color: #333; border-bottom: 2px solid #666; padding-bottom: 5px; }}
        .image-info {{ font-family: monospace; background: #eee; padding: 5px; margin: 5px 0; }}
        img {{ max-width: 100%; height: auto; border: 1px solid #ccc; }}
        .dimensions {{ color: #666; font-size: 0.9em; }}
        .required {{ background: #e7f7e7; border-left: 4px solid #2ecc71; padding: 10px; margin: 10px 0; }}
        .optional {{ background: #f0f0f0; border-left: 4px solid #95a5a6; padding: 10px; margin: 10px 0; }}
    </style>
</head>
<body>
    <h1>Split Images Test</h1>
    <p class="dimensions">Original: {total_width} x {total_height} | Left column: {left_width}px | Header: {header_height}px</p>
    
    <div class="required">
        <h3>Required Files for Freeze Pane Viewer:</h3>
        <ol>
            <li><strong>header_right.jpg</strong> - Right part of header (for frozen top row)</li>
            <li><strong>body_left.jpg</strong> - Left column body section (for frozen left column)</li>
            <li><strong>body_right.jpg</strong> - Main content area (scrollable area)</li>
        </ol>
    </div>
    
    <div class="container">
        <div class="section">
            <h2>1. Header Right (Required)</h2>
            <div class="image-info">header_right.jpg - For frozen header</div>
            <img src="header_right.jpg" alt="Header Right" onerror="this.style.display='none';">
        </div>
        
        <div class="section">
            <h2>2. Body Left (Required)</h2>
            <div class="image-info">body_left.jpg - For frozen left column</div>
            <img src="body_left.jpg" alt="Body Left" onerror="this.style.display='none';">
        </div>
        
        <div class="section">
            <h2>3. Body Right (Required)</h2>
            <div class="image-info">body_right.jpg - For main scrollable content</div>
            <img src="body_right.jpg" alt="Body Right" onerror="this.style.display='none';">
        </div>
        
        <div class="section">
            <h2>4. Corner (Optional)</h2>
            <div class="image-info">corner.jpg - Top-left corner intersection</div>
            <img src="corner.jpg" alt="Corner" onerror="this.style.display='none';">
        </div>
    </div>
    
    <div class="optional">
        <h3>Other Generated Files:</h3>
        <p>These are for reference and debugging:</p>
        <ul>
            <li>body_left_full.jpg - Full left column (including header)</li>
            <li>body_right_full.jpg - Full right part (including header)</li>
            <li>body_left_header.jpg - Header part of left column</li>
            <li>body_right_header.jpg - Header part of main content</li>
            <li>split_visualization.png - Visual guide of the split</li>
        </ul>
    </div>
    
    <div style="margin-top: 30px; padding: 15px; background: #e3f2fd; border-left: 4px solid #2196f3;">
        <h3>Next Steps:</h3>
        <ol>
            <li>Copy the 3 required files to your web server directory</li>
            <li>Update the HTML freeze pane viewer to use these files</li>
            <li>Test the viewer with the new split images</li>
        </ol>
        <p><strong>Note:</strong> The freeze pane HTML code needs to be updated to reference these split images.</p>
    </div>
</body>
</html>
"""
    
    html_path = os.path.join(output_dir, "test_split.html")
    with open(html_path, 'w') as f:
        f.write(html_content)
    
    print(f"   - HTML test file saved to: {html_path}")

def main():
    parser = argparse.ArgumentParser(description='Split images for Excel-like freeze pane viewer')
    parser.add_argument('--header', default='cc_h.jpg', help='Path to header image (default: cc_h.jpg)')
    parser.add_argument('--body', default='cc_b.jpg', help='Path to body image (default: cc_b.jpg)')
    parser.add_argument('--left-width', type=int, default=85, help='Width of left column in pixels (default: 300)')
    parser.add_argument('--header-height', type=int, default=989, help='Height of header in pixels (default: 989)')
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("Image Splitter for Excel-like Freeze Pane Viewer")
    print("=" * 60)
    
    split_images(args.header, args.body, args.left_width, args.header_height)

if __name__ == "__main__":
    main()