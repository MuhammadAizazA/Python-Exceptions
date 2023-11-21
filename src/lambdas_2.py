"""
create a lambda function that takes this list of strings,
converts each string to an integer, filters out the even numbers,
squares the remaining odd numbers, and returns the result as a list.
"""


numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

lambda_square_even=lambda x: int(x)**2 if int(x)%2!=0 else int(x)

list1=list(map(lambda_square_even,numbers))

print(list1)