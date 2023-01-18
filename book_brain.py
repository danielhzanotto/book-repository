import requests
from bs4 import BeautifulSoup
import pandas as pd


class Brain:
    def __init__(self):
        pass

    def create_book(self, input_book):
        search_input = input_book
        search_parse = search_input.replace(" ", "+").lower()

        search_page = requests.get(
            f'https://openlibrary.org/search?q=title%3A+"{search_parse}"&mode=everything')
        search_page.raise_for_status()

        soup = BeautifulSoup(search_page.text, "html.parser")
        book_div = soup.find(id="searchResults")
        book_link = book_div.span.a["href"].split("?")[0]
        book_OLID = book_link.split("/")[-1]

        response = requests.get(
            f"https://openlibrary.org/book/{book_OLID}.json")
        response.raise_for_status()
        self.book = response.json()
        self.author = self.get_author_name(self, self.book)
        self.book_dict = self.create_dict(self, self.book, self.author)

    def get_author_name(self, book_link):
        author_link = book_link["authors"][0]["author"]["key"]
        author_request = requests.get(
            f"https://openlibrary.org{author_link}.json")
        author_request.raise_for_status()
        return author_request.json()

    def create_dict(self, book, author):
        return {
            "key": book["key"].split("/")[-1],
            "title": book["title"],
            "author": author["name"],
            "keywords": "",
            "already": 0
        }

    def add_to_file(self, book):
        book_obj = pd.DataFrame([book])
        book_obj.to_csv("books.csv", mode="a", index=False, header=False)

    def consult_catalog(self):
        return pd.read_csv("books.csv")

    def get_book(self, book_input):
        df = pd.read_csv("books.csv")
        for book in df.itertuples():
            if book[0] == book_input:
                book_index = book
        return book_index

    def refresh_csv(self, book_data):
        df = pd.read_csv("books.csv")
        for book in df.itertuples():
            if book[1] == book_data["key"]:
                print("ok")
                df.loc[book[0], "title"] = book_data["title"]
                df.loc[book[0], "author"] = book_data["author"]
                df.loc[book[0], "keywords"] = book_data["keywords"]
                df.loc[book[0], "already"] = book_data["already"]
                df.to_csv("books.csv", mode="w", index=False, header=True)

    def delete_book(self, index):
        df = pd.read_csv("books.csv")
        df.drop(int(index), axis=0, inplace=True)
        df.to_csv("books.csv", mode="w", index=False, header=True)

    def get_search_books(value, search, read):
        df = pd.read_csv("books.csv")
        if value == 1:
            df_2 = df[df["title"].str.contains(search)]
        elif value == 2:
            df_2 = df[df["author"].str.contains(search)]
        elif value == 3:
            df_2 = df[df["keywords"].str.contains(search)]
        elif value == 4:
            df_2 = df[df["already"] == read - 1]
        return df_2
