from email.mime import image
from itertools import product
import requests
from bs4 import BeautifulSoup 
from send_email import sendMail


url1="https://www.trendyol.com/nike/bq3207-wmns-revolution-5-p-33522061?boutiqueId=610684&merchantId=526575"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}


page=requests.get(url1,headers=headers)

htmlPage = BeautifulSoup(page.content, 'html.parser')

productTitle = htmlPage.find("h1", class_="pr-new-br").get_text()

price=htmlPage.find("span", class_="prc-dsc").get_text()

image=htmlPage.find("img", class_="hoverZoomLink")
convertedPrice=float(price.replace(",",".").replace("TL",""))
if (convertedPrice <=2000):
    print("Ürünün fiyatı Düştü")
    htmlEmailContent = """\
    <html>
    <head> </head>
    <body>
    <h1>{0}</h1>
    <br/>
    {1}
    <p>Ürün Linki: {2}</p>
    </body>
    </html>
        """ .format(productTitle,image,url1)

    sendMail("ataoz412@gmail.com","Ürünün fiyatı Düştü",htmlEmailContent)

print(convertedPrice)
 