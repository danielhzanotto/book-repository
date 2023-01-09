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
        df.to_csv("catalog.csv", mode="w", index=False, header=False)

    def edit_book(self, book_input):
        book_obj = df = pd.read_csv("catalog.csv")

        get_book = [book for book in df.itertuples() if book[0] == book_input]
        print(get_book)

        

        # book_obj.to_csv("catalog.csv", mode="a", index=False, header=False)
