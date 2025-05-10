function solution(n, works) {
    let answer = 0;

    works.sort((a, b) => b - a);

    for (let i = 0; i < n; i++) {
        if (works[0] === 0) break;
        works[0]--;

        let j = 0;
        while (j + 1 < works.length && works[j] < works[j + 1]) {
            [works[j], works[j + 1]] = [works[j + 1], works[j]];
            j++;
        }
    }

    for (let i = 0; i < works.length; i++) {
        answer += works[i] ** 2;
    }

    return answer;
}
