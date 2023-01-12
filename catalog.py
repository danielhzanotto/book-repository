from tkinter import *


class Catalog:
    def __init__(self):
        pass

    def show_info(self, info, screen):
        self.book_list = Listbox(master=screen, height=6, width=60)
        self.book_list.grid(row=4, column=0, columnspan=4)

        for book in info.itertuples():

            if book[4] == 0:
                read = "X"
            else:
                read = "V"

            self.book_list.insert(
                book[0], f"{book[0]+1}: {book[2]} ({book[3]})")
