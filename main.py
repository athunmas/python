import requests
from bs4 import BeautifulSoup
import datetime
import schedule
import time
# Mở file ở chế độ ghi 'w' sẽ tự động xóa hết nội dung hiện tại của file
 # Không ghi gì vào file, file sẽ bị xóa trắng
def my_join():
    x = datetime.datetime.now()
    with open('file.csv', 'a' ,encoding= 'utf-8' ) as file:
        file.writelines(f"{x} \n")
    url = 'https://www.pnj.com.vn/blog/gia-vang/?r=1726709709840'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('tbody' , id = 'content-price')
        rows = table.find_all('tr')
        for row in rows:
            columns = row.find_all('td')
            name = columns[0].text.strip()
            purchaseprice = columns[1].text.strip()
            sellingprice = columns[2].text.strip()
            with open('file.csv', 'a', encoding = 'utf-8') as file:
                file.writelines(f"{name}, {purchaseprice}, {sellingprice} \n")
my_join()