import statistics
import random


def task4 (path):
    with open(path, "r") as f1:
        numbers = [int(line) for line in f1]
        med = round(statistics.median(numbers))
        turns = sum(abs(num - med) for num in numbers)
    print(turns)


path = "numbers.txt"

num_num = random.randrange(1, 11)
numbers = [f"{str(random.randrange(-10, 11))}\n" for i in range(num_num)]

with open(path, "w") as f1:
    f1.writelines(numbers)

task4(path)
