// 전화번호 목록

function solution(phone_book) {
    phone_book.sort(); 

    for (let i = 0; i < phone_book.length - 1; i++) {
        // startsWith() 접두사 반환 함수
        if (phone_book[i + 1].startsWith(phone_book[i])) {
            return false; // 접두사 관계 발견
        }
    }

    return true; // 전부 통과
}
