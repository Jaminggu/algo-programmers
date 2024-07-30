function solution(a, b, n) {
    var answer = 0;
    let total = n;
    
    while(total >= a) {
        let bottle = Math.floor(total / a) * b;
        answer += bottle;
        total = (total % a) + bottle;
    }
    
    return answer;
}