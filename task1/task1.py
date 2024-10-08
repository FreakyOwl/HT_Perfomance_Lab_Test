import sys


def task1(n, m):
    if not isinstance(n, int):
        raise TypeError(f"Expected int, got {type(n)}")
    if not isinstance(m, int):
        raise TypeError(f"Expected int, got {type(m)}")
    first_elem = 1
    cur_elem = first_elem
    output = f"{first_elem}"
    while 1:
        cur_elem = 1 + (cur_elem + m - 2) % n
        if cur_elem == first_elem:
            break
        output = output + str(cur_elem)
    print(output)


if sys.argv[1:]:
    args = sys.argv[1:]
    n = int(args[0])
    m = int(args[1])
else:
    n = 5
    m = 4

task1(n, m)
