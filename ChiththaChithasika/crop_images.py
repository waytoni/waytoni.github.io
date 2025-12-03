#!/usr/bin/env python3
"""
CORRECTED: Image Splitter for Freeze Pane Viewer
Splits body image into left column and main content (FULL HEIGHT)
"""

from PIL import Image
import os
import argparse

def split_body_image(body_path, left_column_width=85):
    """
    Split body image into left column and main content (FULL HEIGHT).
    
    Args:
        body_path: Path to body image (cc_b.jpg)
        left_column_width: Width of the frozen left column (in pixels)
    """
    
    # Create output directory
    output_dir = "split_images"
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Splitting body image with left column width: {left_column_width}px")
    print(f"Output directory: {output_dir}")
    print("-" * 50)
    
    # Load body image
    try:
        body_img = Image.open(body_path)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return
    
    # Get image dimensions
    body_width, body_height = body_img.size
    
    print(f"Body image: {body_width}x{body_height}")
    
    if left_column_width >= body_width:
        print(f"Error: Left column width ({left_column_width}) is greater than or equal to body width ({body_width})")
        return
    
    # 1. Extract LEFT COLUMN from body (FULL HEIGHT)
    print(f"\n1. Creating LEFT COLUMN (body_left.jpg):")
    left_column_box = (0, 0, left_column_width, body_height)
    left_column_img = body_img.crop(left_column_box)
    left_column_path = os.path.join(output_dir, "body_left.jpg")
    left_column_img.save(left_column_path)
    print(f"   - Crop box: {left_column_box}")
    print(f"   - Dimensions: {left_column_img.size}")
    print(f"   - Saved to: {left_column_path}")
    
    # 2. Extract MAIN CONTENT from body (FULL HEIGHT, everything except left column)
    print(f"\n2. Creating MAIN CONTENT (body_right.jpg):")
    main_content_box = (left_column_width, 0, body_width, body_height)
    main_content_img = body_img.crop(main_content_box)
    main_content_path = os.path.join(output_dir, "body_right.jpg")
    main_content_img.save(main_content_path)
    print(f"   - Crop box: {main_content_box}")
    print(f"   - Dimensions: {main_content_img.size}")
    print(f"   - Saved to: {main_content_path}")
    
    # 3. Also create a debug image showing the overlap
    print(f"\n3. Creating debug overlay image:")
    debug_img = Image.new('RGB', (body_width, body_height), color='white')
    
    # Paste left column
    debug_img.paste(left_column_img, (0, 0))
    
    # Paste main content with red border to show alignment
    debug_img.paste(main_content_img, (left_column_width, 0))
    
    # Draw red line at the split
    from PIL import ImageDraw
    draw = ImageDraw.Draw(debug_img)
    draw.line([(left_column_width, 0), (left_column_width, body_height)], 
              fill='red', width=3)
    
    # Add text labels
    draw.text((10, 10), "body_left.jpg", fill='green', stroke_width=2, stroke_fill='white')
    draw.text((left_column_width + 10, 10), "body_right.jpg", fill='blue', stroke_width=2, stroke_fill='white')
    draw.text((left_column_width + 10, 50), f"Starts at: ({left_column_width}, 0)", fill='black')
    
    debug_path = os.path.join(output_dir, "debug_alignment.jpg")
    debug_img.save(debug_path, quality=50)
    print(f"   - Debug image saved to: {debug_path}")
    
    # 4. Copy header image if it exists
    print(f"\n4. Looking for header image:")
    header_path = "cc_h.jpg"
    if os.path.exists(header_path):
        try:
            import shutil
            header_dest = os.path.join(output_dir, "cc_h.jpg")
            shutil.copy2(header_path, header_dest)
            header_img = Image.open(header_path)
            print(f"   - Found: cc_h.jpg ({header_img.size})")
            print(f"   - Copied to: {header_dest}")
        except Exception as e:
            print(f"   - Warning: {e}")
    else:
        print(f"   - Not found: cc_h.jpg")
        print(f"   - IMPORTANT: You need cc_h.jpg for the freeze pane viewer!")
    
    print(f"\n" + "=" * 50)
    print(f"SUCCESS! Created 2 files from body image:")
    print(f"1. body_left.jpg  - {left_column_img.size} (FULL HEIGHT)")
    print(f"2. body_right.jpg - {main_content_img.size} (FULL HEIGHT)")
    print(f"\nBoth images start at Y=0 (top of body image)")
    print(f"\nYou also need: cc_h.jpg (original header image)")
    print(f"\nTotal files needed for freeze pane viewer: 3")

def main():
    parser = argparse.ArgumentParser(description='Split body image for freeze pane viewer')
    parser.add_argument('--body', default='cc_b.jpg', help='Path to body image (default: cc_b.jpg)')
    parser.add_argument('--left-width', type=int, default=85, help='Width of left column in pixels (default: 85)')
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("CORRECTED: Freeze Pane Image Splitter")
    print("Creates: body_left.jpg and body_right.jpg (FULL HEIGHT)")
    print("=" * 60)
    
    split_body_image(args.body, args.left_width)

if __name__ == "__main__":
    main()