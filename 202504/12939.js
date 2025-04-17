// 프로그래머스 최솟값과 최댓값

function solution(s) {
    const numbers = s.split(" ").sort((a, b) => a - b)
    var answer = '';
    answer += numbers[0] + " " + numbers[numbers.length - 1]
    return answer;
}