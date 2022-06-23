from sys import stdin

input = stdin.readline


def solve():
    str1 = input()[:-1]
    str2 = input()[:-1]

    dp = [0] * len(str1)
    for char in str2:
        count = 0
        for i in range(len(str1)):
            if count < dp[i]:
                count = dp[i]
            elif char == str1[i]:
                dp[i] = count + 1

    return max(dp)


if __name__ == '__main__':
    print(solve())
