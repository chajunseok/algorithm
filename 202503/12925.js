// 프로그래머스 문자ㄹ을 정수로 바꾸기


function solution(s) {
    var answer = 0;
    let new_str = ''
    if (s[0] === '+') {
        new_str = s.substr(1)
    } else {
        new_str = s
    }
    
    answer = Number(new_str)
    
    return answer;
}