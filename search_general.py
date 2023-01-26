from tkinter import *


class SearchGeneral:
    def __init__(self, init):
        self.init = init

        self.window_search = Toplevel()
        self.window_search.title("Search")
        self.window_search.config(padx=20, pady=20)

        self.select_label = Label(
            self.window_search, text="Select category:", width=50)
        self.select_label.grid(row=0, column=0, columnspan=4)

        self.radio_state = IntVar()
        self.radiobutton1 = Radiobutton(self.window_search,
                                        text="Title", value=1, variable=self.radio_state)
        self.radiobutton2 = Radiobutton(self.window_search,
                                        text="Author", value=2, variable=self.radio_state)

        self.search_entry = Entry(self.window_search, width=60)

        self.search_button = Button(self.window_search, text="Search", command=self.search_book,
                                    highlightthickness=0, width=40)

        self.cancel_button = Button(self.window_search, text="Cancel", command=self.cancel,
                                    highlightthickness=0, width=10)

        self.edit_button = Button(self.window_search, text="Edit Book", command=self.edit_book_func,
                                  highlightthickness=0, width=25)

        self.add_button = Button(
            self.window_search, text="Add Book to List", command=self.add_book_func, highlightthickness=0, width=25)

        self.radiobutton1.grid(row=1, column=0, columnspan=2)
        self.radiobutton2.grid(row=1, column=2, columnspan=2)
        self.search_entry.grid(row=2, column=0, columnspan=4)
        self.search_button.grid(row=3, column=0, columnspan=3)
        self.cancel_button.grid(row=3, column=3)

        self.window_search.mainloop()

    def search_book(self):
        self.search_info = self.init.brain.get_search_books(self.radio_state.get(
        ), self.search_entry.get().title())

        self.init.catalog.show_info(self, self.search_info, self.window_search)

        self.book_list.grid(row=4, column=0, columnspan=4)
        self.edit_button.grid(row=5, column=2, columnspan=2)
        self.add_button.grid(row=5, column=0, columnspan=2)

    def edit_book_func(self):

        self.book_input = self.list_input()
        self.book_selected = self.init.brain.get_book(self, self.book_input)
        self.window_search.destroy()
        self.init.edit(self.init, self.book_selected)

    def add_book_func(self):
        self.book_input = self.list_input()
        self.book_selected = self.init.brain.get_book(
            self.init, self.book_input)
        self.book_user = self.init.brain.add_book_user(self.init.brain,
            self.book_selected, self.init.user, self.window_search)
        if len(self.book_user) != 0:
            self.init.window_general.destroy()
            self.window_search.destroy()
            self.init.main.edit(self.init.main, self.book_user)
            self.init.main.refresh_window()

    def list_input(self):
        return int(self.book_list.get(self.book_list.curselection())[0])-1

    def cancel(self):
        self.window_search.destroy()
