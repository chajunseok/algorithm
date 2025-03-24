// 프로그래머스 자릿수 더하기

function solution(n)
{
    var answer = 0;
    const char = n.toString()
    for (let num of char) { // for of 는 이터러블에만 사용가능 숫자에 불가
        answer += Number(num)
    }

    return answer;
}