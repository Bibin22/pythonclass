import requests
from bs4 import BeautifulSoup

url = 'https://www.luminartechnolab.com/contact'
page = requests.get(url)
data = page.text
soup = BeautifulSoup(page.content, 'html.parser')
post_listings = soup.find_all('li', {'class': 'col-lg-3 col-md-6'})
final_posting = []
for post in post_listings:
    contact = post.find(class_='fa fa-phone').text
    print(contact)