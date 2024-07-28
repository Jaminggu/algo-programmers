function solution(numbers) {
    var answer = [];
    let temp = new Set();
    
    for(let i = 0; i < numbers.length - 1; i ++) {
        for(let j = i + 1; j < numbers.length; j ++) {
            temp.add(numbers[i] + numbers[j])
        }
    }
    
    answer = Array.from(temp).sort((a, b)=> a - b)
    
    return answer;
}