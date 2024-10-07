import requests
from bs4 import BeautifulSoup

find = "Weather in Paris now"
url = f'https://www.google.com/search?q={find}'

req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

weather = soup.find('div', class_ = 'BNeawe').text
print(weather)