import functools
def print_person_info_simple(name,age,city):
    print(f"Name: {name}, Age: {age}, City: {city}")

def print_person_info_forced(name,*,age,city):
    print(f"Name: {name}, Age: {age}, City: {city}")

my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
my_numbers = [4, 6, 9, 23, 5]

mapped_floats=list(map(lambda x: f"{x:.3f}",my_floats))
filter_result = list(filter(lambda name: len(name)>=7, my_names))
product=functools.reduce(lambda x,y:x*y,my_numbers)

print(mapped_floats)
print(filter_result)
print(product)
