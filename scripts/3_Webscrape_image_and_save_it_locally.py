"""
Scraping an image from an web page and save it locally as a png

Important note:
 - There is a dependency of externals libraries. To get them, the following commands were used:
    a) pip install requests
    b) pip instal lxml
    c) pip install bs4

The page used is from Wikipedia (being open source): https://en.wikipedia.org/wiki/Gustavo_Santaolall

"""


import requests
import bs4

result = requests.get("https://en.wikipedia.org/wiki/Gustavo_Santaolalla")
result.text
# the value printed is not easy to read, so the bs4 library is used
soup = bs4.BeautifulSoup(result.text,"lxml")
soup


# now to check the url of the image to be scraped
value = soup.select(".image")[0]
value


image_link = requests.get("https://upload.wikimedia.org/wikipedia/commons/a/a1/Gustavo_Santaolalla_-_9MAR07_-presidencia-govar.jpg")

# the following lines allow to store the image locally 
f = open("C:gustavo_santaolalla_image.jpg", "wb") #"wb" means write binary
f.write(image_link.content)
f.close()