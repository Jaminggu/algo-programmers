function solution(s){
    let stack = [];
    
    if(s[0] === ')') return false;
    
    for(let i = 0; i < s.length; i ++) {
        s[i] === '(' ? stack.push(1) : stack.pop();
    }
    
    return stack.length === 0;
}