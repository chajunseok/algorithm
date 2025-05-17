// 프로세스 (우선순위 큐)

function solution(priorities, location) {
  let queue = priorities.map((priority, index) => [index, priority]);
  let count = 0;

  while (queue.length > 0) {
    const [currentIndex, currentPriority] = queue.shift();

    // 우선순위가 더 높은 프로세스가 있는지 확인
    const hasHigherPriority = queue.some(([_, p]) => p > currentPriority);

    if (hasHigherPriority) {
      // 다시 큐에 넣기
      queue.push([currentIndex, currentPriority]);
    } else {
      // 실행
      count++;
      if (currentIndex === location) {
        return count;
      }
    }
  }
}
