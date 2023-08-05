const fs = require('fs');
const input = fs.readFileSync('/dev/stdin', 'utf-8').toString().trim().split('\n');

const d = [[0, 1], [1, 0], [0, -1], [-1, 0]];

class Node {
    constructor(value, next = null) {
        this.value = value;
        this.next = next;
    }
}

class Queue {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    push(val) {
        const node = new Node(val);
        if (this.length === 0) {
            this.head = node;
        } else {
            this.tail.next = node;
        }
        this.tail = node
        this.length++;
    }

    dequeue() {
        if (this.length === 0) return null;

        this.length--;
        if (this.length === 0) {
            this.tail = null;
        }
        const ret = this.head;
        this.head = this.head.next;
        return ret.value;
    }

    get size() {
        return this.length;
    }
}

const solve = (R, C, board) => {
    const isOut = (r, c) => board[r]?.[c] === undefined;
    const que = new Queue();
    let pos = null;

    for (let i = 0; i < R; i++) {
        for (let j = 0; j < C; j++) {
            if (board[i][j] === 'F') {
                que.push([i, j, -1]);
            }
            else if (board[i][j] === 'J') {
                pos = [i, j, 1];
            }
        }
    }
    que.push(pos);

    while (que.size) {
        const [or, oc, time] = que.dequeue();
        for (const [dr, dc] of d) {
            const r = or + dr;
            const c = oc + dc;
            if (isOut(r, c)) {
                if (time > 0) return time;
            }
            else {
                if (board[r][c] !== '.') continue;
                board[r][c] = '#';
                que.push([r, c, time < 0 ? -1 : time + 1]);
            }
        }
    }

    return 'IMPOSSIBLE';
};

console.log(solve(...input[0].split(' ').map(Number), input.slice(1).map(el => el.split(''))));
