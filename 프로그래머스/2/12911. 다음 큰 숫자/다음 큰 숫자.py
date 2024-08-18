def solution(n):
    n_cnt1 = bin(n).count('1')
    
    num = n + 1
    while True:
        if bin(num).count('1') == n_cnt1:
            return num
        num += 1