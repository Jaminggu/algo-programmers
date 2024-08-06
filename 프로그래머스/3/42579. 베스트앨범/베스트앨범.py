def solution(genres, plays):
    answer = []
    genres_dict = {}
    plays_dict = {}
    
    for idx in range(len(genres)):
        genre = genres[idx]
        play = plays[idx]
        
        if genre in plays_dict:
            plays_dict[genre] += play
        else:
            plays_dict[genre] = play
        
        if genre not in genres_dict:
            genres_dict[genre] = []
        genres_dict[genre].append((play, idx))
    
    sorted_genres = sorted(plays_dict.items(), key=lambda x: -x[1])
    
    for genre, _ in sorted_genres:
        sorted_songs = sorted(genres_dict[genre], key=lambda x: (-x[0], x[1]))
        answer.extend(song[1] for song in sorted_songs[:2])
    
    return answer
