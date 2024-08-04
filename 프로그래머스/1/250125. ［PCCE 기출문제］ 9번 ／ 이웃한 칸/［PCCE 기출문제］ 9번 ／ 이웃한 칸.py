def solution(board, h, w):
    count = 0
    
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    for i in range(4):
        x = h + dh[i]
        y = w + dw[i]
        
        if x < 0: x = 0
        elif x == len(board): x = len(board) - 1
        
        if y < 0: y = 0
        elif y == len(board[0]): y = len(board[0]) - 1

        if x == h and y == w: count -= 1
            
        if(board[x][y] == board[h][w]):
            count += 1
    
    return count