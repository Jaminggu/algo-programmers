function solution(s) {
    var answer = [];
    let temp = {};
    
    for(let i = 0; i < s.length; i ++) {
        if(s[i] in temp) {
            answer.push(i - temp[s[i]]);
            temp[s[i]] = i;
        } else {
            temp[s[i]] = i;
            answer.push(-1);
        }
    }
    
    return answer;
}