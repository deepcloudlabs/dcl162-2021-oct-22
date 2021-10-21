import json

employees = [
    {"iban": "tr1", "fullname": "jack bauer", "salary": 1000},
    {"iban": "tr2", "fullname": "kate austen", "salary": 2000},
    {"iban": "tr3", "fullname": "james sawyer", "salary": 3000},
    {"iban": "tr4", "fullname": "jin kwon", "salary": 4000}
]

with open("employees.json", mode="wt") as f:
    json.dump(employees, f)
