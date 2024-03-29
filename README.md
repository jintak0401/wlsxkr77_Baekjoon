# JS 코딩 팁

## 기본 알고리즘

### 이분탐색

```js
const bisectLeft = (arr, x) => {
  let left = 0,
    right = arr.length,
    mid;
  while (left < right) {
    mid = Math.floor((left + right) / 2);
    arr[mid] < x ? (left = mid + 1) : (right = mid);
  }
  return left;
};

const bisectRight = (arr, x) => {
  let left = 0,
    right = arr.length,
    mid;
  while (left < right) {
    mid = Math.floor((left + right) / 2);
    arr[mid] <= x ? (left = mid + 1) : (right = mid);
  }
  return right;
};
```

### Heap

```js
const compare = (a, b) => {
    if (typeof a === 'number') return a - b;
    else {
        let val = 0;
        for (let i = 0; i < a.length; i++) {
            val = a[i] - b[i];
            if (val !== 0) return val;
        }
        return 0;
    }
};

const heappush = (heap, element) => {
    heap.push(element);
    let idx = heap.length - 1;
    let parentIdx = 0;
    const last = heap[idx];

    while (idx) {
        parentIdx = Math.floor((idx - 1) / 2);
        if (compare(heap[parentIdx], last) > 0) {
            heap[idx] = heap[parentIdx];
            idx = parentIdx;
        } else break;
    }

    heap[idx] = last;
};
const heappop = (heap) => {
    if (heap.length === 0) return undefined;

    const min = heap[0];
    const last = heap.pop();
    const len = heap.length;
    if (len !== 0) {
        let leftIdx,
            rightIdx,
            smallIdx,
            idx = 0;
        while ((leftIdx = 2 * idx + 1) < len) {
            rightIdx = leftIdx + 1;
            smallIdx =
                rightIdx < len && compare(heap[rightIdx], heap[leftIdx]) <= 0
                    ? rightIdx
                    : leftIdx;
            if (compare(last, heap[smallIdx]) > 0) {
                heap[idx] = heap[smallIdx];
                idx = smallIdx;
            } else break;
        }
        heap[idx] = last;
    }
    return min;
};

const heapify = (heap) => {
    const len = heap.length;
    let leftIdx, rightIdx, smallIdx, rootIdx;

    const build = (idx) => {
        rootIdx = idx;
        leftIdx = 2 * idx + 1;
        rightIdx = leftIdx + 1;
        smallIdx =
            rightIdx < len && compare(heap[rightIdx], heap[leftIdx]) <= 0
                ? rightIdx
                : leftIdx;

        if (compare(heap[rootIdx], heap[smallIdx]) > 0) {
            [heap[rootIdx], heap[smallIdx]] = [heap[smallIdx], heap[rootIdx]];
            if (2 * smallIdx + 1 < len) build(smallIdx);
        }
    };

    for (let i = Math.floor(len / 2) - 1; i >= 0; i--) {
        build(i);
    }
};
```

### 순열, 조합

```js
// 순열
function* permute(arr, r = arr.length) {
    for (let i = 0; i < arr.length; i++) {
        if (r === 1) {
            yield [arr[i]];
        }
        else {
            const next = arr.slice(0, i).concat(arr.slice(i + 1));
            for (const p of permute(next, r - 1)) {
                yield [arr[i], ...p];
            }
        }
    }
}

// 조합
function* combi(arr, r = arr.length) {
    for (let i = 0; i < arr.length; i++) {
        if (r === 1) {
            yield [arr[i]];
        }
        else {
            const next = arr.slice(i + 1);
            for (const c of combi(next, r - 1)) {
                yield [arr[i], ...c];
            }
        }
    }
}

// 중복순열
function* product(arr, r = arr.length) {
    for (let i = 0; i < arr.length; i++) {
        if (r === 1) {
            yield [arr[i]];
        }
        else {
            for (const p of product(arr, r - 1)) {
                yield [arr[i], ...p];
            }
        }
    }
}

// 중복조합
function* combiWithReplacement(arr, r = arr.length) {
    for (let i = 0; i < arr.length; i++) {
        if (r === 1) {
            yield [arr[i]];
        } else {
            const next = arr.slice(i);
            for (const c of combiWithReplacement(next, r - 1)) {
                yield [arr[i], ...c];
            }
        }
    }
}
```


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

