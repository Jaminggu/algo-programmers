def solution(numbers):
    answer = 0
    i = 0
    
    for n in range(10):
        if i not in numbers: answer += i
        i += 1
    
    return answer