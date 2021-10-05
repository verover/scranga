from bs4 import BeautifulSoup

# Local Scraping on HTML Files
with open('index.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    check_item = soup.find_all('div', class_='item')
    for item in check_item:
        item_name = item.h1.text
        item_price = item.a.text.split()[-1]

        print(f'Les {item_name} harganya {item_price}')
