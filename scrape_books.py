import sqlite3
import requests
from bs4 import BeautifulSoup


BASE_URL = "http://books.toscrape.com/catalogue/category/books_1/"


def get_books_data(BASE_URL):
    page = "page-1.html"
    books = []

    while page:
        print(f"Scraping {BASE_URL}{page}...")
        response = requests.get(f"{BASE_URL}{page}")
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find_all("article")
        for book in data:
            books.append((get_title(book), get_price(book), get_raiting(book)))
        next_btn = soup.select(".next a")
        page = next_btn[0]["href"] if next_btn else None

    save_to_db(books)

    print(books)


def save_to_db(books):
    conn = sqlite3.connect("books.db")
    c = conn.cursor()
    c.execute("CREATE TABLE books (title TEXT, price REAL, rating INTEGER)")
    with conn:
        c.executemany("INSERT INTO books VALUES (?, ?, ?)", books)


def get_title(book):
    return book.select("h3 a")[0]["title"]


def get_price(book):
    return "{0:.2f}".format(float(book.select(".price_color")[0].get_text()[2:]))


def get_raiting(book):
    raiting_values = {"Zero": 0, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    stars = book.select(".star-rating")[0]["class"][1]
    return raiting_values[stars]


get_books_data(BASE_URL)
