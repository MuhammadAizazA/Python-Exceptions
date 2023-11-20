import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution Time: {end_time - start_time} seconds")
        return result
    return wrapper

squares = [x**2 for x in range(1, 11)]
even_squares = [x for x in squares if x % 2 == 0]

class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration

for num in range(5, 11):
    print(num)

sum_of_range = sum(range(1, 101))

multiply = lambda x, y: x * y
sorted_tuples = sorted([(2, 5), (1, 8), (3, 3)], key=lambda x: x[1])

@timing_decorator
def process_numbers():
    cubes = [x**3 for x in range(1, 6)]
    print(cubes)
    filtered_cubes = list(filter(lambda x: x % 3 == 0, cubes))
    print("Filtered Cubes:", filtered_cubes)

if __name__=='__main__':
    process_numbers()

