# Extract left column (300px wide, full height)
convert cc_b.jpg -crop 300x5417+0+0 body_left.jpg

# Extract right part (9300px wide, full height)  
convert cc_b.jpg -crop 9300x5417+300+0 body_right.jpg

# Extract header from right part (first 989px)
convert body_right.jpg -crop 9300x989+0+0 header_right.jpg

# Trim body_right to remove header part
convert body_right.jpg -crop 9300x4428+0+989 +repage body_right.jpg

# Trim body_left to remove header part
convert body_left.jpg -crop 300x4428+0+989 +repage body_left.jpg