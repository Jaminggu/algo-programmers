function solution(A, B) {
    let B_score = 0;
    
    A.sort((a, b) => a - b);
    B.sort((a, b) => a - b);
    
    let j = 0;
    
    for (let i = 0; i < B.length; i ++) {
        if (B[i] > A[j]) {
            B_score ++;
            j ++;  
        }

        if (j === A.length) break;
    }
        
    return B_score;
}
