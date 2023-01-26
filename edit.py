from tkinter import *


class Edit:
    def __init__(self, init, data):
        self.init = init
        self.data = data

        self.window_two = Toplevel()
        self.window_two.title("Edit Book")
        self.window_two.config(padx=20, pady=20)

        self.book_title_label = Label(
            self.window_two, text=f"{self.data['title'].title()} ({self.data['author'].title()})")
        self.book_title_label.grid(row=0, column=0, columnspan=2)

        self.labels_label = Label(self.window_two, text="Keywords:")
        self.labels_label.grid(row=1, column=0)
        self.labels_entry = Text(self.window_two, width=43, height=3)
        self.labels_entry.insert(END, self.data['keywords'])
        self.labels_entry.grid(row=1, column=1, columnspan=2)

        self.score_label = Label(self.window_two, text="Score:")
        self.score_label.grid(row=2, column=0)

        self.scale_score = Scale(self.window_two,
                                 from_=0, to=10, command=self.scale_used, orient=HORIZONTAL, length=350)
        self.scale_score.grid(row=2, column=1, columnspan=2)
        self.scale_score.set(self.data['score'])

        self.checked_state = IntVar()
        self.already_read_check = Checkbutton(self.window_two,
                                              text="Already Read", variable=self.checked_state)
        self.already_read_check.grid(row=3, column=0)
        self.check_state()

        self.edit = Button(self.window_two, text="Save Book", command=self.edit_book,
                           highlightthickness=0, width=20)
        self.edit.grid(row=3, column=1)

        self.cancel_button = Button(self.window_two, text="Cancel", command=self.cancel,
                                    highlightthickness=0, width=20)
        self.cancel_button.grid(row=3, column=2)

        self.window_two.mainloop()

    def edit_book(self):
        if self.checked_state.get() == 0:
            score = 0
        elif self.checked_state.get() == 1 and self.scale_score.get() == 0:
            score = 1
        else:
            score = self.scale_score.get()

        self.book_data = {self.data["key"]: {
            "keywords": self.labels_entry.get(1.0, "end-1c").title(),
            "already": self.checked_state.get(),
            "score": score,
        }}
        print(self.book_data)
        self.window_two.destroy()
        self.init.brain.refresh_book_list(self, self.book_data, self.init.user)
        self.init.refresh_window()

    def check_state(self):
        if self.data["already"] == 0:
            self.already_read_check.deselect()
            self.scale_score.set(0)
        elif self.data["already"] == 1:
            self.already_read_check.select()
        else:
            pass

    def scale_used(self, value):
        self.book_score = value

    def cancel(self):
        self.window_two.destroy()
