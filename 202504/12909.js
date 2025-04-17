// 프로그래머스 올바른 괄호

function solution(s) {
    const stack = [];

    for (let val of s) { // 문자열에는 of 를 쓰자
        if (val === '(') {
            stack.push(val);
        } else {
            if (stack.length > 0 && stack[stack.length - 1] === '(') {
                stack.pop();
            } else {
                return false;
            }
        }
    }

    return stack.length === 0; // true 반환
}
