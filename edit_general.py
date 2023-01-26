from tkinter import *


class Edit:
    def __init__(self, init, data):
        self.init = init
        self.data = data

        self.window_edit_general = Toplevel()
        self.window_edit_general.title("Edit Book")
        self.window_edit_general.config(padx=20, pady=20)

        self.book_title_label = Label(
            self.window_edit_general, text="Book Title:")
        self.book_title_label.grid(row=1, column=0)
        self.book_title_entry = Entry(self.window_edit_general, width=40)
        self.book_title_entry.insert(0, self.data[2])
        self.book_title_entry.grid(row=1, column=1)

        self.author_label = Label(self.window_edit_general, text="Author:")
        self.author_label.grid(row=2, column=0)
        self.author_entry = Entry(self.window_edit_general, width=40)
        self.author_entry.insert(0, self.data[3])
        self.author_entry.grid(row=2, column=1)

        self.register = Button(self.window_edit_general, text="Edit Book", command=self.edit_book,
                               highlightthickness=0, width=34)
        self.register.grid(row=4, column=1)

        self.cancel_button = Button(self.window_edit_general, text="Cancel", command=self.cancel,
                                    highlightthickness=0)
        self.cancel_button.grid(row=4, column=0)

        self.window_edit_general.mainloop()

    def edit_book(self):
        self.book_data = {
            "key": self.data[1],
            "title": self.book_title_entry.get().title(),
            "author": self.author_entry.get().title(),
        }

        self.window_edit_general.destroy()
        self.init.brain.refresh_csv(self, self.book_data)
        self.init.refresh_window()

    def cancel(self):
        self.window_edit_general.destroy()
