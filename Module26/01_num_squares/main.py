class Square:
    def __init__(self,number: int) -> None:
        self.number = number
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count > self.number:
            raise StopIteration
        return self.count ** 2


def gen_sqr(number):
    for num in range(1,number + 1):
        yield num ** 2

number = int(input("Enter number: "))
class_sqr = Square(number)

print("Class generator:")
for num in class_sqr:
    print(num, end=" ")

print("\nFunction generator: ")
for num in gen_sqr(number):
    print(num, end=" ")

print("\nGen expression: ")

numbers = (num ** 2 for num in range(1,number + 1))
print(*numbers)

