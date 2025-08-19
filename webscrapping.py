import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

url = 'https://www.eia.gov/dnav/pet/pet_pri_spt_s1_d.htm'  # Replace with the URL of the website you want to scrape
baseurl = 'https://www.eia.gov/dnav/pet/'
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

# Find the table containing the data
link = soup.find('a', {'class': 'crumb'})  # Replace 'data-table' with the actual id or class of the table

print(link)
documentLink = link['href']
print(documentLink)

# Handle relative URLs
full_url = os.path.join(baseurl, documentLink)

print('Full URL:', full_url)

# Step 3: Download the document
document_response = requests.get(full_url)

# Check if the document request was successful
if document_response.status_code == 200:
    # Save the document to a file
    with open('report.xls', 'wb') as file:
        file.write(document_response.content)
    print('Document downloaded successfully.')
else:
    print('Failed to download the document. Status code:', document_response.status_code)
    
    
    
