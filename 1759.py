from sys import stdin

input = stdin.readline


def solve():
    L, C = map(int, input().split())
    letters = sorted(input().split())

    vowels = {'a', 'e', 'i', 'o', 'u'}

    code = []
    ans = []

    def dfs(idx, consonant, vowel):
        if len(code) == L:
            if consonant >= 2 and vowel >= 1:
                ans.append(''.join(code))

        elif idx == C:
            return

        # 추가로 선택해야하는 수 <= 선택 가능한 알파벳 갯수
        elif L - len(code) <= C - idx:
            a = letters[idx]
            code.append(a)
            if a in vowels:
                dfs(idx+1, consonant, vowel+1)
            else:
                dfs(idx+1, consonant+1, vowel)
            code.pop()
            dfs(idx+1, consonant, vowel)

    dfs(0, 0, 0)

    print(*sorted(ans), sep='\n')


if __name__ == '__main__':
    solve()
