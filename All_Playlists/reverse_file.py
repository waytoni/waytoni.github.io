# Open the input file for reading
with open('All_Playlists/all_videos.txt', 'r', encoding="utf-8") as f:

    # Read the lines of the input file into a list
    lines = f.readlines()

# Open the output file for writing
with open('All_Playlists/reversed.html', 'w', encoding="utf-8") as f:

    # Reverse the order of the lines list
    lines.reverse()
    selected_lines = [line for line in lines if 'Abhidhamma lesson Kalutara Bodhiya D' in line]
    # selected_lines = [f"{index + 1} {line}" for index, line in enumerate(lines) if 'Abhidhamma lesson Kalutara Bodhiya G' in line]
    
    # Write the reversed lines to the output file
    for line in lines:
        f.write(line)


with open('All_Playlists/D_series.txt', 'w', encoding="utf-8") as f:
    for line in selected_lines:
        f.write(line)