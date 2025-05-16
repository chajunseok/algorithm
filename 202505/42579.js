// 베스트 앨범

function solution(genres, plays) {
    var answer = [];
    let genres_dict = {}
    genres.forEach((song, idx) => {
        genres_dict[song] = (genres_dict[song] || 0) + plays[idx]
    })
    // 몇가지 장르가 있는지 확인
    const entries = Object.entries(genres_dict);
    // 2. 배열을 값 기준으로 정렬 (비교 함수 사용)
    const sortedArray = entries.sort((a, b) => b[1] - a[1]);
    // 재생수의 합을 더함 -> sort
    let visited = Array(genres.length).fill(false)
    
    for (genre=0; genre < sortedArray.length; genre++) {
        let tmp_lst = []
        for (i=0; i<genres.length; i++) {
            // 장르 우선순위가 높은 순서의 곡들을 조회 -> 2곡만 뽑음 -> 배열을 만들고 (재생수, idx) 형태로 저장
            if (visited[i]) continue 
            if (sortedArray[genre][0] === genres[i]) {
                   // visited 배열 만들어서 중복으로 순회 안하게 함
                visited[i] = true
                tmp_lst.push([plays[i], i])
            }
        }
        // sort 1순위 재생수, 2순위 idx 순서
        tmp_lst.sort((a, b) => b[0] - a[0])
        for (let j = 0; j < Math.min(2, tmp_lst.length); j++) {
             // 다 순회하면 answer 에 넣음
            answer.push(tmp_lst[j][1]);
        }   
    }
    return answer;
}