// JadenCase 문자열 만들기

function solution(s) {
    let result = "";
    let isStart = true;
  
    for (let char of s) { // split(" ") 연속된 공백에 대한 방지
      if (char === " ") { // 문자간 끊어짐 확인
        result += char;
        isStart = true; 
      } else {
        result += isStart ? char.toUpperCase() : char.toLowerCase();
        isStart = false;
      }
    }
  
    return result;
  }
  