// 튜플

function solution(s) {
    var answer = [];
    let repeat = []
    //  집합 배열 parse
    const parsed = JSON.parse(s.replace(/{/g, "[").replace(/}/g, "]"));
    // 배열의 길이 순서대로 sort
    parsed.sort((a, b) =>  a.length - b.length)
    // 순서 배열 선언
    let count = Array(parsed.length).fill(0)
    // 배열의 순서 찾기
    parsed.forEach((val, idx) => {
        val.forEach((add_val) => {
            // includes 로 이미 나온 문자인지 확인
            if (!repeat.includes(add_val)) {
                repeat.push(add_val)
                // 없을 경우 새로운 idx에 추가
                count[idx] = add_val
            } 
        })
    })
    answer = count
    return answer;
}