def solution(n):
    seq = [1, 1]
    
    if n == 1:
        return 1
    
    for i in range(1, n):
        seq.append(seq[0] + seq[1])
        seq.pop(0)
    
    return seq[1] % 1234567