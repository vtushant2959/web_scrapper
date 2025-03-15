import requests
from bs4 import BeautifulSoup

# URL of the webspage I want to scrape
url = "https://www.scrapethissite.com"

# Send a GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the links on the webspage
    links = soup.find_all('a')

    # Print the URLs of the links
    for link in links:
        print(link.get('href'))
    else:
        print("Failed to retrieve the webpage")