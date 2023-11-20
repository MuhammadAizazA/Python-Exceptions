def print_person_info_simple(name,age,city):
    print(f"Name: {name}, Age: {age}, City: {city}")

def print_person_info_forced(name,*,age,city):
    print(f"Name: {name}, Age: {age}, City: {city}")