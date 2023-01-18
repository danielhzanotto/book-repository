import json
from tkinter import messagebox
import smtplib

EMAIL = "mmegaterio@gmail.com"
APIKEY = "nottheapikey"


class UserBrain:
    def __init__(self):
        pass

    def append_user(self, data):
        email = [value for value in data.values()][0]["email"]
        if "@" in email and ".com" in email:
            with open("users.json", mode="r+") as f:
                file = json.load(f)
                users = [user for user in list(file)]
                if str([key for key in data.keys()][0]) in users:
                    UserBrain.raise_user_duplicate(self)
                    return False
                else:
                    file.update(data)
                    f.seek(0)
                    json.dump(file, f)
                    return True

        else:
            UserBrain.raise_wrong_email(self)
            return False

    def check_user(self, data):
        with open("users.json", mode="r+") as f:
            file = json.load(f)
            for users in file:
                if users == data[0]:
                    if file[data[0]]["password"] == data[1]:
                        return True
                    else:
                        UserBrain.raise_wrong_pass(self)
                        return False
                else:
                    pass
            UserBrain.raise_wrong_user(self)
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
                        self.raise_successful_email()
                        return True
                    UserBrain.raise_invalid_email(self)
                    return False
        else:
            UserBrain.raise_wrong_email(self)
            return False

    def send_email(self, user):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=APIKEY)
            connection.sendmail(from_addr=EMAIL,
                                to_addrs=f"{user['email']}",
                                msg=f"Subject:Your Password\n\nYour BOOK CATALOG password is {user['password']}")

    def raise_user_duplicate(self):
        messagebox.showinfo(
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

    def raise_wrong_email(self):
        messagebox.showinfo(
            title="Oops", message="The email is not right, please provide a valid email")

    def raise_invalid_email(self):
        messagebox.showinfo(
            title="Oops", message="The email doesn't exist, please provide another email or create a new account.")

    def raise_successful_email(self):
        messagebox.showinfo(
            title="Email Sent", message="Check your email to recover your password.")
