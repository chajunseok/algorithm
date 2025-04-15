// 자연수 뒤집어 배열로 만들기

function solution(n) {
    var answer = [];
    const char = n.toString()
    for (let i = char.length-1; i>=0; i--) {
        answer.push(Number(char[i]))
    }
    return answer;
}