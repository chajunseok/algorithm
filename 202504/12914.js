// 멀리 뛰기

function solution(n) {
    let jump = Array(n + 1).fill(0);

    jump[1] = 1;
    jump[2] = 2;

    for (let i = 3; i <= n; i++) {
        jump[i] = (jump[i - 1] + jump[i - 2]) % 1234567; // mod 연산은 loof 안에서 해야함
    }

    return jump[n];
}