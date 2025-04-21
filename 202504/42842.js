// 카펫

function solution(brown, yellow) {
    for (let height = 1; height <= Math.sqrt(yellow); height++) { // 노란색 영역을 기준으로 계산
        if (yellow % height === 0) {
            let width = yellow / height;

            let totalWidth = width + 2;
            let totalHeight = height + 2;

            let totalArea = totalWidth * totalHeight;
            let brownCheck = totalArea - yellow;

            if (brownCheck === brown) {
                return [totalWidth, totalHeight];
            }
        }
    }
}
