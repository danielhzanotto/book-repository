from tkinter import *
from user_brain import UserBrain
from main import Init


class Login:
    def __init__(self):

        self.window_login = Tk()
        self.window_login.title("Login")
        self.window_login.config(padx=20, pady=20)

        self.user_label = Label(text="User Name: ")
        self.user_label.grid(row=0, column=0)

        self.user_entry = Entry(width=40)
        self.user_entry.grid(row=0, column=1)

        self.password_label = Label(text="Password: ")
        self.password_label.grid(row=1, column=0)

        self.password_entry = Entry(show="*", width=40)
        self.password_entry.grid(row=1, column=1)

        self.checked_state = IntVar()
        self.see_password = Checkbutton(
            text="See password", variable=self.checked_state, command=self.checkbutton_login)
        self.see_password.grid(row=1, column=2)

        self.forgot_pass = Button(
            text="Forgot Password", command=self.recover_pass, highlightthickness=0)
        self.forgot_pass.grid(row=2, column=2)

        self.login_button = Button(
            text="Login", command=self.login_user, highlightthickness=0, width=34)
        self.login_button.grid(row=2, column=1)

        self.create_button = Button(
            text="Create User", command=self.create_user_log, highlightthickness=0, width=34)
        self.create_button.grid(row=3, column=1)

        self.window_login.mainloop()

    def recover_pass(self):
        Recover()

    def login_user(self):
        if len(self.user_entry.get()) == 0:
            UserBrain.raise_user_empty(self)
        elif len(self.password_entry.get()) == 0:
            UserBrain.raise_pass_empty(self)
        else:
            user = [self.user_entry.get(), self.password_entry.get()]
            valid = UserBrain.check_user(self, user)
        if valid:
            self.window_login.destroy()
            Init()

    def create_user_log(self):
        CreateUser()

    def checkbutton_login(self):
        Func.checkbutton_used(self, self.checked_state,
                              self.password_entry, self.window_login)


class CreateUser:
    def __init__(self):

        self.window_create = Toplevel()
        self.window_create.title("Create User")
        self.window_create.config(padx=20, pady=20)

        self.create_user_label = Label(self.window_create, text="User Name: ")
        self.create_user_label.grid(row=0, column=0)

        self.create_user_entry = Entry(self.window_create, width=40)
        self.create_user_entry.grid(row=0, column=1)

        self.create_password_label = Label(
            self.window_create, text="Password: ")
        self.create_password_label.grid(row=1, column=0)

        self.create_password_entry = Entry(
            self.window_create, show="*", width=40)
        self.create_password_entry.grid(row=1, column=1)

        self.checked_state = IntVar()
        self.create_see_password = Checkbutton(self.window_create,
                                               text="See password", variable=self.checked_state, command=self.checkbutton_create)
        self.create_see_password.grid(row=1, column=2)

        self.email_label = Label(self.window_create, text="Email: ")
        self.email_label.grid(row=2, column=0)

        self.email_entry = Entry(self.window_create, width=40)
        self.email_entry.grid(row=2, column=1)

        self.create_button = Button(self.window_create,
                                    text="Create User", command=self.create_user, highlightthickness=0, width=34)
        self.create_button.grid(row=3, column=1)

        self.window_create.mainloop()

    def create_user(self):

        self.user_data = {self.create_user_entry.get(): {
            "password": self.create_password_entry.get(),
            "email": self.email_entry.get(),
            "books": []
        }}
        success = UserBrain.append_user(self, self.user_data)
        if success:
            self.window_create.destroy()

    def checkbutton_create(self):
        Func.checkbutton_used(self, self.checked_state,
                              self.create_password_entry, self.window_create)


class Recover:
    def __init__(self):
        self.window_recover = Toplevel()
        self.window_recover.title("Recover Passoword")
        self.window_recover.config(padx=20, pady=20)

        self.email_recover_label = Label(
            self.window_recover, text="Enter your email: ")
        self.email_recover_label.grid(row=0, column=0)

        self.email_recover_entry = Entry(self.window_recover, width=40)
        self.email_recover_entry.grid(row=0, column=1)

        self.recover_password_button = Button(self.window_recover,
                                              text="Recover Password", command=self.recover_password, highlightthickness=0, width=34)
        self.recover_password_button.grid(row=1, column=1)

    def recover_password(self):
        success = UserBrain.check_email(self, self.email_recover_entry.get())
        if success:
            self.window_recover.destroy()


class Func:
    def __init__(self):
        pass

    def checkbutton_used(self, state, entry, window):
        if state.get() == 0:
            entry.config(show="*")
        elif state.get() == 1:
            entry.config(show="")
        window.update()


Login()