## bit 연산
### bit 수 세기
```python
N = 21 # 0b10101
print(N.bit_length()) # 5
print((21).bit_length()) # 5

# error!
print(21.bit_length())
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
print(bin(a).count('1')) # 5
```

### 짝수를 홀수로, 홀수를 짝수로
2로 나누었을 때 몫이 같은 값의 짝/홀수로 바꾸기
```python
odd_a = 21
even_a = odd_a ^ 1

even_b = 30
odd_b = even_b | 1
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

### 두 값 비교
`max`, `min` 함수를 이용하는 것보다 `if-else`를 이용하는 것이 더 빠르다
```python
a, b = 100, 1

# 빠르다
max_val = a if a > b else b
min_val = a if a < b else b

# 느리다
max_val = max(a, b)
min_val = min(a, b)
```

### 누적합
```python
from itertools import accumulate

a = [1, 2, 3, 4, 5]

acc_a = [*accumulate(a)] # [1, 3, 6, 10, 15]
```

### 리스트 곱
```python
from math import prod
arr = [2, 3, 4, 5, 6]

print(prod(arr)) # 720
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

## 밀러-라빈 알고리즘을 이용한 소수 판별

```python
small_prime = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}

def miller_rabin(n, a):
    d = n-1
    while not d & 1:
        d >>= 1
        if pow(a, d, n) == n-1:
            return True
    if pow(a, d, n) == 1:
        return True
    return False


def is_prime(n):
    return n in small_prime or all(miller_rabin(n, a) for a in small_prime)
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

### 소인수 분해
간단하며 확실한 방법
```python
# { 소인수: 개수, ... }
def prime_factorization(x):
    if x == 1:
        return {1 : 1}
    ans = {}
    for i in range(2, int(x ** 0.5) + 1):
        while x % i == 0:
            ans[i] = ans.get(i, 0) + 1
            x //= i
    if x > 1:
        ans[x] = ans.get(x, 0) + 1
        
    return ans
```
밀러-라빈 알고리즘과 폴라드 로 알고리즘을 이용한 방법
```python
from random import randrange
from math import gcd

small_prime = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}
prime = {}

def miller_rabin(n, a):
    d = n-1
    while not d & 1:
        d >>= 1
        if pow(a, d, n) == n-1:
            return True
    if pow(a, d, n) == 1:
        return True
    return False


def is_prime(n):
    return n in small_prime or all(miller_rabin(n, a) for a in small_prime)


