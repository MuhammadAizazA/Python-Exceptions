#1
square=lambda x: x**2

square(6)

#2
raw_list_1=[x for x in range(1,11)]
even_number=list(filter(lambda x: (x % 2)==0,raw_list_1))

print(even_number)

raw_list_2=[x for x in range(1,6)]
square_list=list(map(lambda x: x**2,raw_list_2))

print(square_list)