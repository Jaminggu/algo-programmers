function solution(operations) {
    var queue = [];
    
    for(let i = 0; i < operations.length; i ++) {
        let [sign, num] = operations[i].split(' ');
        
        if(sign == 'I') {
            queue.push(parseFloat(num));
        } else {
            if(num == '1') {
                queue.pop();
            } else {
                queue.shift();
            }
        }
        queue.sort((a, b) => a - b);
    }
    
    return queue.length == 0 ? [0, 0] : [Math.max(...queue), Math.min(...queue)];
}