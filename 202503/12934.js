// 정수 제곱근 판별

function solution(n) {
    var answer = 0;
    const devide = Math.sqrt(n) // 제곤근 구하는 함수 
    if (Number.isInteger(devide)) {      // 정수인지 판별하는 함수(Number을 붙여야함)
        answer = (devide+1) * (devide+1)
    } else {
        answer = -1
    }
    return answer;
}