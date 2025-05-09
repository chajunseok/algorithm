// 기능 개발

function solution(progresses, speeds) {
    var answer = [];
    let day = []
    let max_day = 0
    progresses.forEach((progress, idx) => {
        const need_day = Math.ceil((100 - progress) / speeds[idx])
        if (idx === 0 ) {
            max_day = need_day
        }
        if (day.length > 0 && max_day < need_day) {
            answer.push(day.length)
            max_day = need_day
            day = [need_day]
        } else {
            day.push(need_day)
        }
    })
    answer.push(day.length)
    
    return answer;
}