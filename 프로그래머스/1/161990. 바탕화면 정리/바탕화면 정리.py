def solution(wallpaper):
    answer = []
    lux = len(wallpaper) - 1
    luy = len(wallpaper[0]) - 1
    rdx = 0
    rdy = 0
    
    for xi, x in enumerate(wallpaper):
        for yi, y in enumerate(x):
            if wallpaper[xi][yi] == "#":
                if xi < lux:
                    lux = xi
                elif xi > rdx:
                    rdx = xi
                if yi < luy:
                    luy = yi
                elif yi > rdy:
                    rdy = yi
    rdx += 1
    rdy += 1
    
    if lux == rdx:
        rdx = lux + 1
    if luy == rdy:
        rdy = luy + 1

    answer.append(lux)
    answer.append(luy)
    answer.append(rdx)
    answer.append(rdy)
    
    return answer