def solution(n, m):
    answer = []
    
    for i in range(1, min(n, m) + 1):
        if(n % i == 0 and m % i == 0):
            gcd = i
    
    lcm = 1
    while(lcm % n != 0 or lcm % m != 0):
        lcm += 1
        
    answer.append(gcd)
    answer.append(lcm)
        
    return answer