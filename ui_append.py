from tkinter import *


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

        self.author_label = Label(self.window_three, text="Author:")
        self.author_label.grid(row=2, column=0)
        self.author_entry = Entry(self.window_three, width=40)
        self.author_entry.grid(row=2, column=1)

        self.labels_label = Label(self.window_three, text="Labels:")
        self.labels_label.grid(row=3, column=0)
        self.labels_entry = Entry(self.window_three, width=40)
        self.labels_entry.grid(row=3, column=1)

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

    def append_book(self):
        self.book_data = [{
            "title": self.book_title_entry.get().title(),
            "author": self.author_entry.get().upper(),
            "labels": self.labels_entry.get().title(),
            "read": self.checked_state.get()
        }]

        self.init.brain.append_new_book(self, self.book_data)

        self.window_three.destroy()

        self.init.refresh_window()
