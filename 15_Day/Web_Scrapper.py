

import requests

from bs4 import BeautifulSoup

url = "https://www.codedex.io"

response = requests.get(url)
print(response)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')

    articles_titles = soup.find_all('h2', class_ = 'course-title')

    for title in articles_titles:
        print(title.text)


    
else:
    print("Failed to retrieve webpage")



