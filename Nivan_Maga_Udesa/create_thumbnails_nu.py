from PIL import Image
import os

# Set the desired width for the resized images
width = 300
resize_factor = 3

# Set the path to the folder containing the images
folder_path = './Nivan_Maga_Udesa/docs'

# Loop through all the files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an image
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Open the image file
        with Image.open(os.path.join(folder_path, filename)) as img:
            # Calculate the height of the resized image to maintain aspect ratio
            height = int((float(img.size[1]) * float(width / float(img.size[0]))))
            
            # Resize the image using width
            # img = img.resize((width, height))
            
            # Resize the image using resize_factor
            img = img.resize((int((img.size[0])/resize_factor), int((img.size[1])/resize_factor)))

            # Save the resized image with a new filename
            #img.save(os.path.join(folder_path+'/'+'thumbnails', f'{filename[:-4]}_resized.jpg'))
            img.save(os.path.join(folder_path+'/'+'thumbnails', f'{filename}'))
