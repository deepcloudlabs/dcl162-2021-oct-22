import pickle

employees = [
    ["tr1", "jack bauer", 1000],
    ["tr2", "kate austen", 2000],
    ["tr3", "james sawyer", 3000],
    ["tr4", "jin kwon", 4000]
]

with open("employees.pkl", mode="wb") as f:
    pickle.dump(employees, f)
