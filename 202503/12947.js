// 하샤드 수

function solution(x) {
    var answer = true;
    let sum = 0
    for (let num of x.toString()) {
        sum += Number(num)
    }
    if (x % sum != 0) {
        answer = false
    }
    
    return answer;
}