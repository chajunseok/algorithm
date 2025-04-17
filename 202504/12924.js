// 다음 큰 숫자

function solution(n) {
    // 2진 문자열에서 '1'의 개수를 세는 함수
    const countOnes = bin => bin.split('1').length - 1;
      
    // 기준값  
    let cur = n            
    const ones = countOnes(n.toString(2));
  
    // 1씩 늘리며 같은 1‑개수를 찾는다
    while (true) {
      cur += 1;                      
      if (countOnes(cur.toString(2)) === ones) {
        return Number(cur);          
      }
    }
  }
  