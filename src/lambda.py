import functools 
#1
square=lambda x: x**2

square(6)

#2
raw_list_1=[x for x in range(1,11)]
even_number=list(filter(lambda x: (x % 2)==0,raw_list_1))



#3
raw_list_2=[x for x in range(1,6)]
square_list=list(map(lambda x: x**2,raw_list_2))



#4
students = {('Aizaz', 85,6), ('Hamza', 92,4), ('Ali', 78,1), ('Dawood', 95,7), ('Saif', 88,8)}

sorted_students = sorted(students, key=lambda x: x[2],reverse=False)



#5
raw_list_3=[x for x in range(1,6)]
partial_sum = functools.partial(lambda x, y, z: (x + y) * z)
result=functools.reduce(lambda x,y: x+y,raw_list_3)





if __name__=='__main__':
    square(7)
    print(even_number)
    print(square_list)
    print(sorted_students)
    print(result)