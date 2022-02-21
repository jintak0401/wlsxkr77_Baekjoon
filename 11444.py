from sys import stdin

input = stdin.readline

mod = 1_000_000_007


def mul_mat(mat1, mat2):
    ret = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ret[i][j] += mat1[i][k] * mat2[k][j]
            ret[i][j] %= mod

    return ret


def solve():
    global n

    ans = [[1, 0], [0, 1]]
    mat = [[1, 1], [1, 0]]

    while n:
        if n & 1:
            ans = mul_mat(ans, mat)
        mat = mul_mat(mat, mat)
        n //= 2

    return ans[0][1]


if __name__ == '__main__':
    n = int(input())

    if n <= 1:
        print(n)
    else:
        print(solve())
