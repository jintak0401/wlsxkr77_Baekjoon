from sys import stdin

input = stdin.readline


arr = []

# '4' -> 4 / 'A' -> 10 / 'Z' -> 35
c2n = {}

# 4 -> '4' / 10 -> 'A' / 35 -> 'Z'
n2c = {}


def solve():

    power = [1] * 51
    for i in range(1, len(power)):
        power[i] = 36 * power[i-1]

    dic = {}

    for num in arr:
        for i in range(len(num)):
            digit = c2n[num[~i]]
            dic[digit] = dic.get(digit, 0) + power[i]

    if K == 0:
        gain = 0

    else:
        gain = sum(sorted((35 - digit) * _sum for digit, _sum in dic.items())[-K:])

    total = gain + sum(digit * _sum for digit, _sum in dic.items())

    # 10진수 -> 36진수 변환
    ans = ''
    while total != 0:
        div, mod = divmod(total, 36)
        ans += n2c[mod]
        total = div

    return ans[::-1] if len(ans) else 0


if __name__ == '__main__':
    N = int(input())
    for _ in range(N):
        arr.append(input().rstrip())
    K = int(input())

    alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(alpha)):
        c2n[alpha[i]] = i
        n2c[i] = alpha[i]

    print(solve())
