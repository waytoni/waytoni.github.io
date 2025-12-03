#!/usr/bin/env python3
"""
COMPLETE Image Splitter for Freeze Pane Viewer
Splits the ORIGINAL complete image (9600×6387) into all needed parts
"""

from PIL import Image
import os
import argparse

def split_complete_image(original_path, header_height=989, left_column_width=85):
    """
    Split the original complete image (9600×6387) into all needed parts.
    
    Args:
        original_path: Path to original complete image (cc.jpg, 9600×6387)
        header_height: Height of the header section (989px)
        left_column_width: Width of the frozen left column (85px)
    """
    
    # Create output directory
    output_dir = "complete_split"
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Splitting complete image with:")
    print(f"  - Header height: {header_height}px")
    print(f"  - Left column width: {left_column_width}px")
    print(f"Output directory: {output_dir}")
    print("-" * 50)
    
    # Load original image
    try:
        original_img = Image.open(original_path)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return
    
    # Get image dimensions
    total_width, total_height = original_img.size
    
    print(f"Original image: {total_width}x{total_height}")
    
    if total_width != 9600 or total_height != 6387:
        print(f"Warning: Expected 9600×6387, got {total_width}×{total_height}")
    
    # Calculate body height
    body_height = total_height - header_height  # 6387 - 989 = 5398
    
    print(f"\nCalculated dimensions:")
    print(f"  - Total: {total_width}x{total_height}")
    print(f"  - Header: {total_width}x{header_height}")
    print(f"  - Body: {total_width}x{body_height}")
    print(f"  - Left column: {left_column_width}x{body_height}")
    print(f"  - Main content: {total_width-left_column_width}x{body_height}")
    
    # 1. Extract HEADER (top part, full width)
    print(f"\n1. Creating HEADER (cc_h.jpg):")
    header_box = (0, 0, total_width, header_height)
    header_img = original_img.crop(header_box)
    header_path = os.path.join(output_dir, "cc_h.jpg")
    header_img.save(header_path)
    print(f"   - Crop box: {header_box}")
    print(f"   - Dimensions: {header_img.size}")
    print(f"   - Saved to: {header_path}")
    
    # 2. Extract BODY LEFT (left column of body, full body height)
    print(f"\n2. Creating BODY LEFT (body_left.jpg):")
    body_left_box = (0, header_height, left_column_width, total_height)
    body_left_img = original_img.crop(body_left_box)
    body_left_path = os.path.join(output_dir, "body_left.jpg")
    body_left_img.save(body_left_path)
    print(f"   - Crop box: {body_left_box}")
    print(f"   - Dimensions: {body_left_img.size}")
    print(f"   - Saved to: {body_left_path}")
    
    # 3. Extract BODY RIGHT (main content of body, full body height)
    print(f"\n3. Creating BODY RIGHT (body_right.jpg):")
    body_right_box = (left_column_width, header_height, total_width, total_height)
    body_right_img = original_img.crop(body_right_box)
    body_right_path = os.path.join(output_dir, "body_right.jpg")
    body_right_img.save(body_right_path)
    print(f"   - Crop box: {body_right_box}")
    print(f"   - Dimensions: {body_right_img.size}")
    print(f"   - Saved to: {body_right_path}")
    
    # 4. Create a COMPLETE BODY image for reference
    print(f"\n4. Creating COMPLETE BODY (body_complete.jpg):")
    body_complete_box = (0, header_height, total_width, total_height)
    body_complete_img = original_img.crop(body_complete_box)
    body_complete_path = os.path.join(output_dir, "body_complete.jpg")
    body_complete_img.save(body_complete_path)
    print(f"   - Crop box: {body_complete_box}")
    print(f"   - Dimensions: {body_complete_img.size}")
    print(f"   - Saved to: {body_complete_path}")
    
    # 5. Create debug visualization
    print(f"\n5. Creating debug visualization:")
    create_debug_visualization(original_img, header_height, left_column_width, output_dir)
    
    print(f"\n" + "=" * 60)
    print(f"SUCCESS! All images created from {original_path}:")
    print(f"1. cc_h.jpg         - {header_img.size} - Header (top section)")
    print(f"2. body_left.jpg    - {body_left_img.size} - Left column (body only)")
    print(f"3. body_right.jpg   - {body_right_img.size} - Main content (body only)")
    print(f"4. body_complete.jpg - {body_complete_img.size} - Complete body for reference")
    print(f"\nNote: body_left.jpg and body_right.jpg have SAME HEIGHT: {body_height}px")
    
    # Verify alignment
    print(f"\n" + "=" * 60)
    print(f"VERIFICATION:")
    print(f"✓ body_left.jpg height: {body_left_img.height}px")
    print(f"✓ body_right.jpg height: {body_right_img.height}px")
    print(f"✓ Both should be equal: {body_left_img.height == body_right_img.height}")
    
    if body_left_img.height == body_right_img.height:
        print(f"✓ PERFECT! Vertical scrolling will sync correctly.")
    else:
        print(f"✗ WARNING: Heights differ! Vertical scrolling won't sync.")

