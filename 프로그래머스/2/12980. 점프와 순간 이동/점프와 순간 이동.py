def solution(n):
    ans = 0
    
    while n:
        if n % 2 == 1:
            n = n - 1
            ans += 1
        n = n // 2

    return ans