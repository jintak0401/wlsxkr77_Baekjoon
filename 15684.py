from sys import stdin

input = stdin.readline


def solve():
    N, M, H = map(int, input().split())
    installed = [0] * N
    horizontal = [set() for _ in range(H + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        horizontal[a].add(b)
        installed[b-1] += 1

    def check_installed(d):
        val = 0
        for i in installed:
            if i % 2:
                val += 1
        return val <= 3 - d

    def check():
        line = [i for i in range(N + 1)]
        for i in range(1, H + 1):
            for j in horizontal[i]:
                line[j], line[j + 1] = line[j + 1], line[j]

        for i in range(1, N + 1):
            if line[i] != i:
                return False

        return True

    def put(max_depth, cur_depth, row, col):
        if max_depth == cur_depth:
            if check():
                return cur_depth
            return -1
        elif check_installed(cur_depth):
            for i in range(row, H + 1):
                for j in range(col if i == row else 1, N):
                    if j-1 not in horizontal[i] and j not in horizontal[i] and j+1 not in horizontal[i]:
                        horizontal[i].add(j)
                        installed[j-1] += 1
                        ret = put(max_depth, cur_depth + 1, i, j)
                        if ret != -1:
                            return ret
                        horizontal[i].remove(j)
                        installed[j-1] -= 1

        return -1

    for depth in range(4):
        ans = put(depth, 0, 1, 1)
        if ans != -1:
            return ans

    return -1


if __name__ == '__main__':
    print(solve())
