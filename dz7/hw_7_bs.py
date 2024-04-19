import requests
from bs4 import BeautifulSoup
import json

url = 'https://books.toscrape.com/catalogue/category/books/travel_2/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

try:
    books_data = []

    for book in soup.find_all('h3'):
        title = book.a['title']
        book_url = book.a['href']
        full_book_url = f'https://books.toscrape.com/catalogue{book_url}'
        price = book.find_next('p', class_='price_color').text.strip()[2:]
        availability = book.find_next('p', class_='instock availability').text.strip()

        # Сохранение данных в виде словаря
        book_data = {
            'Title': title,
            'URL': full_book_url,
            'Price': price,
            'Availability': availability
        }

        books_data.append(book_data)

    # Сохранение данных в JSON-файл
    output_file = 'travel_books_data.json'
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(books_data, json_file, ensure_ascii=False, indent=2)

    print(f'Требуемая информация находится в файле {output_file}')

except Exception as e:
    print("Что-то пошло не так!")
