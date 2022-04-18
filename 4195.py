"""
Probliem Link: https://www.acmicpc.net/problem/4195
Solution Link: https://jintak0401.github.io/posts/boj-4195
"""
from sys import stdin

input = stdin.readline


def solve():
    TC = int(input())

    for _ in range(TC):
        F = int(input())
        # 자식이름: 부모이름 or 집합 갯수
        disjoint_set = {}
        for _ in range(F):
            a, b = input().split()
            if a not in disjoint_set:
                disjoint_set[a] = 1
            if b not in disjoint_set:
                disjoint_set[b] = 1

            while isinstance(disjoint_set[a], str):
                a = disjoint_set[a]
            while isinstance(disjoint_set[b], str):
                b = disjoint_set[b]

            if a == b:
                print(disjoint_set[a])
            else:
                a_val, b_val = disjoint_set[a], disjoint_set[b]
                if b_val < a_val:
                    disjoint_set[a] += disjoint_set[b]
                    disjoint_set[b] = a
                    print(disjoint_set[a])
                else:
                    disjoint_set[b] += disjoint_set[a]
                    disjoint_set[a] = b
                    print(disjoint_set[b])


if __name__ == '__main__':
    solve()
