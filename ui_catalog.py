from tkinter import *


class Catalog:
    def __init__(self):
        pass

    def show_info(self, info):

        for book in info.itertuples():

            self.book_index = Label(text=book[0], pady=10, padx=5)
            self.book_index.grid(row=book[0] + 2, column=0)

            self.book_title = Label(text=book[1], pady=10, padx=5)
            self.book_title.grid(row=book[0] + 2, column=1)

            self.book_author = Label(text=book[2], pady=10, padx=5)
            self.book_author.grid(row=book[0] + 2, column=2)

            self.book_labels = Label(text=book[3], pady=10, padx=5)
            self.book_labels.grid(row=book[0] + 2, column=3)

            if book[4] == 0:
                read = "X"
            else:
                read = "V"

            self.book_read = Label(text=read, pady=10, padx=5)
            self.book_read.grid(row=book[0] + 2, column=4)

            self.edit_book = Button(
                text="Edit Book", command=self.edit_book_func)
            self.edit_book.grid(row=book[0] + 2, column=5)
