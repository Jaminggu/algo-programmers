function solution(s, n) {
    var answer = '';
    
    for (let i = 0; i < s.length; i++) {
         if (s[i] >= 'a' && s[i] <= 'z') {
            answer += String.fromCharCode((s.charCodeAt(i) - 97 + n) % 26 + 97);
        } else if (s[i] >= 'A' && s[i] <= 'Z') {
            answer += String.fromCharCode((s.charCodeAt(i) - 65 + n) % 26 + 65);
        } else {
            answer += s[i];
        }
    }
    
    return answer;
}