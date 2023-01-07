from tkinter import *
from brain import Brain
from ui_consult import Consult


class Interface:
    def __init__(self, brain: Brain):
        self.brain = brain

        self.window = Tk()
        self.window.title("Book Catalog")
        self.window.config(padx=20, pady=20)

        self.book_title_label = Label(text="Book Title:")
        self.book_title_label.grid(row=1, column=0)
        self.book_title_entry = Entry(width=40)
        self.book_title_entry.grid(row=1, column=1)

        self.author_label = Label(text="Author:")
        self.author_label.grid(row=2, column=0)
        self.author_entry = Entry(width=40)
        self.author_entry.grid(row=2, column=1)

        self.labels_label = Label(text="Labels:")
        self.labels_label.grid(row=3, column=0)
        self.labels_entry = Entry(width=40)
        self.labels_entry.grid(row=3, column=1)

        self.checked_state = IntVar()
        self.already_read_check = Checkbutton(
            text="Already Read", variable=self.checked_state, command=self.checkbutton_used)
        self.already_read_check.grid(row=5, column=0)

        self.register = Button(text="Register Book", command=self.append_book,
                               highlightthickness=0, width=34)
        self.register.grid(row=5, column=1)

        self.consult_books = Button(text="Consult All Books", command=self.consult_all,
                                    highlightthickness=0, width=34)
        self.consult_books.grid(row=6, column=1)

        self.window.mainloop()

    def checkbutton_used(self):
        print(self.checked_state.get())

    def append_book(self):
        self.book_data = [{
            "title": self.book_title_entry.get(),
            "author": self.author_entry.get(),
            "labels": self.labels_entry.get(),
            "read": self.checked_state.get()
        }]

        self.brain.append_new_book(self.book_data)

    def consult_all(self):
        Consult()


# book title
# book author
# read?
# comments
