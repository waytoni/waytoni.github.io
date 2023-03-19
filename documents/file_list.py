import os

# directory path
dir_path = './documents'

# get all files in the directory
files = os.listdir(dir_path)

# create file for writing
with open(dir_path+'/file_list.txt', 'w') as f:
    # iterate over all the files
    f.write('<div class="grid-container">\n')
    for file in files:
        # check if the file extension is .jpg, .png or .jpeg
        if file.endswith(('jpg', 'jpeg', 'png')):
            # write the image file names to the file
            f.write("\t<div class=""grid-item"">\n")
            f.write('\t<a href="' + file + '"><img src="' + file + '" alt="' + file + '"></a>')
            f.write('\t<p>' + file + '</p>\n')
            f.write('\t</div>\n')
    
    f.write('</div>\n')
