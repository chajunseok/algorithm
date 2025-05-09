// 피로도

function solution(k, dungeons) {
    var answer = 0;
    // 방문 배열 선언
    let visit = Array(dungeons.length).fill(false)
    
    // 재귀 함수 선언
    function visitDungeons(life, visited, cnt) {
        // 최대 던전 갯수 갱신
        answer = Math.max(answer, cnt); 
        
        // 백트래킹
        for (let i = 0; i < dungeons.length; i++) {
            // 방문하지 않았고 최소 필요 피로도보다 현재 피로도가 높을 때 탐색
            if (!visited[i] && life >= dungeons[i][0]) {
                visited[i] = true;
                // 재귀 함수 호출
                visitDungeons(life - dungeons[i][1], visited, cnt + 1);
                visited[i] = false;
            }
        }
    }

    visitDungeons(k, visit, 0);
    return answer;
}
