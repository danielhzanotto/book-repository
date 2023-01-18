from tkinter import *
import random


class Append:
    def __init__(self, init):
        self.init = init

        self.window_three = Toplevel()
        self.window_three.title("Append Book")
        self.window_three.config(padx=20, pady=20)

        self.book_title_label = Label(self.window_three, text="Book Title:")
        self.book_title_label.grid(row=1, column=0)
        self.book_title_entry = Entry(self.window_three, width=40)
        self.book_title_entry.grid(row=1, column=1)

        self.book_search = Button(
            self.window_three, text="Search Book", highlightthickness=0, width=34, command=self.search_book)
        self.book_search.grid(row=2, column=1)

        self.author_label = Label(self.window_three, text="Author:")
        self.author_label.grid(row=3, column=0)
        self.author_entry = Entry(self.window_three, width=40)
        self.author_entry.grid(row=3, column=1)

        self.labels_label = Label(self.window_three, text="Keywords:")
        self.labels_label.grid(row=4, column=0)
        self.labels_entry = Entry(self.window_three, width=40)
        self.labels_entry.grid(row=4, column=1)

        self.checked_state = IntVar()
        self.already_read_check = Checkbutton(self.window_three,
                                              text="Already Read", variable=self.checked_state, command=self.checkbutton_used)
        self.already_read_check.grid(row=5, column=0)

        self.register = Button(self.window_three, text="Register Book", command=self.append_book,
                               highlightthickness=0, width=34)
        self.register.grid(row=5, column=1)

        self.window_three.mainloop()

    def checkbutton_used(self):
        print(self.checked_state.get())

    def search_book(self):
        self.init.brain.create_book(
            self.init.brain, self.book_title_entry.get())
        print(self.init.brain.book_dict)

        self.book_title_entry.delete(0, END)
        self.author_entry.delete(0, END)
        self.book_title_entry.insert(0, self.init.brain.book_dict["title"])
        self.author_entry.insert(0, self.init.brain.book_dict["author"])
        self.window_three.update()

    def append_book(self):
        if hasattr(self.init.brain, "book_dict"):
            book_key = self.init.brain.book_dict["key"]
        else:
            book_key = random.randint(1000, 99999)

        self.book_data = {

            "key": book_key,
            "title": self.book_title_entry.get().title(),
            "author": self.author_entry.get().title(),
            "keywords": self.labels_entry.get().title(),
            "already": self.checked_state.get()
        }

        self.init.brain.add_to_file(self, self.book_data)
        self.window_three.destroy()
        self.init.refresh_window()
