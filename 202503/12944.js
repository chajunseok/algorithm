// 평균 구하기

function solution(arr) {
    var answer = 0;
    arr.forEach((val) => {
        answer += val
    })
    answer /= arr.length
    return answer;
}