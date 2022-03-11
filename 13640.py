from sys import stdin

input = stdin.readline


def solve():
    N, M = map(int, input().split())
    d = ((1, 0), (0, 1), (-1, 0), (0, -1))
    arr = [0] * N
    r_pos, b_pos, o_pos = -1, -1, -1
    arr[0] = input()[:-1]
    for i in range(1, N-1):
        arr[i] = input()[:-1]
        if r_pos == -1:
            pos = arr[i].find('R')
            if pos != -1:
                r_pos = (i, pos)
        if b_pos == -1:
            pos = arr[i].find('B')
            if pos != -1:
                b_pos = (i, pos)
        if o_pos == -1:
            pos = arr[i].find('O')
            if pos != -1:
                o_pos = (i, pos)
    arr[-1] = input()[:-1]

    def move_marble(pos, dx, dy):
        cur_x, cur_y = pos
        while True:
            next_x, next_y = cur_x + dx, cur_y + dy
            if arr[next_x][next_y] == '#':
                break
            elif arr[next_x][next_y] == 'O':
                cur_x, cur_y = next_x, next_y
                break
            cur_x, cur_y = next_x, next_y
        return cur_x, cur_y

    state = (r_pos, b_pos)
    que = [state]
    visited = set([state])
    for step in range(1, 12):
        new_que = []
        if step == 11 or not que:
            return -1
        while que:
            start_rpos, start_bpos = que.pop()
            for dx, dy in d:
                end_rpos = move_marble(start_rpos, dx, dy)
                end_bpos = move_marble(start_bpos, dx, dy)
                if end_bpos == o_pos:
                    continue
                elif end_rpos == o_pos:
                    return step
                elif end_rpos == end_bpos:
                    if dx:
                        if start_rpos[0] * dx < start_bpos[0] * dx:
                            end_rpos = (end_rpos[0] - dx, end_rpos[1])
                        else:
                            end_bpos = (end_bpos[0] - dx, end_bpos[1])
                    else:
                        if start_rpos[1] * dy < start_bpos[1] * dy:
                            end_rpos = (end_rpos[0], end_rpos[1] - dy)
                        else:
                            end_bpos = (end_bpos[0], end_bpos[1] - dy)

                state = (end_rpos, end_bpos)
                if state not in visited:
                    visited.add(state)
                    new_que.append(state)

        que = new_que


if __name__ == '__main__':
    print(solve())
