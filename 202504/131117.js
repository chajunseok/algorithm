// 할인 행사

function solution(want, number, discount) {
    var answer = 0;
    const buy_lst = {};

    for (let i = 0; i < want.length; i++) {
        buy_lst[want[i]] = number[i];
    }

    for (let day = 0; day <= discount.length - 10; day++) {
        let check_lst = {};

        for (let j = 0; j < 10; j++) {
            let item = discount[day + j];
            // 값이 없으면 초기화하고 +1 해야함
            check_lst[item] = (check_lst[item] || 0) + 1;
        }

        // dict 끼리 연산은 하나 하나 연산해야함
        let isSame = true;
        for (let key in buy_lst) {
            if (buy_lst[key] !== check_lst[key]) {
                isSame = false;
                break;
            }
        }

        if (isSame) {
            answer++;
        }
    }

    return answer;
}
