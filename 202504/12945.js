// 피보나치 수

function solution(n) {
    let a = 0, b = 1; // 배열 대신 변수 2개만 사용해서 메모리를 줄이고 시간도 절약할 수 있다.

    for (let i = 2; i <= n; i++) {
        const next = (a + b) % 1234567;
        a = b;
        b = next;
    }

    return n === 0 ? a : b;
}
