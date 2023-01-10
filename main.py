from tkinter import *
from brain import Brain
from append import Append
from catalog import Catalog
from edit import Edit


class Init:
    def __init__(self):
        self.brain = Brain
        self.catalog = Catalog
        self.edit = Edit

        self.window = Tk()
        self.window.title("Catalog Consult")
        self.window.config(padx=20, pady=20)

        self.append_button = Button(
            text="Create New Book", command=self.append_book, highlightthickness=0)
        self.append_button.grid(row=0, column=0)

        self.edit_book = Button(
            text="Edit Book", command=self.edit_book_func, highlightthickness=0)
        self.edit_book.grid(row=0, column=1)

        self.delete_book = Button(
            text="Delete Book", command=self.delete_book_selected, highlightthickness=0)
        self.delete_book.grid(row=0, column=2)

        self.consult_cat = self.brain.consult_catalog(self)
        self.catalog.show_info(self, self.consult_cat)

        self.window.mainloop()

    def append_book(self):
        Append(self)

    def edit_book_func(self):
        self.book_input = self.list_input()
        book_selected = self.brain.get_book(self, self.book_input)
        self.edit(self, book_selected)

    def delete_book_selected(self):
        self.book_input = self.list_input()
        self.brain.delete_book(self, self.book_input)
        self.refresh_window()

    def refresh_window(self):
        data = self.brain.consult_catalog(self)
        self.catalog.show_info(self, data)
        self.window.update()

    def list_input(self):
        return int(self.book_list.get(self.book_list.curselection())[0])-1


catalog = Init()
