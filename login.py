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
        if valid == "validate":
            UserBrain.raise_invalid_account(self)
            Validation()
        elif valid == True:
            self.window_login.destroy()
            Init(user[0])

    def create_user_log(self):
        CreateUser()

    def checkbutton_login(self):
        UserBrain.checkbutton_used(self, self.checked_state,
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
            "validation-code": int(self.generate_validation_code()),
            "validate": 0,
            "books": {},
        }}
        success = UserBrain.append_user(self, self.user_data)
        if success:
            self.window_create.destroy()
            Validation()

    def checkbutton_create(self):
        UserBrain.checkbutton_used(self, self.checked_state,
                                   self.create_password_entry, self.window_create)

    def generate_validation_code(self):
        from random import randint
        code = ""
        while len(code) < 6:
            code += str(randint(0, 9))
        return code


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


class Validation:
    def __init__(self):
        self.window_validation = Toplevel()
        self.window_validation.title("Validation Code")
        self.window_validation.config(padx=20, pady=20)

        self.code_label = Label(self.window_validation,
                                text="Please enter your validation code: ")
        self.code_label.grid(row=0, column=0)

        self.code_entry = Entry(self.window_validation, width=40)
        self.code_entry.grid(row=0, column=1)

        self.code_button = Button(self.window_validation, text="Validate your account",
                                  command=self.validate_account, highlightthickness=0, width=34)
        self.code_button.grid(row=1, column=1)

        self.resend_label = Label(self.window_validation,
                                  text="Check if the email is at the spam box.\nIf you didn't recieve or lost your validation code,\nenter your email and click 'Send Code' to send again")
        self.resend_label.grid(row=2, column=0, columnspan=2)

        self.email_resend_entry = Entry(self.window_validation, width=40)
        self.email_resend_entry.grid(row=3, column=0)

        self.resend_button = Button(self.window_validation, text="Send Code",
                                    command=self.send_code_again, highlightthickness=0, width=34)
        self.resend_button.grid(row=3, column=1)

        self.window_validation.mainloop()

    def validate_account(self):
        self.code = self.code_entry.get()
        success = UserBrain.validate_user_account(self, self.code)
        if success:
            self.window_validation.destroy()

    def send_code_again(self):
        self.email_resend = self.email_resend_entry.get()
        UserBrain.send_new_code(self, self.email_resend)


Login()
