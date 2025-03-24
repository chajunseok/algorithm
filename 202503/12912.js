// 두 정수 사이의 합

function solution(a, b) {
    var answer = 0;
    const tmp = a
    if (b < a) {
        [b, a] = [a, b] // 두 수의 합 바꿀때 이렇게 바꾸면 가능!
    }
    
    for (let i = a; i <= b; i++) {
        answer += i
    }
    return answer;
}