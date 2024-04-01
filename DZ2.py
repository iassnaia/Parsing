import requests
from bs4 import BeautifulSoup
import json


# Функция для извлечения информации о книгах
def scrape_books(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = []

    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']
        price_text = book.find('p', class_='price_color').text.strip().replace('£', '').replace('Â', '')
        price = float(price_text)

        stock = "в наличии"

        description_elem = book.find('p', class_='excerpt')
        description = description_elem.text.strip() if description_elem else ''

        books.append({
            'title': title,
            'price': price,
            'stock': stock,
            'description': description
        })

    return books


# Главная функция для скрапинга книг во всех категориях
def scrape_all_books():
    base_url = 'http://books.toscrape.com/'
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    categories = soup.find('ul', class_='nav-list').find_all('a')

    all_books = []

    for category in categories:
        category_url = base_url + category['href']
        category_name = category.text.strip()
        print("Scraping category:", category_name)
        books_in_category = scrape_books(category_url)
        all_books.extend(books_in_category)

    return all_books


# Сохранение данных в JSON-файл
def save_to_json(data, filename='books.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    all_books_data = scrape_all_books()
    save_to_json(all_books_data)
