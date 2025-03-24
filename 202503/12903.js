// 가운데 글자 가져오기

function solution(s) {
    var answer = '';
    if (s.length % 2 == 0) {
        answer += s[s.length/2-1] 
        answer += s[s.length/2] 
    } else {
        answer += s[Math.round(s.length/2)-1] // 반올림
    }
    return answer;
}