def solution(new_id):
    new_id = new_id.lower()
    id1 = ''
    
    for char in new_id:
        if char not in 'qwertyuiopasdfghjklzxcvbnm1234567890-_.': continue
        id1 += char
    
    id2 = ''
    for char in id1:
        if char == '.':
            if id2 and id2[-1] != '.':
                id2 += char
        else:
            id2 += char    
            
    if id2 and id2[0] == '.':
        id2 = id2[1:]
    if id2 and id2[-1] == '.':
        id2 = id2[:-1]
        
    if len(id2) == 0:
        id2 += 'a'
    
    if len(id2) >= 16:
        id2 = id2[0:15]
        if id2[-1] == '.': id2 = id2[:-1]
    elif len(id2) <= 2:
        append_char = id2[-1]
        for _ in range(3 - len(id2)):
            id2 += append_char
            
    
    return id2