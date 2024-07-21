def solution(x):
    temp = x
    total = 0
    
    while(temp != 0):
        total += temp % 10
        temp //= 10
    
    return (x % total == 0)