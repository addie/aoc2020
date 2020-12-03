import time
from typing import *
import collections


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            val = (te - ts) * 1000
            print(f'{method.__name__}  {val:2.2f} ms')
        return result

    return timed


@timeit
def part1(inputValues: List[List[str]]) -> int:
    return count_trees(inputValues, 1, 3)


# Right 1, down 1.
# Right 3, down 1.
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
@timeit
def part2(inputValues: List[List[str]]) -> int:
    return count_trees(inputValues, 1, 1) \
           * count_trees(inputValues, 1, 3) \
           * count_trees(inputValues, 1, 5) \
           * count_trees(inputValues, 1, 7) \
           * count_trees(inputValues, 2, 1)


def count_trees(grid: List[List[str]], r: int, c: int) -> int:
    trees = 0
    row, col = r, c
    while row < len(grid):
        if grid[row][col] == '#':
            trees += 1
        row += r
        col = (col + c) % len(grid[0])
    return trees


def main():
    inputValues = []
    with open("day3input.txt", "r") as f:
        for line in f.readlines():
            curr_line = []
            for char in line:
                if char == "." or char == "#":
                    curr_line.append(char)
            inputValues.append(curr_line)

    res = part1(inputValues)
    print(res)
    res = part2(inputValues)
    print(res)


if __name__ == '__main__':
    main()
