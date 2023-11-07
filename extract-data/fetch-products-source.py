import requests;
from bs4 import BeautifulSoup;

#request alapján kérek le html source-t

currentWebsiteURL = "https://www.nike.com/hu/w/ferfi-cipok-nik1zy7ok";
currentRequestData  = requests.get(currentWebsiteURL);

currentWebsiteHTMLData = BeautifulSoup(currentRequestData.text, 'html.parser');

#div-eket listázok, melyek class-ának értéke a következő
productsSourceData = currentWebsiteHTMLData.find_all('div', {'class': 'product-card__body'});

print(productsSourceData);