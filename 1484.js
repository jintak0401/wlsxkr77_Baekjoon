const fs = require('fs')

function solve() {
    const G = parseInt(fs.readFileSync("/dev/stdin").toString());

    let cur = 2, past = 1;
    const ans = [];
    while (past < cur) {
        const val = (cur + past) * (cur - past);
        if (val < G) cur++;
        else if (val > G) past++;
        else {
            ans.push(cur);
            cur++;
        }
    }

    if (ans.length === 0) console.log(-1);
    else ans.forEach((val) => console.log(val))
}

solve();
