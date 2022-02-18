from sys import stdin
import re

input = stdin.readline

regex = re.compile('(100+1+|01)+')


def solve(pattern: str):
    result = regex.fullmatch(pattern)
    return 'YES\n' if result else 'NO\n'


if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        inputPattern = input()[:-1]
        print(solve(inputPattern))
