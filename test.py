import pandas as pd

book_data = [{
    "title": 123,
    "author": 456,
    "labels": 789,
    "read": 0
}]


book_obj = pd.DataFrame.from_dict(book_data)
book_obj.to_csv("catalog.csv", mode="a", index=True, header=False)
