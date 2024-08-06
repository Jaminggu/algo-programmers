function solution(priorities, location) {
    let index = 0;
    let arr = [];
    let max = Math.max(...priorities);
    let answer = 0;
    
    for(let i = 0; i < priorities.length; i ++) {
        arr.push(i);
    }
    
    while(priorities.length != 0) {
        max = Math.max(...priorities);
        
        if(priorities[0] < max) {
            priorities.push(priorities.shift());
            arr.push(arr.shift());
        } else {
            answer ++;
            priorities.shift();
            
            if(arr.shift() == location) {
                return answer;
            }
        }
        
    }
}