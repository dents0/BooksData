# Books data

**Author:** Deniss Tsokarev

---

### Description
File **scrape_books.py** scrapes an [online-bookstore](http://books.toscrape.com) and creates a **SQLite** database with its data.

Once the database is created, **top10.py** is used to search the database and create data frames for the top 10 books in the following categories:
*"TOP RATED"*, *"BEST PRICE"* and *"RECOMMENDED"*. The data frames are then saved in an Excel file.

### Modules used
* [sqlite3](https://docs.python.org/2/library/sqlite3.html)
* [Requests](https://2.python-requests.org/en/master/)
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Pandas](https://pandas.pydata.org/pandas-docs/stable/)
* [XlsxWriter](https://xlsxwriter.readthedocs.io/)

---

### Result

![sc_exl](https://user-images.githubusercontent.com/28843507/57562221-17e75700-7391-11e9-9c49-4a859463ebcd.PNG)
