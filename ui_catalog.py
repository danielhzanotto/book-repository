from tkinter import *


class Catalog:
    def __init__(self):
        pass

    def show_info(self, info):
        self.book_list = Listbox(height=5, width=40)
        self.book_list.grid(row=1, column=0, columnspan=3)

        for book in info.itertuples():

            if book[4] == 0:
                read = "X"
            else:
                read = "V"

            self.book_list.insert(
                book[0], f"{book[0]+1}: {book[1]} ({book[2]})")
