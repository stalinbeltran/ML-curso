import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

url = 'https://utilitytransitionhub.rmi.org/data-download/'  # Replace with the URL of the website you want to scrape
baseurl = 'https://utilitytransitionhub.rmi.org/data-download/'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print('Request successful!')
else:
    print('Failed to retrieve the webpage')
    
soup = BeautifulSoup(response.content, 'html.parser')

# Print the title of the webpage to verify
print(soup.title.text)
#print(soup)

# Find all document links on the page
divs = soup.find_all('div', {'class': 'download'})
#document_links
# Loop through each link and download the corresponding document
for i, div in enumerate(divs):
    link = div.find('a')
    document_url = os.path.join(baseurl, link['href'])
    try:
        print("trying url: ", document_url)
        document_response = requests.get(document_url)
        
    except Exception as e:
        print("error in url: ", document_url)
        print(e)
    
    if document_response.status_code == 200:
        # Save each document with a unique name
        file_name = f'report_{i+1}.pdf'
        with open(file_name, 'wb') as file:
            file.write(document_response.content)
        print(f'Document {i+1} downloaded successfully as {file_name}.')
    else:
        print(f'Failed to download document {i+1}. Status code:', document_response.status_code)
    
