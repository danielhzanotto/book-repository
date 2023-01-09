import pandas as pd


df = pd.read_csv("catalog.csv")
print(df)

book_data = [{
    "title": "aaa",
    "author": 222,
    "labels": 222,
    "read": 1
}]

# input_book = 0
# get_book = [book for book in df.itertuples() if book[0] == input_book]
# print(get_book[0][2])

book_obj = pd.DataFrame.from_dict(book_data)


for book in df.itertuples():
    if book[1] == book_obj.iloc[0][0]:
        print(book[0])
        df.drop(book[0], axis=0, inplace=True)
        df.to_csv("catalog.csv", mode="w", index=False, header=False)
        book_obj.to_csv("catalog.csv", mode="a", index=False, header=False)

df = pd.read_csv("catalog.csv")
print(df)
