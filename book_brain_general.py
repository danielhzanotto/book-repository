from bs4 import BeautifulSoup
import pandas as pd
import requests
from tkinter import messagebox


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
            "author": author["name"]
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
                df.to_csv("books.csv", mode="w", index=False, header=True)

    def get_search_books(value, search):
        df = pd.read_csv("books.csv")
        if value == 1:
            df_2 = df[df["title"].str.contains(search)]
        elif value == 2:
            df_2 = df[df["author"].str.contains(search)]
        return df_2

    def add_book_user(self, book, user, window):
        users = pd.read_json("users.json")
        if book[1] in users[user]["books"]:
            self.raise_book_already(self, window)
            return ""
        else:
            users[user]["books"][book[1]] = {
                "keywords": "", "already": 0, "score": 0}
            users.to_json("users.json")
            return {"key": book[1], "title": book[2], "author": book[3], "keywords": "", "already": 0, "score": 0}

    def raise_book_already(self, window):
        messagebox.showinfo(parent=window,
                            title="Oops", message="You already have this book in your list!")

    def get_repeated_keys(key):
        df = pd.read_csv("books.csv")
        repeat = [str(k) for k in df["key"] if str(k) == key]
        if len(repeat) == 0:
            return False
        else:
            return True
