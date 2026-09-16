def solution(citations):
    
    citations.sort(reverse=True) # 큰 순서대로 정렬
    answer = citations[0] # 최댓값부터 시작
    
    while answer >= 0:
        # answer 이상인 값의 수 >= answer면 return answer
        cnt = 0
        for c in citations:
            if c >= answer:
                cnt += 1
        if cnt >= answer:
            return answer
    
        answer -= 1