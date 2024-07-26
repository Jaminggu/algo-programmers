def solution(n):
    answer = ''
    
    while(n):
        answer = str(n % 3) + answer
        n = n // 3
    
    answer = answer[::-1]
    
    an = 0
    power = 1
    for i in reversed(answer):
        an += int(i) * power
        power *= 3
    
    return an