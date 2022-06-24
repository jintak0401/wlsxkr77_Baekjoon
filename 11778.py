from sys import stdin

input = stdin.readline


def solve():
    mod = 1_000_000_007

    def mul_mat(mat1, mat2):
        ret = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    ret[i][j] += mat1[i][k] * mat2[k][j]
                ret[i][j] %= mod
        return ret

    def fibonacci(num):
        if num <= 2: return 1
        ans = [[1, 0], [0, 1]]
        mat = [[1, 1], [1, 0]]

        while num:
            if num % 2:
                ans = mul_mat(ans, mat)
            mat = mul_mat(mat, mat)
            num //= 2

        return ans[0][1]

    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    N, M = map(int, input().split())

    return fibonacci(gcd(N, M))


if __name__ == '__main__':
    print(solve())
