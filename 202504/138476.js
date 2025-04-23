// 귤 고르기

function solution(k, tangerine) {
    var answer = 0;
    // 배열 중 가장 큰 수 구하기
    let max_num = Math.max(...tangerine)
    // counter 배열 만들기
    const numbers = Array(max_num+1).fill(0)
    // tangerine 순회하면서 counter 배열 채우기
    tangerine.forEach((fruit) => {
        numbers[fruit] ++
    })
    // 배열 역순으로 만들기
    numbers.sort((a, b) => b - a)
    // k 가 찰 때 까지 순회하기 answer ++
    let sum_fruit = 0
    for (let val of numbers) {
        if (sum_fruit >= k) break; // *** break 는 forEach에 동작하지 않는다.  *** //
        answer++;
        sum_fruit += val;
    }
    // k 가 다차는 순간 answer return 하기
    return answer;
}