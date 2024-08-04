def solution(board, moves):
    answer = 0
    dolls = []
    
    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1] > 0:
                dolls.append(board[i][move - 1])
                board[i][move - 1] = 0
                break
        if len(dolls) >= 2 and dolls[-1] == dolls[-2]:
            dolls.pop()
            dolls.pop()
            answer += 2
    
    return answer