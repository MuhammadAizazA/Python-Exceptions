class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration

        result = self.current
        self.current += 2
        return result

user_limit = int(input("Enter range from 0 to: "))

even_numbers = EvenNumbers(limit=user_limit)

if __name__ == '__main__':
    for num in even_numbers:
        print(num)
