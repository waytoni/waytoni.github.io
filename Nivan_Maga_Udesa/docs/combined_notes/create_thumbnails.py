from PIL import Image
import os

# Set the desired width for the resized images
width = 300

# Set the path to the folder containing the images
folder_path = './Nivan_Maga_Udesa/docs/combined_notes'

# Loop through all the files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an image
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
        # Open the image file
        with Image.open(os.path.join(folder_path, filename)) as img:
            # Calculate the height of the resized image to maintain aspect ratio
            height = int((float(img.size[1]) * float(width / float(img.size[0]))))
            # Resize the image
            img = img.resize((width, height))
            # Save the resized image with a new filename
            #img.save(os.path.join(folder_path+'/'+'thumbnails', f'{filename[:-4]}_resized.jpg'))
            img.save(os.path.join(folder_path+'/'+'thumbnails', f'{filename}'))
