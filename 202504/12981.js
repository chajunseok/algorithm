// 영어 끝말잇기

function solution(n, words) {
    let usedWords = []
    let answer = [0, 0]
    for (let i = 0; i < words.length; i++) {
      const current = words[i]
      const prev = words[i - 1]
  
      // 중복 또는 끝말잇기 실패
      // includes 메소드는 배열의 중복을 확인하는 메소드
      // forEach 문은 return 이 되지 않음
      if (
        usedWords.includes(current) ||
        (i > 0 && prev[prev.length - 1] !== current[0])
      ) {
        answer = [(i % n) + 1, Math.floor(i / n) + 1];
        break;
      }
  
      usedWords.push(current);
    }
  
    return answer;
  }
  