def solution(a, b):
    weekends = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    endDate = [31, 29, 31, 30, 31, 30, 31, 31, 30, 30, 31]
    date = b + sum(endDate[0 : a - 1])
    
    return weekends[date % 7]