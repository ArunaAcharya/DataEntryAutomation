from bs4 import BeautifulSoup
import requests
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from  fill_form import FillForm
link ="https://docs.google.com/forms/d/e/1FAIpQLSdq75K7SINQqaGOV0K6ebC8n6XZ4wrAYYrqq3BUVBpPtrOyIA/viewform?usp=sf_link"

response= requests.get("https://www.rent.com.au/properties/sydney-nsw-2000")
website_data= response.text

soup = BeautifulSoup(website_data, "html.parser")

all_price=[]
all_address=[]
all_links=[]

prices = soup.find_all(class_= "price")
for price in prices:
   all_price.append(price.text.split("\nApartment\n")[0].strip('\n'))
addresses= soup.find_all(name="h2", class_="address")
for address in addresses:
    all_address.append(address.text)
links= soup.find_all(name="a", class_="asset")
for link in links:
    all_links.append(link.get('href'))

bot= FillForm(Service(ChromeDriverManager().install()))
for _ in range(len(all_address)):
    bot.fill_form(all_address[_], all_price[_],all_links[_])



