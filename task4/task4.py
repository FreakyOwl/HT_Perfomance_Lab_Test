import statistics
import random
import sys
import os


def task4(path):
    with open(path, "r") as f1:
        numbers = [int(line) for line in f1]
        med = round(statistics.median(numbers))
        turns = sum(abs(num - med) for num in numbers)
    print(turns)


if sys.argv[1:]:
    args = sys.argv[1:]
    path = args[0]
else:
    path = "numbers.txt"

if not os.path.isfile(path):
    num_num = random.randrange(1, 11)
    numbers = [f"{str(random.randrange(-10, 11))}\n" for i in range(num_num)]
    with open(path, "w") as f1:
        f1.writelines(numbers)

task4(path)
