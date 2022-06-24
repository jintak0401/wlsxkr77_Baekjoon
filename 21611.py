from sys import stdin
from itertools import chain

input = stdin.readline


def solve():
    def get_beads():
        arr = [0] * N2
        for i in range(0, N2, N):
            arr[i:i + N] = map(int, input().split())

        N_plus_1 = N + 1
        N_minus_1 = N - 1
        center = (N2 - 1) // 2
        ret = []
        for i in range(1, N_minus_1 // 2 + 1):
            start = center - N_plus_1 * (i - 1) - 1
            lu = start - N
            ld = center + N_minus_1 * i
            rd = center + N_plus_1 * i
            ru = center - N_minus_1 * i
            _chain = chain(
                range(start, ld, N),
                range(ld, rd, 1),
                range(rd, ru, -N),
                range(ru, lu - 1, -1)
            )
            for j in _chain:
                ret.append(arr[j])

        return ret

    start_pos = [0, 6, 2, 0, 4]
    gaps = [0, 15, 11, 9, 13]

    def magic(direction, dist):
        indices = [start_pos[direction]]
        gap = gaps[direction]

        for _ in range(1, dist):
            indices.append(indices[-1] + gap)
            gap += 8

        for i, pos in enumerate(indices):
            if (tmp := pos - i) < len(beads):
                del beads[tmp]
            else:
                break

    def explode_beads():
        flag = True
        while flag:
            flag = False
            idx = 0
            while idx < len(beads):
                nxt_idx = idx + 1
                while nxt_idx < len(beads) and beads[nxt_idx] == beads[idx]:
                    nxt_idx += 1

                if (tmp := nxt_idx - idx) >= 4 or beads[idx] == 0:
                    exploded_marbles[beads[idx]] += tmp
                    flag = True
                    del beads[idx:nxt_idx]

                else:
                    idx = nxt_idx

    def split_beads():
        nxt_beads = []
        idx = 0
        while idx < len(beads) and len(nxt_beads) != N2 - 1:
            nxt_idx = idx + 1
            while nxt_idx < len(beads) and beads[nxt_idx] == beads[idx]:
                nxt_idx += 1

            nxt_beads.append(nxt_idx - idx)
            nxt_beads.append(beads[idx])
            idx = nxt_idx

        return nxt_beads

    N, M = map(int, input().split())
    N2 = N * N

    beads = get_beads()

    exploded_marbles = [0] * 4
    for _ in range(M):
        d, s = map(int, input().split())
        magic(d, s)
        explode_beads()
        beads = split_beads()

    ans = 0
    for i in range(1, 4):
        ans += exploded_marbles[i] * i
    return ans


if __name__ == '__main__':
    print(solve())
