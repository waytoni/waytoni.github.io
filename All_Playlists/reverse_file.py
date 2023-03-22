# Open the input file for reading
with open('All_Playlists/to_be_reversed.html', 'r', encoding="utf-8") as f:

    # Read the lines of the input file into a list
    lines = f.readlines()

# Open the output file for writing
with open('All_Playlists/A_G_sorted.html', 'w', encoding="utf-8") as f:

    # Reverse the order of the lines list
    lines.reverse()

    # Write the reversed lines to the output file
    for line in lines:
        f.write(line)
