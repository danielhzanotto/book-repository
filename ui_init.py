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
        self.append_button.grid(row=0, column=0)

        self.edit_book = Button(
            text="Edit Book", command=self.edit_book_func, highlightthickness=0)
        self.edit_book.grid(row=0, column=1)

        self.consult_cat = brain.consult_catalog()
        self.catalog.show_info(self, self.consult_cat)

        self.window_two.mainloop()

    def append_book(self):
        Interface(self.brain, self)

    def edit_book_func(self):
        self.book_input = int(self.book_list.get(
            self.book_list.curselection())[0])-1
        self.brain.edit_book(self, self.book_input)
