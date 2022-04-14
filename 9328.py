from sys import stdin

input = stdin.readline


def solve():
    def adj(pos):
        r, c = pos // w, pos % w
        if 0 < r:
            yield pos - w
        if r < h - 1:
            yield pos + w
        if 0 < c:
            yield pos - 1
        if c < w - 1:
            yield pos + 1

    def get_entrance():
        for i in range(w):
            if arr[i] != '*':
                yield i

        idx = w
        for i in range(h - 2):
            if arr[idx] != '*':
                yield idx
            idx += w - 1
            if arr[idx] != '*':
                yield idx
            idx += 1

        for i in range(idx, _len):
            if arr[i] != '*':
                yield i

    def visit(pos):
        _pos = ord(arr[pos])
        # 빈 공간 or 문서
        if _pos == 46 or _pos == 36:
            que.append(pos)
            visited[pos] = True
        # 열쇠
        elif 97 <= _pos <= 122:
            k = _pos - 97
            if not key[k]:
                key[k] = True
                que.extend(stuck[k])
            que.append(pos)
            visited[pos] = True
        # 문
        else:
            d = _pos - 65
            if key[d]:
                que.append(pos)
            else:
                stuck[d].append(pos)

            visited[pos] = True

    for _ in range(int(input())):
        h, w = map(int, input().split())
        _len = h * w
        arr = ''

        for _ in range(h):
            arr += input()[:-1]

        key_str = input()[:-1]
        key = [False] * 26
        if key_str != '0':
            for k in key_str:
                key[ord(k) - 97] = True

        stuck = [[] for _ in range(26)]
        visited = [False] * _len

        # $: 36 / *: 42 / a: 97 / z: 122 / A: 65 / Z: 90 / .: 46
        ans = 0
        # get_entrance() 에서 가능한 입구만 yield 해준다
        for e in get_entrance():
            if not visited[e]:
                que = []
                visit(e)
                while que:
                    pos = que.pop()
                    # 문서인 경우
                    if arr[pos] == '$':
                        ans += 1
                    for nxt in adj(pos):
                        if arr[nxt] != '*' and not visited[nxt]:
                            visit(nxt)

        print(ans)


if __name__ == '__main__':
    solve()
