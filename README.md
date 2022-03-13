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

### 2차원 리스트를 1차원 리스트로 다루기
```python
row, col = 3, 4
arr = [1, 0, 0, 1,
       0, 1, 1, 0,
       1, 1, 0, 0]

def adj(pos):
    r, c = pos // col, pos % col
    # 상
    if r > 0:
        yield pos-col
    # 하
    if r < row - 1:
        yield pos+col
    # 좌
    if c > 0:
        yield pos-1
    # 우
    if c < col - 1:
        yield pos+1

for pos in range(len(arr)):
    # ex) pos: 0 --> around: [1, 4] / pos: 5 --> around: [1, 4, 6, 0]
    for around in adj(pos):
        ...
```

### deque 없이 BFS 하기
```python
que = [시작 지점]
end_step = 0
for step in range(100):
    if not que:
        # 몇 번째 단계에서 끝났는지
        end_step = step
        break
    new_que = []
    while que:
        val = que.pop()
        ...
        new_que.append(다음에 수행해야할 지점)

    que = new_que
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

### 10진수를 2진수 변환
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

### 특정 비트 빼기
```python
a = (1 << 5) - 1 # a = 11111

b = 1 << 3 # b = 100

c = a & (~b) # c = 11011
```

### 2진수 변환시 1 개수 세기
```python
a = (1 << 5) - 1 # a = 11111
print(bin(a).count('1'))
```
```
5
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
# left_vertex[i]: i번째 left_vertex가 갈 수 있는 right_vertex들
left_vertex = [0, [5], [], [6, 7], [2, 3, 5, 7, 8], ... , [5]]
right_vertex_num = 10 
# right_vertex와 연결된 left_vertex
right_vertex = [0] * (right_vertex_num + 1)

def bipartite_matching(visited, here):
    visited[here] = True
    for there in left_vertex[here]:
        if not right_vertex[there]:
            right_vertex[there] = here
            return True
    for there in left_vertex[here]:
        if not visited[right_vertex[there]] and bipartite_matching(visited, right_vertex[there]):
            right_vertex[there] = here
            return True
    return False

count = 0
# 편의상 1부터 시작
for i in range(1, len(left_vertex)+1):
    # visited는 방문했던 right_vertex
    # visited는 새 노드 left_vertex를 시작할 때 매번 초기화 필요
    if bipartite_matching([False] * (len(left_vertex) + 1), i):
        count += 1
        if count == right_vertex_num:
            break
```

### 선분 교차 판별
```python
def ccw(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (c[0]-a[0])*(b[1]-a[1])


# line: ((x좌표1, y좌표1), (x좌표2, y좌표2))
def is_intersect(line1, line2):
    a, b = line1[0], line1[1]
    c, d = line2[0], line2[1]
    ab = ccw(a, b, c) * ccw(a, b, d)
    cd = ccw(c, d, a) * ccw(c, d, b)
    if ab == 0 and cd == 0:
        if a > b:
            a, b = b, a
        if c > d:
            c, d = d, c
        return c <= b and a <= d
    return ab <= 0 and cd <= 0
```