def create_debug_visualization(original_img, header_height, left_column_width, output_dir):
    """Create debug images to show the splits."""
    from PIL import ImageDraw
    
    total_width, total_height = original_img.size
    body_height = total_height - header_height
    
    # Create a simple grid visualization
    grid_img = Image.new('RGB', (min(800, total_width//12), min(600, total_height//12)), color='white')
    draw = ImageDraw.Draw(grid_img)
    
    # Calculate scaled dimensions
    scale_x = grid_img.width / total_width
    scale_y = grid_img.height / total_height
    
    scaled_header = int(header_height * scale_y)
    scaled_left = int(left_column_width * scale_x)
    
    # Draw main borders
    draw.rectangle([0, 0, grid_img.width, grid_img.height], outline='black', width=2)
    
    # Draw header line
    draw.line([0, scaled_header, grid_img.width, scaled_header], fill='blue', width=2)
    
    # Draw left column line
    draw.line([scaled_left, scaled_header, scaled_left, grid_img.height], fill='red', width=2)
    
    # Label sections
    from PIL import ImageFont
    try:
        font = ImageFont.truetype("arial.ttf", 12)
    except:
        font = ImageFont.load_default()
    
    # Header
    draw.text((10, 5), "HEADER (cc_h.jpg)", fill='blue', font=font)
    draw.text((10, 25), f"{total_width}×{header_height}", fill='gray', font=font)
    
    # Left column
    draw.text((10, scaled_header + 5), "body_left.jpg", fill='green', font=font)
    draw.text((10, scaled_header + 25), f"{left_column_width}×{body_height}", fill='gray', font=font)
    
    # Main content
    draw.text((scaled_left + 10, scaled_header + 5), "body_right.jpg", fill='purple', font=font)
    draw.text((scaled_left + 10, scaled_header + 25), f"{total_width-left_column_width}×{body_height}", fill='gray', font=font)
    
    # Save grid
    grid_path = os.path.join(output_dir, "split_grid.png")
    grid_img.save(grid_path)
    print(f"   - Grid visualization: {grid_path}")
    
    # Create alignment test
    align_img = Image.new('RGB', (total_width, body_height), color='white')
    
    # Paste body parts with colored borders
    body_left = original_img.crop((0, header_height, left_column_width, total_height))
    body_right = original_img.crop((left_column_width, header_height, total_width, total_height))
    
    align_img.paste(body_left, (0, 0))
    align_img.paste(body_right, (left_column_width, 0))
    
    # Draw alignment line
    align_draw = ImageDraw.Draw(align_img)
    align_draw.line([(left_column_width, 0), (left_column_width, body_height)], 
                   fill='red', width=5)
    
    # Add alignment markers
    for y in [0, body_height//2, body_height-1]:
        align_draw.line([(left_column_width-10, y), (left_column_width+10, y)], 
                       fill='yellow', width=3)
    
    # Save at reduced size for viewing
    align_small = align_img.resize((min(1600, total_width), 
                                   min(1200, int(body_height * (1600/total_width)))), 
                                 Image.Resampling.LANCZOS)
    align_path = os.path.join(output_dir, "alignment_test.jpg")
    align_small.save(align_path, quality=85)
    print(f"   - Alignment test: {align_path}")

def main():
    parser = argparse.ArgumentParser(description='Split complete image for freeze pane viewer')
    parser.add_argument('--image', default='cc.jpg', help='Path to complete image (default: cc.jpg)')
    parser.add_argument('--header-height', type=int, default=989, help='Height of header in pixels (default: 989)')
    parser.add_argument('--left-width', type=int, default=85, help='Width of left column in pixels (default: 85)')
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("COMPLETE Image Splitter for Freeze Pane Viewer")
    print(f"Input: {args.image} (should be 9600×6387)")
    print("=" * 60)
    
    split_complete_image(args.image, args.header_height, args.left_width)

if __name__ == "__main__":
    main()