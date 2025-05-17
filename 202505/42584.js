// 주식가격

function solution(prices) {
  var answer = [];

  function find_down(currentIdx, array) {
    for (let i = currentIdx + 1; i < array.length; i++) {
      if (array[i] < array[currentIdx]) {
        return i - currentIdx;
      }
    }
    return array.length - currentIdx - 1;
  }

  prices.forEach((price, idx) => {
    answer.push(find_down(idx, prices));
  });
  return answer;
}
