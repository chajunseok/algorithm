// 점프와 순간 이동

function solution(n) {
    let battery = 0;

    while (n > 0) {
        // 홀수면 점프
        if (n % 2 === 1) {
            n -= 1;
            battery += 1;
        } else {
            // 짝수면 순간이동
            n /= 2;
        }
    }

    return battery;
}
