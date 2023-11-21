"""
create a lambda function that takes this list of strings,
converts each string to an integer, filters out the even numbers,
squares the remaining odd numbers, and returns the result as a list.
"""


numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

lambda_square_even=lambda x: int(x)**2 if int(x)%2!=0 else int(x)

list1=list(map(lambda_square_even,numbers))

print(list1)

people = [
    {'name': 'Alice', 'age': 25, 'salary': 60000},
    {'name': 'Bob', 'age': 35, 'salary': 45000},
    {'name': 'Charlie', 'age': 40, 'salary': 80000},
    {'name': 'David', 'age': 28, 'salary': 55000},
    {'name': 'Eva', 'age': 45, 'salary': 48000},
]
#age>30 and 

list_1= (lambda persons:sorted(map(lambda person:person['name'],filter(lambda person: person['salary']<50000 and person['age']>30,persons))))(people)

print(list_1)