import json
from tkinter import messagebox
import smtplib

EMAIL = "email@gmail.com"
APIKEY = "notemailkey"


class UserBrain:
    def __init__(self):
        pass

    def append_user(self, data):
        email = list(data.values())[0]["email"]
        name = list(data.keys())[0]
        password = list(data.values())[0]["password"]
        if len(name) != 0 and len(password) != 0:
            if "@" in email and ".com" in email:
                with open("users.json", mode="r+") as f:
                    file = json.load(f)
                    for users in file:
                        if name == users:
                            UserBrain.raise_user_duplicate(self)
                            return False
                        else:
                            file.update(data)
                            f.truncate(0)
                            f.seek(0)
                            json.dump(file, f)
                            UserBrain.raise_user_requested(self)
                            UserBrain.send_email_code(
                                self, list(data.values())[0])
                            return True
            else:
                UserBrain.raise_wrong_email(self, self.window_create)
                return False
        else:
            UserBrain.raise_empty_field(self)
            return False

    def check_user(self, data):
        with open("users.json", mode="r+") as f:
            file = json.load(f)
            for users in file:
                if users == data[0]:
                    if file[data[0]]["validate"] == 1:
                        if file[data[0]]["password"] == data[1]:
                            return True
                        else:
                            UserBrain.raise_wrong_pass(self)
                            return False
                    elif file[data[0]]["validate"] == 0:
                        return "validate"
                else:
                    pass
            UserBrain.raise_wrong_user(self)
            return False

    def validate_user_account(self, code):
        if len(code) != 0 and code.isnumeric():
            self.code = int(code)
            with open("users.json", mode="r+") as f:
                file = json.load(f)
                for user in file.values():
                    if user["validation-code"] != self.code:
                        continue
                    elif user["validation-code"] == self.code:
                        user["validate"] = 1
                        f.truncate(0)
                        f.seek(0)
                        json.dump(file, f)
                        UserBrain.raise_valid_account(self)
                        return True
                    UserBrain.raise_invalid_code(self)
                    return False
        else:
            UserBrain.raise_invalid_code(self)
            return False

    def check_email(self, email):
        if "@" in email and ".com" in email:
            with open("users.json", mode="r+") as f:
                file = json.load(f)
                for user in file.values():
                    if user["email"] != email:
                        continue
                    elif user["email"] == email:
                        UserBrain.send_email(self, user)
                        UserBrain.raise_successful_email(
                            self, self.window_recover)
                        return True
                    UserBrain.raise_invalid_email(self, self.window_recover)
                    return False
        else:
            UserBrain.raise_wrong_email(self, self.window_recover)
            return False

    def send_new_code(self, email):
        if "@" in email and ".com" in email:
            with open("users.json", mode="r+") as f:
                file = json.load(f)
                for user in file.values():
                    if user["email"] != email:
                        continue
                    elif user["email"] == email:
                        UserBrain.send_email_code(self, user)
                        UserBrain.raise_successful_email(
                            self, self.window_validation)
                        return True
                    UserBrain.raise_invalid_email(self, self.window_validation)
                    return False
        else:
            UserBrain.raise_wrong_email(self, self.window_validation)
            return False

    def send_email(self, user):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=APIKEY)
            connection.sendmail(from_addr=EMAIL,
                                to_addrs=f"{user['email']}",
                                msg=f"Subject:Your Password\n\nYour BOOK CATALOG password is {user['password']}")

    def send_email_code(self, user):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=APIKEY)
            connection.sendmail(from_addr=EMAIL,
                                to_addrs=f"{user['email']}",
                                msg=f"Subject:Your Validation Code\n\nYour BOOK CATALOG validation code is {user['validation-code']}")

    def checkbutton_used(self, state, entry, window):
        if state.get() == 0:
            entry.config(show="*")
        elif state.get() == 1:
            entry.config(show="")
        window.update()

    def raise_user_duplicate(self):
        messagebox.showinfo(parent=self.window_create,
                            title="Oops", message="The username already exists! Try another username")

    def raise_user_empty(self):
        messagebox.showinfo(
            title="Oops", message="The username is empty! Please provide a valid input")

    def raise_pass_empty(self):
        messagebox.showinfo(
            title="Oops", message="The password is empty! Please provide a valid input")

    def raise_wrong_user(self):
        messagebox.showinfo(
            title="Oops", message="This user doesn't exist! Please check it or create new user")

    def raise_wrong_pass(self):
        messagebox.showinfo(
            title="Oops", message="The password is wrong, please try again or click on Forgot Password")

    def raise_wrong_email(self, window):
        messagebox.showinfo(parent=window,
                            title="Oops", message="The email is not right, please provide a valid email")

    def raise_invalid_email(self, window):
        messagebox.showinfo(parent=window,
                            title="Oops", message="The email doesn't exist, please provide another email or create a new account.")

    def raise_successful_email(self, window):
        messagebox.showinfo(parent=window,
                            title="Email Sent", message="Check your email to recover your password.")

    def raise_empty_field(self):
        messagebox.showinfo(parent=self.window_create,
                            title="Oops", message="You left something empty. Please fill all fields")

    def raise_valid_account(self):
        messagebox.showinfo(parent=self.window_validation,
                            title="Confirmed!", message="Your account has been activated! It's ready to be used.")

    def raise_invalid_code(self):
        messagebox.showinfo(parent=self.window_validation,
                            title="Invalid Code", message="Please insert a valid input")

    def raise_user_requested(self):
        messagebox.showinfo(parent=self.window_create,
                            title="Email Sent", message="We just sent you an email with your validation code! Please check the spambox")

    def raise_invalid_account(self):
        messagebox.showinfo(parent=self.window_login,
                            title="Account not Activated", message="We saw that you haven't activated your account, please activate now.")
