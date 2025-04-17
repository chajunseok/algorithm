function solution(n) {
    // 1) 2의 거듭제곱 인수를 제거해 n을 홀수로
    while (n % 2 === 0) n >>= 1;
  
    // 2) 남은 홀수 부분의 약수 개수 계산
    let answer = 1;
    for (let p = 3; p * p <= n; p += 2) {
      if (n % p === 0) {
        let cnt = 0;
        while (n % p === 0) { n /= p; cnt++; }
        answer *= (cnt + 1);              // (지수+1)만큼 경우의 수 곱
      }
    }
    if (n > 1) answer *= 2;               // 마지막 소인수가 남으면 ×2
    return answer;
  }
  