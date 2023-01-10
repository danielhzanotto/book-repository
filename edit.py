from tkinter import *


class Edit:
    def __init__(self, init, data):
        self.init = init
        self.data = data

        self.window_two = Toplevel()
        self.window_two.title("Edit Book")
        self.window_two.config(padx=20, pady=20)

        self.book_title_label = Label(self.window_two, text="Book Title:")
        self.book_title_label.grid(row=1, column=0)
        self.book_title_entry = Entry(self.window_two, width=40)
        self.book_title_entry.insert(0, self.data[1])
        self.book_title_entry.grid(row=1, column=1)

        self.author_label = Label(self.window_two, text="Author:")
        self.author_label.grid(row=2, column=0)
        self.author_entry = Entry(self.window_two, width=40)
        self.author_entry.insert(0, self.data[2])
        self.author_entry.grid(row=2, column=1)

        self.labels_label = Label(self.window_two, text="Category:")
        self.labels_label.grid(row=3, column=0)
        self.labels_entry = Entry(self.window_two, width=40)
        self.labels_entry.insert(0, self.data[3])
        self.labels_entry.grid(row=3, column=1)

        self.checked_state = IntVar()
        self.already_read_check = Checkbutton(self.window_two,
                                              text="Already Read", variable=self.checked_state, command=self.checkbutton_used)
        self.already_read_check.grid(row=5, column=0)
        self.check_state()
        self.register = Button(self.window_two, text="Edit Book", command=self.edit_book,
                               highlightthickness=0, width=34)
        self.register.grid(row=5, column=1)

        self.window_two.mainloop()

    def checkbutton_used(self):
        print(self.checked_state.get())

    def edit_book(self):
        self.book_data = [{
            "title": self.book_title_entry.get().title(),
            "author": self.author_entry.get().upper(),
            "labels": self.labels_entry.get().title(),
            "read": self.checked_state.get()
        }]

        self.init.brain.refresh_csv(self, self.book_data)

        self.window_two.destroy()

        self.init.refresh_window()

    def check_state(self):
        if self.data[4] == 0:
            self.already_read_check.deselect()
        elif self.data[4] == 1:
            self.already_read_check.select()
        else:
            pass
