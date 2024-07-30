function solution(strings, n) {
    var answer = [];
    let sortedStrings = strings.sort();
    
    return sortedStrings.sort((a, b) => a.charCodeAt(n) - b.charCodeAt(n));
}