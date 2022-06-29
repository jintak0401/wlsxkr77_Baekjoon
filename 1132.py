from sys import stdin

input = stdin.readline


def solve():
    N = int(input())
    power = [1]
    for _ in range(11):
        power.append(10 * power[-1])

    alpha = {}
    start = set()
    for _ in range(N):
        tmp = input()[:-1]
        start.add(tmp[0])
        for i in range(len(tmp)):
            alpha[tmp[i]] = alpha.get(tmp[i], 0) + power[len(tmp) - i - 1]

    alpha = sorted(alpha.items(), key=lambda x: -x[1])
    if len(alpha) == 10 and alpha[-1][0] in start:
        idx = -2
        while alpha[idx][0] in start:
            idx -= 1
        alpha.append(alpha.pop(idx))

    ans = 0
    num = 9
    for _, digit in alpha:
        ans += num * digit
        num -= 1

    return ans


if __name__ == '__main__':
    print(solve())