from tkinter import *
from brain import Brain
from ui_append import Interface
from ui_catalog import Catalog


class Consult:
    def __init__(self, brain: Brain):
        self.brain = Brain
        self.catalog = Catalog

        self.window_two = Tk()
        self.window_two.title("Catalog Consult")
        self.window_two.config(padx=20, pady=20)

        self.append_button = Button(
            text="Create New Book", command=self.append_book, highlightthickness=0)
        self.append_button.grid(row=0, column=0, columnspan=4)

        self.book_index = Label(text="Book Index", pady=10, padx=5)
        self.book_index.grid(row=1, column=0)

        self.book_title = Label(text="Book Title", pady=10, padx=5)
        self.book_title.grid(row=1, column=1)

        self.book_author = Label(text="Book Author", pady=10, padx=5)
        self.book_author.grid(row=1, column=2)

        self.book_labels = Label(text="Book Labels", pady=10, padx=5)
        self.book_labels.grid(row=1, column=3)

        self.book_read = Label(text="Already Read", pady=10, padx=5)
        self.book_read.grid(row=1, column=4)

        self.consult_cat = brain.consult_catalog()
        self.catalog.show_info(self, self.consult_cat)

        self.window_two.mainloop()

    def append_book(self):
        Interface(self.brain, self)

    def edit_book_func(self):
        pass
