// 콜라츠 추측

function solution(num) {
    var answer = 0;
    while (answer < 500 && num != 1) {
        if (num % 2 == 0) {
            num /= 2
        } else {
            num = num*3 + 1
        }
        answer ++
    }
    
    answer = (answer === 500) ? -1 : answer; // 삼항 연산자 잘 사용하기 둘 중 하나 일 때
    
    return answer;
}