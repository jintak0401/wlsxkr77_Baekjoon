# 파이썬 코딩 팁

## Dictionary &nbsp; vs &nbsp; List
### 정해진 범위 내에서 값 읽고 쓰기 속도 비교
`dictionary`의 시간복잡도가 O(N)이어도 `list`가 더 빠르다
```python
n = 1_000_000

# 빠르다
arr = [0] * (n+1)
for i in range(1, n+1):
    arr[i] = some_val
    
# 느리다
dic = {}
for i in range(1, n+1):
    dic[i] = some_val
```

## Dictionary
### 딕셔너리 만들기
`{}`는 literal syntax라서 더 빠르다고 한다.
```python
# 빠르다
list1 = {}

# 느리다
list2 = dict()
```

## List
### 리스트 만들기
`[]`는 literal syntax라서 더 빠르다고 한다.
```python
# 빠르다
list1 = [*map(int, input().split())]
list2 = [0] * N

# 느리다
list3 = list(map(int, input().split()))
list4 = [0 for _ in range(N)]
```

### 리스트에 넣을 원소 개수를 알 때 원소 넣기
```python
# 빠르다
arr1 = [0] * N
for i in range(N):
    arr1[i] = i

# 느리다
arr2 = []
for i in range(N):
    arr2.append(i)
```

### 특정 간격으로 값을 바꾸기
```python
arr = [i for i in range(1, 101)]
interval = 3
start = 2
arr[start::interval] = [0] * len(arr[start::interval])
```
```
[ 1, 2, 0, 4, 5, 0, 7, 8, 0, ... , 88, 89, 0, 91, 92, 0, 94, 95, 0, 97, 98, 0, 100 ]
```

### 특정 범위 삭제하기
후자는 `arr`을 복사하기 때문에 느리지만, 전자는 복사하지 않고 해당 리스트를 이용하기 때문에 빠르다
```python
arr = [i for i in range(1, 101)]

# 빠르다
arr[50:] = []

# 느리다
arr = arr[:50]
```

### 입력의 맨 앞은 제외하여 받기
```python
# 입력이 5 1 2 3 4 5 인 경우
n, *arr = map(int, input().split())

print(n)
print(arr)
```
```
5
[1, 2, 3, 4, 5]
```

## 기타
### 0인 경우 1 더하기
```python
# 0이 아닌경우 1씩 더하기
arr = [0 또는 다른 수로 채워진 리스트]
ans = 0

# 빠르다
for i in range(len(arr)):
    ans += not arr[i]

# 느리다
for i in range(len(arr)):
    if arr[i] != 0:
        ans += 1
        
# 느리다
for i in range(len(arr)):
    arr[i] += 1 if arr[i] else 0
```

### 2진수
`int(string, n)`을 하면 n진법으로 변환가능
```python
val = int('01101', 2)

print(val)
print(bin(val))
```
```
13
'0b1101'
```

---

# 기본 알고리즘

## 에라토스 테네스의 체
```python
def get_prime_list(n: int) -> list[int]:
    if n < 2:
        return []

    n += 1
    # [ 쓰레기값, 3, 5, 7, 9, 11, 13, ... ] 에 대응됨
    sieve = [True] * (n // 2)
    # 3부터 홀수만 검사 (2를 제외한 모든 소수는 홀수이므로)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            k = i * i
            # k=9 -> sieve[4]=9 / i=3는 소수고 sieve[4::3]=[9, 15, 21,...]은 소수가 아님
            # k=25 -> sieve[14]=25 / i=5는 소수고 sieve[14::5]=[25, 35, 45, ...]은 소수가 아님
            sieve[k // 2::i] = [False] * ((n - k - 1) // (2 * i) + 1)

    # 인덱스 1부터 시작하는 이유는 sieve[0]은 쓰레기값이므로
    return [2] + [2 * i + 1 for i in range(1, len(sieve)) if sieve[i]]
```

## 최대공약수, 최소공배수
```python
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return (x * y) // gcd(x, y)
```

## 이분매칭
```python
vertex = [0, [5], [], [6, 7], [2, 3, 5, 7, 8], ... , [5]]
visited = [False] * len(vertex) # 새 노드를 시작할 때 매번 초기화 필요
connected_vertex = [0] * len(vertex)

def bipartite_matching(vertex, here):
    global visited, connected_vertex
    for there in vertex[here]:
        if not visited[there]:
            visited[there] = True
            if (not connected_vertex[there]) or bipartite_matching(vertex, connected_vertex[there]):
                connected_vertex[there] = here
                return True

    return False

count = 0
# 편의상 1부터 시작
for i in range(1, len(vertex)):
    visitied = [False] * len(vertex)
    if bipartite_matching(vertex, i):
        count += 1
```