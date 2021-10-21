import pandas as pd

df1 = pd.DataFrame([
    {"iban": "tr1", "fullname": "jack bauer", "salary": 1000},
    {"iban": "tr2", "fullname": "kate austen", "salary": 2000},
    {"iban": "tr3", "fullname": "james sawyer", "salary": 3000},
    {"iban": "tr4", "fullname": "jin kwon", "salary": 4000}
], columns=["iban", "fullname", "salary"])

df1.to_json("employees_dataframe.json")

df2 = pd.read_json('employees_dataframe.json')
print(df2.index)
print(df2.columns)
print(df2)
