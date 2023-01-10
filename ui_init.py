from tkinter import *
from brain import Brain
from ui_append import Interface
from ui_catalog import Catalog
from ui_edit import Edit


class Consult:
    def __init__(self, brain: Brain):
        self.brain = Brain
        self.catalog = Catalog
        self.edit = Edit

        self.window_two = Tk()
        self.window_two.title("Catalog Consult")
        self.window_two.config(padx=20, pady=20)

        self.append_button = Button(
            text="Create New Book", command=self.append_book, highlightthickness=0)
        self.append_button.grid(row=0, column=0)

        self.edit_book = Button(
            text="Edit Book", command=self.edit_book_func, highlightthickness=0)
        self.edit_book.grid(row=0, column=1)

        self.delete_book = Button(
            text="Delete Book", command=self.delete_book_selected, highlightthickness=0)
        self.delete_book.grid(row=0, column=2)

        self.consult_cat = brain.consult_catalog()
        self.catalog.show_info(self, self.consult_cat)

        self.window_two.mainloop()

    def append_book(self):
        Interface(self)

    def edit_book_func(self):
        self.book_input = int(self.book_list.get(
            self.book_list.curselection())[0])-1
        book_selected = self.brain.get_book(self, self.book_input)

        self.edit(self, book_selected)

    def delete_book_selected(self):
        pass

    def refresh_window(self):
        data = self.brain.consult_catalog(self)
        self.catalog.show_info(self, data)
        self.window_two.update()
