function solution(people, limit) {
    people.sort((a, b) => a - b); // 오름차순
    let answer = 0;
    let left = 0;
    let right = people.length - 1;

    while (left <= right) {
        if (people[left] + people[right] <= limit) {
            left++; // 같이 탈 수 있음
        }
        right--; // 무거운 사람은 무조건 태움
        answer++;
    }

    return answer;
}
