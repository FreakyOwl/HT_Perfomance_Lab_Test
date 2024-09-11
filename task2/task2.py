import math
import random
import sys
import os


def task2(path1, path2):
    with open(path2, "r") as f2:
        file = f2.readlines()
        center = file[0].split()
        center_x = float(center[0])
        center_y = float(center[1])
        rad = int(file[1])

    with open(path1, "r") as f1:
        for line in f1:
            dot = line.split()
            dot_x = float(dot[0])
            dot_y = float(dot[1])
            hypo = math.sqrt((dot_x - center_x) ** 2 + (dot_y - center_y) ** 2)
            if hypo < rad:
                print("1")
            elif hypo == rad:
                print("0")
            else:
                print("2")


if sys.argv[1:]:
    args = sys.argv[1:]
    path1 = args[0]
    path2 = args[1]
else:
    path1 = "dot.txt"
    path2 = "circle.txt"

if not os.path.isfile(path1):
    dot_n = random.randrange(1, 101)
    dots = [f"{str(random.uniform(0.1, 100))} {str(random.uniform(0.1, 100))}\n" for i in
            range(dot_n)]
    with open(path1, "w") as f1:
        f1.writelines(dots)

if not os.path.isfile(path2):
    with open(path2, "w") as f2:
        circle = f"{str(random.uniform(0.1, 100))} {str(random.uniform(0.1, 100))}\n{str(random.randrange(1, 51))}"
        f2.write(circle)

task2(path1, path2)
