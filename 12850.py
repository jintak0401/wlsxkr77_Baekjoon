from sys import stdin

input = stdin.readline

mod = 1_000_000_007


def mul_mat(a, b):
    ret = [[0] * len(a) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a)):
            for k in range(len(a)):
                ret[i][j] += a[i][k] * b[k][j]
                ret[i][j] %= mod

    return ret


def solve():
    D = int(input())

    mat = [[0, 1, 1, 0, 0, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 0],
           [1, 1, 0, 1, 1, 0, 0, 0],
           [0, 1, 1, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 1, 0],
           [0, 0, 0, 1, 1, 0, 0, 1],
           [0, 0, 0, 0, 1, 0, 0, 1],
           [0, 0, 0, 0, 0, 1, 1, 0]
           ]

    flag = True
    bit = 1
    while True:
        if bit & D:
            if flag:
                ans = mat
                flag = False
            else:
                ans = mul_mat(ans, mat)

        if (bit << 1) > D:
            break
        mat = mul_mat(mat, mat)
        bit <<= 1

    return ans[0][0]


if __name__ == '__main__':
    print(solve())
