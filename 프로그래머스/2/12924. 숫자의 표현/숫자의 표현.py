def solution(n):
    answer = 0
    
    for i in range(1, n + 1):
        num = i
        j = i + 1
        while num < n:
            num += j
            j += 1
        if num == n:
            answer += 1
    
    return answer