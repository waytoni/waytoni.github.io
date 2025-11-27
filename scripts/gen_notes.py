import os
import sys
from PIL import Image

sys.path.append('scripts/py')
from utilities import *

def generate_thumbnail(source_path, thumb_path, width=300):
    """Generate thumbnail for an image"""
    try:
        with Image.open(source_path) as img:
            # Calculate the height to maintain aspect ratio
            height = int((float(img.size[1]) * float(width / float(img.size[0]))))
            # Resize the image
            img = img.resize((width, height))
            # Save the resized image
            img.save(thumb_path)
            return True
    except Exception as e:
        print(f"Error generating thumbnail for {source_path}: {e}")
        return False

def prepare_thumbnails_folder(basepath):
    """Ensure thumbnails folder exists and create subfolders if needed"""
    thumbnails_path = os.path.join(basepath, 'thumbnails')
    if not os.path.exists(thumbnails_path):
        os.makedirs(thumbnails_path)
    
    # Create subfolders in thumbnails to match main structure
    for folder in ['General', 'ChiththaVeethi', 'Chithasika']:
        subfolder_path = os.path.join(thumbnails_path, folder)
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)
    
    return thumbnails_path

def generate_thumbnails_for_folder(folder_path, thumbnails_base_path, folder_name=""):
    """Generate thumbnails for all images in a folder"""
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(image_extensions):
            source_path = os.path.join(folder_path, filename)
            
            # Determine thumbnail path based on whether it's a subfolder or base
            if folder_name:
                thumb_path = os.path.join(thumbnails_base_path, folder_name, filename)
            else:
                thumb_path = os.path.join(thumbnails_base_path, filename)
            
            # Generate thumbnail if it doesn't exist
            if not os.path.exists(thumb_path):
                print(f"Generating thumbnail for: {filename}")
                generate_thumbnail(source_path, thumb_path)
            else:
                print(f"Thumbnail already exists for: {filename}")

def write_image_grid(fp, image_files, base_folder="", thumb_folder=""):
    """Write HTML grid for a set of image files"""
    fp.write('\t<div class="grid-container">\n')
    
    for file in image_files:
        # Determine paths for image and thumbnail
        if base_folder:
            image_path = f"{base_folder}/{file}"
            thumb_path = f"{thumb_folder}/{base_folder}/{file}"
        else:
            image_path = file
            thumb_path = f"{thumb_folder}/{file}"
        
        fp.write("\t\t<div class=\"grid-item\">\n")
        fp.write(f'\t\t<a href="{image_path}"><img src="{thumb_path}" alt="{file}"></a>')
        fp.write(f'\t\t<p>{file}</p>\n')
        fp.write('\t\t</div>\n')
    
    fp.write('\t</div>\n')

def get_image_files(folder_path):
    """Get list of image files from a folder"""
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')
    image_files = []
    
    for file in os.listdir(folder_path):
        if file.lower().endswith(image_extensions):
            image_files.append(file)
    
    # Sort files for consistent ordering
    image_files.sort()
    return image_files

def main():
    basepath = './documents/NotesForDesana'
    intro_file = os.path.join(basepath, 'NotesForDesana_intro.html')
    html_file = os.path.join(basepath, 'NotesForDesana.html')
    series_title = 'සියලු දේශනා සඳහා සටහන්'
    
    Filelist_styles = """
    <link rel="stylesheet" type="text/css" href="/css/file_list.css">
    """
    
    # Prepare thumbnails folder structure
    thumbnails_path = prepare_thumbnails_folder(basepath)
    
    # Generate thumbnails for all images
    print("Generating thumbnails for base folder...")
    generate_thumbnails_for_folder(basepath, thumbnails_path)
    
    subfolders = {
        'General': 'General',
        'Chithasika': 'චිත්ත සහ චෛතසික චක්‍ර',
        'ChiththaVeethi': 'චිත්ත වීති සඳහා'
    }
    
    for folder, title in subfolders.items():
        folder_path = os.path.join(basepath, folder)
        if os.path.exists(folder_path):
            print(f"Generating thumbnails for {folder} folder...")
            generate_thumbnails_for_folder(folder_path, thumbnails_path, folder)
    
    # Create HTML file
    print(f"Creating HTML file: {html_file}")
    PrepareHeadSimpleStyles(html_file, series_title, Filelist_styles)
    
    # Write introduction
    with open(html_file, 'a', encoding='utf-8') as fp:
        with open(intro_file, 'r', encoding='utf-8') as fintro:
            page_intro = fintro.read()
            fp.write(page_intro)
        
        # Section 1: Base folder images
        base_images = get_image_files(basepath)
        if base_images:
            #fp.write('\n\t<h2>ප්‍රධාන සටහන්</h2>\n')
            write_image_grid(fp, base_images, "", "thumbnails")
        
        # Section 2: General folder images
        general_path = os.path.join(basepath, 'General')
        if os.path.exists(general_path):
            general_images = get_image_files(general_path)
            if general_images:
                #fp.write('\n\t<h2>සාමාන්‍ය සටහන්</h2>\n')
                write_image_grid(fp, general_images, "General", "thumbnails")
        
        # Section 3: Chithasika folder images
        chithasika_path = os.path.join(basepath, 'Chithasika')
        if os.path.exists(chithasika_path):
            chithasika_images = get_image_files(chithasika_path)
            if chithasika_images:
                fp.write('\n\t<h2>චිත්ත සහ චෛතසික චක්‍ර විග්‍රහය සඳහා</h2>\n')
                write_image_grid(fp, chithasika_images, "Chithasika", "thumbnails")
        
        # Section 4: ChiththaVeethi folder images
        chiththaveethi_path = os.path.join(basepath, 'ChiththaVeethi')
        if os.path.exists(chiththaveethi_path):
            chiththaveethi_images = get_image_files(chiththaveethi_path)
            if chiththaveethi_images:
                fp.write('\n\t<h2>චිත්ත වීති විග්‍රහය සඳහා</h2>\n')
                write_image_grid(fp, chiththaveethi_images, "ChiththaVeethi", "thumbnails")
        
        # Close HTML file
        fp.write('</body>\n')
        fp.write('</html>\n')
    
    print("HTML file generation completed successfully!")

if __name__ == "__main__":
    main()