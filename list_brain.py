import pandas as pd
import json


class Brain:
    def __init__(self):
        pass


# --------------------------------------------------------------------------


    def get_search_books(self, value, search, read, score, user):
        books = self.consult_user_list(self, user)

        if value == 1:
            result = [{key: values} for key,
                      values in books.items() if search in values["title"]]
        elif value == 2:
            result = [{key: values} for key,
                      values in books.items() if search in values["author"]]
        elif value == 3:
            result = [{key: values} for key,
                      values in books.items() if search in values["keywords"]]
        elif value == 4:
            result = [{key: values} for key,
                      values in books.items() if read == values["already"]]
        elif value == 5:
            result = [{key: values} for key,
                      values in books.items() if int(score) == values["score"]]
        return result

    def remove_book(self, name, user):
        df = pd.read_csv("books.csv")
        for book in df.itertuples():
            if name == book[2]:
                with open("users.json", "r+") as f:
                    users = json.load(f)
                    users[user]["books"].pop(book[1])
                    f.truncate(0)
                    f.seek(0)
                    json.dump(users, f)

    def consult_user_list(self, user):
        users = pd.read_json("users.json")
        user_list = users[user]["books"]
        books = pd.read_csv("books.csv")
        for book in user_list:
            for b in books.itertuples():
                if book == b[1]:
                    user_list[book]["title"] = b[2]
                    user_list[book]["author"] = b[3]
                    user_list[book]["index"] = b[0]
        return user_list

    def get_book_info(self, book_input, user):
        books = pd.read_csv("books.csv")
        book = books.loc[books["title"] == book_input]
        key = list(book["key"])[0]
        users = pd.read_json("users.json")
        book_info = {"key": key, "title": list(book["title"])[0], "author": list(book["author"])[
            0], "keywords": users[user]["books"][key]["keywords"], "already": users[user]["books"][key]["already"], "score": users[user]["books"][key]["score"]}
        return book_info

    def refresh_book_list(self, book_data, user):
        df = pd.read_json("users.json")

        df[user]["books"][list(book_data.keys())[0]]["keywords"] = list(
            book_data.values())[0]["keywords"]
        df[user]["books"][list(book_data.keys())[0]]["already"] = list(
            book_data.values())[0]["already"]
        df[user]["books"][list(book_data.keys())[0]]["score"] = list(
            book_data.values())[0]["score"]

        df.to_json("users.json")
