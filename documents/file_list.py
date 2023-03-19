import os

# directory path
dir_path = './documents'

# get all files in the directory
files = os.listdir(dir_path)

# create or open the file for writing
with open(dir_path+'/file_list.txt', 'w') as f:
    # iterate over all the files
    for file in files:
        # check if the file extension is .jpg, .png or .jpeg
        if file.endswith(('jpg', 'jpeg', 'png')):
            # write the file name to the file
            f.write("<div class=""grid-item"">\n")
            f.write('<a href="' + file + '"><img src="' + file + '" alt="' + file + '"></a>')
            f.write('<p>' + file + '</p>\n')
            f.write('</div>\n')
