def solution(players, callings):
    answer = []
    player_positions = {player: idx for idx, player in enumerate(players)}
    
    for i in range(len(callings)):
        c_idx = player_positions[callings[i]]
        players[c_idx - 1], players[c_idx] = players[c_idx], players[c_idx - 1]

        player_positions[players[c_idx]] = c_idx
        player_positions[players[c_idx - 1]] = c_idx - 1
        
    return players