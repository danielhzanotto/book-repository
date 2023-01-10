import pandas as pd


class Brain:
    def __init__(self):
        pass

    def append_new_book(self, data):
        book_obj = pd.DataFrame.from_dict(data)
        book_obj.to_csv("catalog.csv", mode="a", index=False, header=False)

    def consult_catalog(self):
        return pd.read_csv("catalog.csv")

    def delete_book(self, index):
        df = pd.read_csv("catalog.csv")
        df.drop(int(index), axis=0, inplace=True)
        df.to_csv("catalog.csv", mode="w", index=False, header=True)

    def get_book(self, book_input):
        df = pd.read_csv("catalog.csv")
        for book in df.itertuples():
            if book[0] == book_input:
                book_index = book
        return book_index

    def refresh_csv(self, book_data):
        df = pd.read_csv("catalog.csv")
        book_obj = pd.DataFrame.from_dict(book_data)
        for book in df.itertuples():
            if book[0] == self.init.book_input:
                df.drop(book[0], axis=0, inplace=True)
                df.to_csv("catalog.csv", mode="w", index=False, header=True)
                book_obj.to_csv("catalog.csv", mode="a",
                                index=False, header=False)
