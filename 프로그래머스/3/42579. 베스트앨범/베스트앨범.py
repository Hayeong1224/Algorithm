def solution(genres, plays):
    
    genre_num = dict()
    genre_plays = dict()
    
    for i in range(len(genres)):
        genre_num[genres[i]] = genre_num.get(genres[i], []) + [i]
        genre_plays[genres[i]] = genre_plays.get(genres[i], 0) + plays[i]
        
    # 많이 재생된 장르 순
    genre_sort = sorted(list(set(genres)), key = lambda x: -genre_plays[x])
    print(genre_sort)
    answer = []
    for genre in genre_sort:
        if len(genre_num[genre]) == 1:
            answer += genre_num[genre]
        else:    
            song_sort = sorted(genre_num[genre], key=lambda x: [plays[x], -x], reverse=True)
            answer += song_sort[:2]
        
    return answer 