import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

URL = 'https://appbrewery.github.io/instant_pot/'
HEADERS = {
    'Accept-Language': 'en-US',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}
response = requests.get(url=URL, headers=HEADERS)
soup = BeautifulSoup(response.text, 'html.parser')


TARGET_PRICE = 100
price = ((soup.find(class_='a-offscreen').getText()).split("$")[1])
product = (soup.find(name='span', id='productTitle').getText()).split('\n')

product_name = ''
for line in product:
    product_name += ' ' + line.strip()


def send_email():

    message = f'''some of your wanted products{product_name} have been under the targeted price
    \n target :${TARGET_PRICE},current price:${price} '''

    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        connection.login(user=os.environ['EMAIL_ADDRESS'], password=os.environ['EMAIL_PASSWORD'])
        connection.sendmail(
            from_addr=os.environ['EMAIL_ADDRESS'],
            to_addrs=os.environ['EMAIL_TO_SEND'],
            msg=f'Price alert \n\n{message}'.encode("utf-8")
        )
        connection.close()


def main():

    if TARGET_PRICE > float(price):
        send_email()


if __name__ == '__main__':

    main()
