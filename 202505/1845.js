// 폰켓몬

function solution(nums) {
    var answer = 0;
    let ponketmon = {}
    nums.forEach((type) => {
        ponketmon[type] = (ponketmon[type] || 0) + 1;
    })
    
    const ponketmon_length = Object.keys(ponketmon).length
    answer = (nums.length / 2 > ponketmon_length) ? ponketmon_length : nums.length / 2;
    
    return answer;
}