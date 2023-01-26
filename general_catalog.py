from tkinter import *
from book_brain_general import Brain
from append import Append
from catalog import Catalog
from edit_general import Edit
from search_general import SearchGeneral


class General:
    def __init__(self, init, user):
        self.brain = Brain
        self.catalog = Catalog
        self.edit = Edit

        self.main = init
        self.user = user

        self.window_general = Toplevel()
        self.window_general.title("Catalog Consult")
        self.window_general.config(padx=20, pady=20)

        self.add_book_list = Button(self.window_general,
                                    text="Add Book to List", command=self.add_book, highlightthickness=0)
        self.add_book_list.grid(row=0, column=0)

        self.search_book_button = Button(self.window_general,
                                         text="Search Book", command=self.search_book, highlightthickness=0)
        self.search_book_button.grid(row=0, column=1)

        self.edit_book = Button(self.window_general,
                                text="Edit Book", command=self.edit_book_func, highlightthickness=0)
        self.edit_book.grid(row=0, column=2)

        self.append_button = Button(self.window_general,
                                    text="Create New Book", command=self.append_book, highlightthickness=0)
        self.append_button.grid(row=0, column=3)

        self.cancel_button = Button(self.window_general,
                                    text="Cancel", command=self.cancel, highlightthickness=0)
        self.cancel_button.grid(row=0, column=4)

        self.consult_cat = self.brain.consult_catalog(self)
        self.catalog.show_info(self, self.consult_cat, self.window_general)

        self.window_general.mainloop()

    def append_book(self):
        Append(self)

    def search_book(self):
        SearchGeneral(self)

    def edit_book_func(self):
        self.book_input = self.list_input()
        self.book_selected = self.brain.get_book(self, self.book_input)
        self.edit(self, self.book_selected)

    def refresh_window(self):
        data = self.brain.consult_catalog(self)
        self.catalog.show_info(self, data, self.window_general)
        self.window_general.update()

    def list_input(self):
        return int(self.book_list.get(self.book_list.curselection())[0])-1

    def add_book(self):
        self.book_input = self.list_input()
        self.book_selected = self.brain.get_book(self, self.book_input)
        self.book_user = self.brain.add_book_user(self.brain,
                                                  self.book_selected, self.user, self.window_general)

        if len(self.book_user) != 0:
            self.window_general.destroy()
            self.main.edit(self.main, self.book_user)
            self.main.refresh_window()

    def cancel(self):
        self.window_general.destroy()
