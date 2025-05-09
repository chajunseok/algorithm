// 의상

function solution(clothes) {
    var answer = 1;
    // 같은 거 끼리 묶기
    const comb = {};
    for (let i = 0; i < clothes.length; i++) {
        const type = clothes[i][1];
        comb[type] = (comb[type] || 0) + 1;
    }
    // 조합의 수 구하기
    // 3 1 1 -> 5 + 3 + 3 + 1 + 3 = 15
    // for...in 문은 객체의 "열거 가능한 속성(key)"을 순회할 때 사용하는 반복문입니다. 간단히 말해, 객체 안에 있는 키(key)         들을 하나씩 꺼낼 때 사용합니다.
    for (let type in comb) {
        answer *= comb[type] + 1
    }
    return answer - 1;
}