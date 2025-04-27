import os

def list_image_files_with_paths(folder_path):
    """
    List all image files in the specified folder with their full paths.
    """
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')
    
    try:
        all_files = os.listdir(folder_path)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}")
        return []
    
    image_files = [
        os.path.join(folder_path, file) 
        for file in all_files
        if file.lower().endswith(image_extensions)
    ]
    
    return image_files


file_list = list_image_files_with_paths('./x/NotesForDesana')

print(file_list)


import os

def list_image_files(folder_path):
    """
    List all image files in the specified folder and return their names as a Python list.
    
    Args:
        folder_path (str): Path to the folder to search for images
        
    Returns:
        list: A list of image filenames
    """
    # Common image file extensions
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')
    
    # Get all files in the folder
    try:
        all_files = os.listdir(folder_path)
    except FileNotFoundError:
        print(f"Error: Folder '{folder_path}' not found.")
        return []
    except PermissionError:
        print(f"Error: No permission to access folder '{folder_path}'.")
        return []
    
    # Filter for image files
    image_files = [
        file for file in all_files
        if file.lower().endswith(image_extensions)
    ]
    
    return image_files

# Example usage:
if __name__ == "__main__":
    # Specify your folder path here
    folder_path = "x/NotesForDesana"
    
    # Get the list of image files
    images_list = list_image_files(folder_path)
    
    # Print the results
    print(f"Found {len(images_list)} image files:")
    for image in images_list:
        print(image)
        
    print(images_list)