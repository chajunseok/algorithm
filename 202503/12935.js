// 제일 작은 수 제거하기

function solution(arr) {
    let min_num = Infinity;
    let min_idx = -1; 
    
    arr.forEach((num, idx) => { // idx 를 이용할 땐 forEach
        if (num < min_num) { 
            min_num = num;
            min_idx = idx;
        }
    });

    if (min_idx !== -1) {
        arr.splice(min_idx, 1);
    }
    
    arr = (arr.length === 0 ) ? [-1] : arr
    return arr;
}
