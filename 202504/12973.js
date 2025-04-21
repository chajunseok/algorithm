// 짝지어 제거하기

function solution(s)
{
    var answer = -1;
    let stack = []
    for (let char of s) {
        if (stack.length > 0 && stack[stack.length - 1] === char) {
            stack.pop()
        } else {
            stack.push(char)
        }
    }
    
    return stack.length === 0 ? 1 : 0;
}