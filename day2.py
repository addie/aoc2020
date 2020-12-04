from timeit import timeit
from typing import *
import collections


@timeit
def part1(inputValues: List[Tuple]) -> int:
    count = 0
    for inputValue in inputValues:
        if valid_count(*inputValue):
            count += 1

    return count


def valid_count(password: str, letter: str, start: int, stop: int) -> bool:
    chars = collections.Counter(password)
    return start <= chars[letter] <= stop


@timeit
def part2(inputValues: List[Tuple]) -> int:
    count = 0
    for inputValue in inputValues:
        if valid_position(*inputValue):
            count += 1

    return count


def valid_position(password: str, letter: str, posOne: int, posTwo: int) -> bool:
    if posOne > len(password) or posTwo > len(password) or \
            (password[posOne - 1] == letter and password[posTwo - 1] == letter):
        return False
    if password[posOne - 1] == letter or password[posTwo - 1] == letter:
        return True
    return False


def main():
    inputValues = []
    with open("day2input.txt", "r") as f:
        for line in f.readlines():
            code = line.split(":")[0].strip()
            ss = code.split(" ")[0]

            password = line.split(":")[1].strip()
            letter = code.split(" ")[1]
            start = ss.split("-")[0]
            stop = ss.split("-")[1]
            inputValues.append((password, letter, int(start), int(stop)))

    # Example "8-9 x: xxxxxxxrk"
    res = part1(inputValues)
    print(res)
    res = part2(inputValues)
    print(res)


if __name__ == '__main__':
    main()
