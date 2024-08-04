def solution(today, terms, privacies):
    answer = []
    
    today_year, today_month, today_day = map(int, today.split('.'))
    
    terms_dict = {}
    for term in terms:
        key, value = term.split()
        terms_dict[key] = int(value)
    
    for idx, privacy in enumerate(privacies):
        date_str, term = privacy.split()
        year, month, day = map(int, date_str.split('.'))
        
        term_months = terms_dict[term]
        month += term_months
        
        while month > 12:
            month -= 12
            year += 1
        
        if (year < today_year or
            (year == today_year and month < today_month) or
            (year == today_year and month == today_month and day <= today_day)):
            answer.append(idx + 1)
        print(year, month, day, today)
    
    return answer
