// 이진 변환 반복하기

function solution(s) {
    let trans_cnt = 0;
    let zero_cnt = 0;
    let bin_num = s;

    while (bin_num !== "1") {
        const removed = bin_num.replace(/0/g, ""); // 0 제거
        zero_cnt += bin_num.length - removed.length; // 제거된 0 개수
        bin_num = removed.length.toString(2); // 길이를 이진수로 변환
        trans_cnt++;
    }

    return [trans_cnt, zero_cnt];
}