def pollard_rho(n):
    global prime
    if is_prime(n):
        prime[n] = prime.get(n, 0) + 1
        return
    if not n & 1:
        prime[2] = prime.get(2, 0) + 1
        pollard_rho(n//2)
        return
    x = y = randrange(2, n)
    c = randrange(1, n)
    d = 1

    while d == 1:
        x = (x ** 2 + c) % n
        y = (y ** 2 + c) % n
        y = (y ** 2 + c) % n
        d = gcd(abs(x - y), n)
        if d == n:
            pollard_rho(n)
            return

    pollard_rho(n//d)
    pollard_rho(d)

pollard_rho(720)
print(prime) # {2: 2, 7: 1, 3: 1, 5: 1}


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

### 세그먼트 트리

구간 합을 구해주는 코드를 작성
```python
arr = [*map(int, input().split())]
N = len(arr)

def init_tree():
    _2N = 2 * N
    tree = [0] * _2N
    # 리프 노드를 입력 받은 수열로 할당
    tree[N:_2N] = arr
    for i in range(N - 1, 0, -1):
        _2N = i * 2
        tree[i] = tree[_2N] + tree[_2N]

    return tree

# [start, end) 의 합을 구한다
def query(start, end):
    global tree
    ret = 0
    start += N
    end += N
    # 리프노드부터 더해나간다
    while start < end:
        if start % 2:
            ret += tree[start]
            start += 1
        if end % 2:
            end -= 1
            ret += tree[end]
        start //= 2
        end //= 2

    return ret

def update(idx, val):
    idx += N
    # 리프 노드 수정 후
    tree[idx] = val
    # 부모노드를 자식 노드를 이용해 수정해준다
    while idx > 1:
        tmp = idx // 2
        tree[tmp] = tree[idx] + tree[idx-1 if idx % 2 else idx+1]
        idx = tmp

        
tree = init_tree()
update(0, 1) # 0번째 값을 1로 바꾼다
print(query(3, 11)) # [3, 11) 범위의 값을 다 더해준다.
```

### 머지소트 트리
```python
arr = [*map(int, input().split())]
N = len(arr)

# ex) 수열 입력: 10, 50, 20, 60, 30, 70, 40, 90, 80
# 루트노드: [0(10), 1(50), 2(20), 3(60), 4(30), 5(70), 6(40), 7(90), 8(80)]
# 루트노드는 인덱스 순서로 정렬되며, 입력된 수열과 같은 순서를 가진다

# 리프노드: [0(10)], [2(20)], [4(30)], [6(40)], [1(50)], [3(60)], [5(70)], [8(80)], [7(90)]
# 리프노드는 입력된 수열이 정렬된 순서로 저장된다
def init_tree():
        # len(arr) -> size: 1 ~ 2 -> 2 / 3 ~ 4 -> 4 / 5 ~ 8 -> 8 / ... / 2^n + 1 ~ 2^(n+1) -> 2^(n+1)
        size = 1 << (N - 1).bit_length()
        # internal_node 의 개수는 (size - 1)개, 루트 노드의 인덱스는 1
        internal_node = [[] for _ in range(size)]
        # leaf_node 의 개수는 size개
        leaf_node = [[i] for i, value in sorted(enumerate(arr), key=lambda t: t[1])] + [[]] * (size - N)
        tree = internal_node + leaf_node
        # internal_node 를 초기화
        for i in range(size - 1, 0, -1):
            tree[i] = tree[2*i] + tree[2*i+1]
            tree[i].sort()
        return size, tree

size, tree = init_tree()
# k번째 수를 구하는 알고리즘
def query(start, end, k):
    idx = 1
    # 리프노드에 도달할 때까지 수행
    while idx < size:
        # 부모노드의 수열 중 작은 수들이 모여있는 왼쪽 자식노드의 수열에 대해
        # start ~ end 의 인덱스에 해당하는 수가 몇 개 있는지 계산
        # 왼쪽 자식은 정렬되어 있는 것은 아니지만 모든 원소가 오른쪽 자식노드보다 작다
        idx += idx
        node = tree[idx]
        count = bisect_left(node, end) - bisect_left(node, start)
        # 왼쪽 자식노드에 start ~ end 인덱스에 해당하는 수가 k보다 적다면 원하는 수는 오른쪽 자식 노드에 있다
        # 왜냐하면 왼쪽 자식노드는 정렬되어 있지는 않지만 모든 원소가 오른쪽 자식노드보다 작기 때문
        if count < k:
            idx += 1
            k -= count

    return arr[tree[idx][0]]

# 개수를 세주기 위해서 start - 1 을 해준다
# 인덱스는 1부터 시작
print(query(start - 1, end, k))
```

### 부분배열의 합
```python
from collections import Counter

arr = [1, 2, 3, 4]

def extend(brr):
    ret = [0]
    for b in brr:
        tmp = [b + c for c in ret]
        ret += tmp
    return ret

# Counter({0: 1, 1: 1, 2: 1, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 1, 9: 1, 10: 1})
count = Counter(extend(arr))
```