from bisect import bisect_left, bisect_right
def check(a, keyword_left, keyword_right):
    left = bisect_left(a, keyword_left)
    right = bisect_right(a, keyword_right)
    return right - left

def solution(words, queries):
    answer = []
    words_list = [[] for _ in range(100001)]
    reverse_words_list = [[] for _ in range(100001)]
    
    for w in words:
        words_list[len(w)].append(w)
        reverse_words_list[len(w)].append(w[::-1])
        
    for i in range(100001):
        words_list[i].sort()
        reverse_words_list[i].sort()
    
    for q in queries:
        if q[-1] == '?': # 접두사 -> words_list
            answer.append(check(words_list[len(q)], q.replace('?','a'), q.replace('?','z')))
        else: # 접미사 -> reverse_words_list
            answer.append(check(reverse_words_list[len(q)], q.replace('?','a')[::-1], q.replace('?','z')[::-1]))
    
    return answer