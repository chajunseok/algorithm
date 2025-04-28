// 괄호 회전하기

function solution(s) {
    var answer = 0;
    let check_char = { ']': '[', ')': '(', '}': '{' };
    
    function check_text(array) {
        let stack = [];
        for (let val of array) {
            if (val === '[' || val === '{' || val === '(') {
                stack.push(val);
            } else {
                if (stack.length > 0 && stack[stack.length - 1] === check_char[val]) {
                    stack.pop();
                } else {
                    return false;
                }
            }
        }
        return stack.length === 0; // 스택이 비어 있어야 올바른 문자열
    }

    // 문자열을 배열로 변환
    let arr = s.split('');
    let turn_idx = 0;
    
    while (turn_idx < s.length) {
        if (check_text(arr)) {
            answer++;
        }
        // 한 칸 왼쪽 shift
        let tmp_char = arr.shift();
        arr.push(tmp_char);
        
        turn_idx++;
    }
    
    return answer;
}
