from sys import stdin
from collections import deque

input = stdin.readline


ans: list[int]
queue: deque[tuple[int, ...]] = deque()


# 유클리드 호제법을 이용한 최대공약수
def GCD(x, y):
    while y:
        x, y = y, x % y
    return x


# 최대공약수를 이용한 최소공배수 구하기
def LCM(x, y):
    return (x * y) // GCD(x, y)


def mul_list(n: int):
    for i in range(len(ans)):
        ans[i] *= n


def solve():
    while queue:
        a, b, p, q = queue.popleft()
        if ans[a] or ans[b]:
            common_idx, target_idx = (a, b) if ans[a] else (b, a)
            common_val, target_val = (p, q) if ans[a] else (q, p)

            lcm = LCM(ans[common_idx], common_val)
            mul_list(lcm // ans[common_idx])
            ans[target_idx] = target_val * (lcm // common_val)

        else:
            queue.append((a, b, p, q))


if __name__ == '__main__':
    n = int(input())
    ans = [0] * n

    for i in range(n - 1):
        a, b, p, q = map(int, input().split())
        gcd = GCD(p, q)
        p //= gcd
        q //= gcd
        if i == 0:
            ans[a] = p
            ans[b] = q
        else:
            queue.append((a, b, p, q))

    solve()
    print(*ans)
