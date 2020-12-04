from timeit import timeit
from typing import *


@timeit
def day1a(values: List[int], target: int) -> int:
    mySet = set()
    for val in values:
        mySet.add(target - val)

    num1 = num2 = 0
    for val in mySet:
        if 2020 - val in mySet:
            num1 = val
            num2 = 2020 - val
            break

    return num1 * num2


@timeit
def day1b(values: List[int], target: int) -> int:
    num1 = num2 = num3 = 0
    for v1 in values:
        for v2 in values:
            for v3 in values:
                if v1 == v2 or v2 == v3 or v1 == v3:
                    continue
                if v1 + v2 + v3 == target:
                    num1 = v1
                    num2 = v2
                    num3 = v3

    return num1 * num2 * num3


def main():
    inputValues = []
    with open("day1input.txt", "r") as f:
        for line in f.readlines():
            inputValues.append(int(line.strip()))

    target = 2020
    res = day1a(inputValues, target)
    print(res)
    res = day1b(inputValues, target)
    print(res)


if __name__ == '__main__':
    main()
