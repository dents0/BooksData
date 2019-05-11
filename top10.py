import sqlite3
import pandas as pd
import xlsxwriter

conn = sqlite3.connect("books.db")
c = conn.cursor()


def get_top_rated():
    '''Find top 10 books with the highest rating'''
    c.execute("SELECT * FROM books WHERE rating = 5 LIMIT 10")
    return c.fetchall()


# def get_average_price():
#     '''Find average price of all books in the DB'''
#     prices = c.execute("SELECT price FROM books").fetchall()
#     total = 0
#     for x in prices:
#         total += x[0]
#     average = round(total/len(prices), 2)
#     return f"{average} GBP"


def get_best_price():
    '''Find top 10 books with the lowest prices'''
    c.execute("SELECT * FROM books ORDER BY price LIMIT 10")
    return c.fetchall()


def get_recommended():
    '''Find 10 most affordable top-rated books'''
    c.execute("SELECT * FROM books WHERE rating = 5 ORDER BY price LIMIT 10")
    return c.fetchall()


def create_df(data_fn):
    '''Create a dataframe'''
    return pd.DataFrame({
        "Title": [x[0] for x in data_fn],
        "Price": [x[1] for x in data_fn],
        "Raiting": [x[2] for x in data_fn]
    })


def write_data_to_excel():
    '''Writes dataframes into an Excel file'''
    recommended_df = create_df(get_recommended())
    top_rated_df = create_df(get_top_rated())
    best_price_df = create_df(get_best_price())

    with pd.ExcelWriter("books_stats.xlsx", engine="xlsxwriter") as writer:
        recommended_df.to_excel(writer, sheet_name="Top 10", index=False, startrow=1)
        top_rated_df.to_excel(writer, sheet_name="Top 10", index=False, startrow=1, startcol=4)
        best_price_df.to_excel(writer, sheet_name="Top 10", index=False, startrow=1, startcol=8)

        # Adding headings above the dataframes
        workbook = xlsxwriter.Workbook(writer)
        merge_format = workbook.add_format()
        worksheet = writer.sheets["Top 10"]
        worksheet.merge_range("A1:C1", "RECOMMENDED", merge_format)
        worksheet.merge_range("E1:G1", "TOP RATED", merge_format)
        worksheet.merge_range("I1:K1", "BEST PRICE", merge_format)


write_data_to_excel()
