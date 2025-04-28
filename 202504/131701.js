// 연속 부분 수열 합의 개수

function solution(elements) {
    var answer = 0;
    const new_elements = [...elements, ...elements]
    // set 선언
    let numbers = new Set()
    // for문을 순회 1개부터 n개까지 n-1까지
    for (let i=0; i<elements.length; i++) {
        for (let j=0; j<elements.length; j++) {
            let tmp_sum = 0
            for (let k=0; k<=i; k++) {
                tmp_sum += new_elements[j+k]
            }
            numbers.add(tmp_sum) // set의 원소 추가하는 메소든 뺴는 건 delete
        }
    }
    answer = numbers.size // set의 원소 갯수를 세는 메소드 size
    return answer;
}