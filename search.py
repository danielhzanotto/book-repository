from tkinter import *


class Search:
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
                                        text="Title", value=1, variable=self.radio_state, command=self.radio_used)
        self.radiobutton2 = Radiobutton(self.window_search,
                                        text="Author", value=2, variable=self.radio_state, command=self.radio_used)
        self.radiobutton3 = Radiobutton(self.window_search,
                                        text="Keyword", value=3, variable=self.radio_state, command=self.radio_used)
        self.radiobutton4 = Radiobutton(self.window_search,
                                        text="Already Read", value=4, variable=self.radio_state, command=self.radio_used)
        self.radio_state_two = IntVar()
        self.radio_yes = Radiobutton(self.window_search,
                                     text="Yes", value=2, variable=self.radio_state_two)
        self.radio_no = Radiobutton(self.window_search,
                                    text="No", value=1, variable=self.radio_state_two)

        self.search_entry = Entry(self.window_search, width=60)

        self.search_button = Button(self.window_search, text="Search", command=self.search_book,
                                    highlightthickness=0, width=50)

        self.edit_button = Button(self.window_search, text="Edit", command=self.edit_book_func,
                                  highlightthickness=0)

        self.delete_button = Button(self.window_search, text="Delete", command=self.delete_book,
                                    highlightthickness=0)

        self.radiobutton1.grid(row=1, column=0)
        self.radiobutton2.grid(row=1, column=1)
        self.radiobutton3.grid(row=1, column=2)
        self.radiobutton4.grid(row=1, column=3)

        self.window_search.mainloop()

    def radio_used(self):
        self.search_method()
        self.window_search.update()

    def search_method(self):
        if int(self.radio_state.get()) == 4:
            self.search_entry.grid_forget()

            self.radio_yes.grid(row=2, column=0, columnspan=2)
            self.radio_no.grid(row=2, column=2, columnspan=2)
            self.search_button.grid(row=3, column=0, columnspan=4)

        else:
            self.radio_yes.grid_forget()
            self.radio_no.grid_forget()

            self.search_entry.grid(row=2, column=0, columnspan=4)
            self.search_button.grid(row=3, column=0, columnspan=4)

    def search_book(self):
        self.search_info = self.init.brain.get_search_books(self.radio_state.get(
        ), self.search_entry.get().title(), self.radio_state_two.get())

        self.init.catalog.show_info(self, self.search_info, self.window_search)

        self.book_list.grid(row=4, column=0, columnspan=4)
        self.edit_button.grid(row=5, column=0, columnspan=2)
        self.delete_button.grid(row=5, column=2, columnspan=2)

    def edit_book_func(self):
        self.book_input = self.list_input()
        self.book_selected = self.init.brain.get_book(self, self.book_input)
        self.window_search.destroy()
        self.init.edit(self.init, self.book_selected)

    def delete_book(self):
        self.delete_input = self.list_input()
        self.init.brain.delete_book(self, self.delete_input)
        self.window_search.destroy()
        self.init.refresh_window()

    def list_input(self):
        return int(self.book_list.get(self.book_list.curselection())[0])-1
