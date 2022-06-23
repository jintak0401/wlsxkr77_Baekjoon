from sys import stdin

input = stdin.readline


def solve():
    str1 = '0' + input()[:-1]
    str2 = '1' + input()[:-1]

    dp = [[0] * len(str2) for _ in range(len(str1))]
    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            dp[i][j] = max(dp[i-1][j-1] + (str1[i] == str2[j]), dp[i][j-1], dp[i-1][j])

    return dp[-1][-1]


if __name__ == '__main__':
    print(solve())
