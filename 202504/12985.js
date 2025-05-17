// 예상 대진표

function solution(n, a, b) {
  var answer = 1;
  function check_game(a, b) {
    if (Math.floor((a + 1) / 2) === Math.floor((b + 1) / 2)) {
      return true;
    } else {
      return false;
    }
  }

  while (true) {
    if (check_game(a, b)) {
      break;
    } else {
      a = Math.ceil(a / 2);
      b = Math.ceil(b / 2);
      answer++;
    }
  }

  return answer;
}
