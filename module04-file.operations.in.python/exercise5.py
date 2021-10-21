import csv

employees = [
    {"iban": "tr1", "fullname": "jack bauer", "salary": 1000},
    {"iban": "tr2", "fullname": "kate austen", "salary": 2000},
    {"iban": "tr3", "fullname": "james sawyer", "salary": 3000},
    {"iban": "tr4", "fullname": "jin kwon", "salary": 4000}
]


def for_each(action, elements):  # higher-order function
    for element in elements:
        action(element)


with open("employees.csv", mode="wt", newline='') as f:
    writer = csv.writer(f)
    for employee in employees:
        writer.writerow(employee.values())
    # writer.writerows(employees)

with open("employees_functional.csv", mode="wt", newline='') as f:
    writeRow = csv.writer(f).writerow
    to_values = lambda emp: emp.values()
    for_each(writeRow, map(to_values, employees))
