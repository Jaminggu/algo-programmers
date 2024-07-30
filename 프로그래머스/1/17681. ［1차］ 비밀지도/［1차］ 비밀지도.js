function solution(n, arr1, arr2) {
    var answer = [];
    let binaryArr1 = arr1.map(num => num.toString(2).padStart(n, '0'));
    let binaryArr2 = arr2.map(num => num.toString(2).padStart(n, '0'));
    
    for(let i = 0; i < arr1.length; i ++) {
        answer.push("");
        
        for(let j = 0; j < n; j ++) {
            if(binaryArr1[i][j] === "1" || binaryArr2[i][j] === "1") {
                answer[i] += "#";
            } else {
                answer[i] += " ";
            }
        }
        
    }
    
    return answer;
}