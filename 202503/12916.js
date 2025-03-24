// 문자열 내 p와 y의 개수

function solution(s){
    var answer = true;
    let y_answer = 0
    let p_answer = 0
    
    s.split("").forEach((val) => {
        if (val.toLowerCase() === 'y') {
            y_answer ++
        } else if (val.toLowerCase() === 'p') {
            p_answer ++
        }
    })
    
    if (y_answer != p_answer) {
        answer = false
    }

    return answer;
}