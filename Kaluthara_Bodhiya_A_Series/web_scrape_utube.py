import requests
from bs4 import BeautifulSoup

# Get the HTML content of the video's page
url = "https://www.youtube.com/watch?v=xh8dRapA4do"
page = requests.get(url)

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(page.content, "html.parser")

print (soup)

# Find the element containing the video's posted date
posted_date_element = soup.find("strong", {"class": "watch-time-text"})

# Extract the posted date text
posted_date = posted_date_element.text

print("The video was posted on:", posted_date)
