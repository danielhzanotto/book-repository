from tkinter import *
from list_brain import Brain
from catalog import Catalog
from edit import Edit
from search import Search
from general_catalog import General


class Init:
    def __init__(self, user):
        self.user = user
        self.brain = Brain
        self.catalog = Catalog
        self.edit = Edit

        self.window = Tk()
        self.window.title(f"{self.user.title()}'s books")
        self.window.config(padx=20, pady=20)

        self.add_button = Button(self.window,
                                 text="Add New Book", command=self.add_book, highlightthickness=0)
        self.add_button.grid(row=0, column=0)

        self.remove_book = Button(self.window,
                                  text="Remove Book", command=self.remove_book_selected, highlightthickness=0)
        self.remove_book.grid(row=0, column=1)

        self.edit_book = Button(self.window,
                                text="Edit Book", command=self.edit_book_func, highlightthickness=0)
        self.edit_book.grid(row=0, column=2)

        self.search_book_button = Button(self.window,
                                         text="Search Books", command=self.search_book, highlightthickness=0)
        self.search_book_button.grid(row=0, column=3)

        self.show_list()

        self.window.mainloop()

    def add_book(self):
        General(self, self.user)

    def search_book(self):
        Search(self)

    def edit_book_func(self):
        self.book_input = self.list_input()
        self.book_selected = self.brain.get_book_info(
            self, self.book_input, self.user)
        self.edit(self, self.book_selected)

    def remove_book_selected(self):
        self.book_input = self.list_input()
        self.brain.remove_book(self, self.book_input, self.user)
        self.refresh_window()

    def show_list(self):
        self.list = self.brain.consult_user_list(self, self.user)
        self.catalog.show_list(self, self.list, self.window)

    def refresh_window(self):
        self.show_list()
        self.window.update()

    def list_input(self):
        selection = self.book_list.get(self.book_list.curselection())
        return selection.split(":")[1].split("(")[0].strip()
