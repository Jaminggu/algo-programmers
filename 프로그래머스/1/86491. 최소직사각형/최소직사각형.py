def solution(sizes):
    answer = 0
    
    for i in range(len(sizes)):
        if sizes[i][1] > sizes[i][0]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
    
    max0 = 0
    max1 = 0
    
    for i in range(len(sizes)):
        if sizes[i][0] > max0:
            max0 = sizes[i][0]
        if sizes[i][1] > max1:
            max1 = sizes[i][1]
            
    return max0 * max1