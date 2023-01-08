import pandas as pd


class Brain:
    def __init__(self):
        pass

    def append_new_book(self, data):
        book_obj = pd.DataFrame.from_dict(data)
        book_obj.to_csv("catalog.csv", mode="a", index=False, header=False)

    def consult_catalog(self):
        return pd.read_csv("catalog.csv")
