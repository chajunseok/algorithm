// n개의 최소공배수

function solution(arr) {
    // 최대공약수 구하는 공식
    const gcd = (a, b) => b === 0 ? a : gcd(b, a % b)
    // 최소공배수 구하는 공식
    const lcm = (a, b) => (a * b) / gcd(a, b)
    
    // reduce 함수는 배열의 값들을 하나로 줄여야 할 떄 유용하다.
    return arr.reduce((acc, curr) => lcm(acc, curr))
}
