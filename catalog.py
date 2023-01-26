from tkinter import *


class Catalog:
    def __init__(self):
        pass

    def show_info(self, info, screen):
        self.book_list = Listbox(master=screen, height=10, width=80)
        self.book_list.grid(row=4, column=0, columnspan=5)

        for book in info.itertuples():
            self.book_list.insert(
                book[0], f"{book[0]+1}: {book[2]} ({book[3]})")

    def show_list(self, info, screen):
        self.book_list = Listbox(master=screen, height=10, width=80)
        self.book_list.grid(row=4, column=0, columnspan=5)

        for book in info.values():
            if book["already"] == 0:
                read = "X"
                book['score'] = "?"
            elif book["already"] == 1:
                read = "V"

            self.book_list.insert(
                book['index'], f"[{read}]: {book['title']} ({book['author']})   SCORE: {book['score']}/10")

    def show_search_list(self, info, screen):
        self.book_list = Listbox(master=screen, height=10, width=80)
        self.book_list.grid(row=4, column=0, columnspan=5)

        for book in info:
            book_info = list(book.items())[0][1]

            if book_info["already"] == 0:
                read = "X"
                book_info['score'] = "?"
            elif book_info["already"] == 1:
                read = "V"

            self.book_list.insert(
                book_info['index'], f"[{read}]: {book_info['title']} ({book_info['author']})   SCORE: {book_info['score']}/10")
