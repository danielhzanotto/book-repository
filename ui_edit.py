from tkinter import *


class Edit:
    def __init__(self, init, data):
        self.init = init
        self.data = data

        self.window = Toplevel()
        self.window.title("Edit Book")
        self.window.config(padx=20, pady=20)

        self.book_title_label = Label(self.window, text="Book Title:")
        self.book_title_label.grid(row=1, column=0)
        self.book_title_entry = Entry(self.window, width=40)
        self.book_title_entry.insert(0, self.data[1])
        self.book_title_entry.grid(row=1, column=1)

        self.author_label = Label(self.window, text="Author:")
        self.author_label.grid(row=2, column=0)
        self.author_entry = Entry(self.window, width=40)
        self.author_entry.insert(0, self.data[2])
        self.author_entry.grid(row=2, column=1)

        self.labels_label = Label(self.window, text="Labels:")
        self.labels_label.grid(row=3, column=0)
        self.labels_entry = Entry(self.window, width=40)
        self.labels_entry.insert(0, self.data[3])
        self.labels_entry.grid(row=3, column=1)

        self.checked_state = IntVar()
        self.already_read_check = Checkbutton(self.window,
                                              text="Already Read", variable=self.checked_state, command=self.checkbutton_used)
        self.already_read_check.grid(row=5, column=0)

        self.register = Button(self.window, text="Edit Book", command=self.edit_book,
                               highlightthickness=0, width=34)
        self.register.grid(row=5, column=1)

        self.window.mainloop()

    def checkbutton_used(self):
        print(self.checked_state.get())

    def edit_book(self):
        self.book_data = [{
            "title": self.book_title_entry.get(),
            "author": self.author_entry.get(),
            "labels": self.labels_entry.get(),
            "read": self.checked_state.get()
        }]

        self.init.brain.refresh_csv(self, self.book_data)

        self.window.destroy()

        self.init.refresh_window()
