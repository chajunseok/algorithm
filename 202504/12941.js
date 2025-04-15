// 프로그래머스 최솟값 만들기

function solution(A,B){
    var answer = 0;
    A.sort((a, b) => a - b) // 가장 작은거랑 
    B.sort((a, b) => b - a) // 가장 큰거랑 곱해야 제일 작겠지
    for (let idx=0; idx<A.length; idx++) {
        answer += A[idx] * B[idx]
    }

    return answer;
}