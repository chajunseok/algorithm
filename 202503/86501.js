// 없는 숫자 더하기

function solution(numbers) {
    var answer = 45;
    const numbers1 = [...Array(10).keys()] // range 배열 만드는 법 참고!!
    for (let num of numbers) {
        answer -= num
    }
    
    return answer;
}