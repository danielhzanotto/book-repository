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
        self.radiobutton5 = Radiobutton(self.window_search,
                                        text="Score", value=5, variable=self.radio_state, command=self.radio_used)
        self.radio_state_two = IntVar()
        self.radio_yes = Radiobutton(self.window_search,
                                     text="Yes", value=1, variable=self.radio_state_two)
        self.radio_no = Radiobutton(self.window_search,
                                    text="No", value=0, variable=self.radio_state_two)

        self.search_entry = Entry(self.window_search, width=60)

        self.score_scale = Scale(self.window_search, from_=1, to=10,
                                 command=self.scale, orient=HORIZONTAL, length=350)

        self.search_button = Button(self.window_search, text="Search", command=self.search_book,
                                    highlightthickness=0, width=50)

        self.edit_button = Button(
            self.window_search, text="Edit", command=self.edit_book_func, highlightthickness=0, width=30)

        self.remove_button = Button(
            self.window_search, text="Remove", command=self.remove_book, highlightthickness=0, width=30)

        self.cancel_button = Button(
            self.window_search, text="Cancel", command=self.cancel, highlightthickness=0)
        self.cancel_button.grid(row=5, column=0)

        self.radiobutton1.grid(row=1, column=0)
        self.radiobutton2.grid(row=1, column=1)
        self.radiobutton3.grid(row=1, column=2)
        self.radiobutton4.grid(row=1, column=3)
        self.radiobutton5.grid(row=1, column=4)

        self.window_search.mainloop()

    def radio_used(self):
        self.search_method()
        self.window_search.update()

    def search_method(self):
        if int(self.radio_state.get()) == 4:
            self.search_entry.grid_forget()
            self.score_scale.grid_forget()

            self.radio_yes.grid(row=2, column=0, columnspan=2)
            self.radio_no.grid(row=2, column=2, columnspan=2)
            self.search_button.grid(row=3, column=0, columnspan=5)

        elif int(self.radio_state.get()) == 5:
            self.search_entry.grid_forget()
            self.radio_yes.grid_forget()
            self.radio_no.grid_forget()

            self.score_scale.grid(row=2, column=0, columnspan=5)
            self.search_button.grid(row=3, column=0, columnspan=5)

        else:
            self.radio_yes.grid_forget()
            self.radio_no.grid_forget()
            self.score_scale.grid_forget()

            self.search_entry.grid(row=2, column=0, columnspan=5)
            self.search_button.grid(row=3, column=0, columnspan=5)

    def search_book(self):
        self.search_info = self.init.brain.get_search_books(self.init.brain, self.radio_state.get(
        ), self.search_entry.get().title(), self.radio_state_two.get(), self.score_scale.get(), self.init.user)

        self.init.catalog.show_search_list(
            self, self.search_info, self.window_search)

        self.book_list.grid(row=4, column=0, columnspan=5)
        self.edit_button.grid(row=5, column=1, columnspan=2)
        self.remove_button.grid(row=5, column=3, columnspan=2)

    def edit_book_func(self):
        self.book_input = self.list_input()
        self.book_selected = self.init.brain.get_book_info(
            self, self.book_input, self.init.user)
        self.window_search.destroy()
        self.init.edit(self.init, self.book_selected)

    def remove_book(self):
        self.remove_input = self.list_input()
        self.init.brain.remove_book(self, self.remove_input, self.init.user)
        self.window_search.destroy()
        self.init.refresh_window()

    def list_input(self):
        selection = self.book_list.get(self.book_list.curselection())
        return selection.split(":")[1].split("(")[0].strip()

    def scale(self, value):
        self.scale_value = value

    def cancel(self):
        self.window_search.destroy()
