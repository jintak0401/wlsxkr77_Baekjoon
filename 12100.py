from sys import stdin
from functools import reduce

input = stdin.readline


def solve():
    N = int(input())
    N2 = N * N
    max_depth = 5

    init_board = [0] * N2
    for i in range(0, N2, N):
        init_board[i:i+N] = [*map(int, input().split())]

    already = set()

    def get_start_and_step(d, line):
        if d == 0: return line, N2, N
        elif d == 1: return N2 - N + line, None, -N
        elif d == 2: return N * line, N * (line + 1), 1
        else: return N * (line + 1) - 1, N * line - 1 if line > 0 else None, -1

    able_to_sum = True
    def reduce_func(prev, cur):
        nonlocal able_to_sum
        if cur == 0: return prev
        elif prev and prev[-1] == cur and able_to_sum:
            prev[-1] += cur
            able_to_sum = False
        else:
            prev.append(cur)
            able_to_sum = True
        return prev

    def dfs(depth, board):
        if depth == max_depth:
            return max(board)
        already.add(tuple(board))
        ret = max(board)
        for d in range(4):
            arr = [0] * N2
            for i in range(N):
                start, end, step = get_start_and_step(d, i)
                tmp = reduce(reduce_func, board[start:end:step], [])
                arr[start:end:step] = tmp + [0] * (N - len(tmp))

            if tuple(arr) not in already:
                val = dfs(depth + 1, arr)
                if ret < val: ret = val

        return ret

    return dfs(0, init_board)


if __name__ == '__main__':
    print(solve())
