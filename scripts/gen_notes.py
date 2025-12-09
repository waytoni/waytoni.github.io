import os
import sys
from PIL import Image

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

def prepare_image_grid(image_files, base_folder="", thumb_folder=""):
    image_grid = ''
    
    for file in image_files:
        # Determine paths for image and thumbnail
        if base_folder:
            image_path = f"{base_folder}/{file}"
            thumb_path = f"{thumb_folder}/{base_folder}/{file}"
        else:
            image_path = file
            thumb_path = f"{thumb_folder}/{file}"
        
        image_grid += f'<div class="grid-item">'
        image_grid += f'<a href="{image_path}"><img src="{thumb_path}" alt="{file}"></a>'
        image_grid += f'<p>{file}</p>'
        image_grid += '</div>'
    return image_grid 

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
    html_file = os.path.join(basepath, 'NotesForDesana.html')
    navigation_file = 'scripts/templates/navigation_header_template.html'  # Adjusted path
    template_file = os.path.join('scripts', 'templates/NotesForDesana_template.html')
   
    
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

    # Read template
    try:
        with open(template_file, 'r', encoding='utf-8') as file:
            template_content = file.read()
    except FileNotFoundError:
        print(f"Error: Template file {template_file} not found.")
        return
    
    # Replace navigation header
    try:
        with open(navigation_file, 'r', encoding='utf-8') as file:
            navigation_content = file.read()
        template_content = template_content.replace('$NAVIGATION_HEADER$', navigation_content)
        print("Successfully replaced navigation header")
    except FileNotFoundError:
        print(f"Error: Navigation file {navigation_file} not found.")
        return
    
    
      
    # Section 1: Base folder images
    base_images = get_image_files(basepath)
    if base_images:
        base_images_content = prepare_image_grid(base_images, "", "thumbnails") 
    
    template_content = template_content.replace('$MAIN_FOLDER_IMAGES$', base_images_content)
    print("Successfully replaced main folder images")
    
    # Section 2: General folder images
    general_path = os.path.join(basepath, 'General')
    if os.path.exists(general_path):
        general_images = get_image_files(general_path)
        if general_images:
            general_images_content = prepare_image_grid(general_images, "General", "thumbnails")
    
    template_content = template_content.replace('$GENERAL_FOLDER_IMAGES$', general_images_content)
    print("Successfully replaced general folder images")
    
    # Section 3: Chithasika folder images
    chithasika_path = os.path.join(basepath, 'Chithasika')
    if os.path.exists(chithasika_path):
        chithasika_images = get_image_files(chithasika_path)
        if chithasika_images:
            chithasika_images_content = prepare_image_grid(chithasika_images, "Chithasika", "thumbnails")   
    
    template_content = template_content.replace('$CHITHASIKA_FOLDER_IMAGES$', chithasika_images_content)
    print("Successfully replaced chithasika folder images") 
    
    # Section 4: ChiththaVeethi folder images
    chiththaveethi_path = os.path.join(basepath, 'ChiththaVeethi')
    if os.path.exists(chiththaveethi_path):
        chiththaveethi_images = get_image_files(chiththaveethi_path)
        if chiththaveethi_images:
            chiththaveethi_images_content = prepare_image_grid(chiththaveethi_images, "ChiththaVeethi", "thumbnails")
    
    template_content = template_content.replace('$CHITHTHAVEETHI_FOLDER_IMAGES$', chiththaveethi_images_content)
    print("Successfully replaced chiththaveethi folder images")

    
    # Write output file
    try:
        with open(html_file, 'w', encoding='utf-8') as file:
            file.write(template_content)
        print(f"Successfully generated {html_file}")
    except Exception as e:
        print(f"Error writing output file: {e}")

if __name__ == "__main__":
    main()