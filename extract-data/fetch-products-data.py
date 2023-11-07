import requests;
import json;

#request alapján kérem le a választ

#a fetch-elés során megadom, hány terméket adjon vissza a query
#viszont van egy limit, amit le lehet kérni, az a 60 (!!!!!)
getItemNumberFrom = 1;
getItemNumberTo = 60;

currentWebsiteURL = f"https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=A8E79F4E6C1E87AE9BE943F8217C88B8&country=hu&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(HU)%26filter%3Dlanguage(hu)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(4ce3d7b4-9566-485a-92a8-7797222b7f93)%26anchor%3D{getItemNumberFrom}%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D{getItemNumberTo}&language=hu&localizedRangeStr=%7BlowestPrice%7D%20%E2%80%93%20%7BhighestPrice%7D";
currentRequestData = requests.get(url=currentWebsiteURL);

websiteHTMLDataJSON = json.loads(currentRequestData.text);
#végig tudunk iterálni elemeken
fetchedProductsDataJSON = websiteHTMLDataJSON['data']['products']['products'];

print(fetchedProductsDataJSON);