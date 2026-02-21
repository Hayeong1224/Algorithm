def solution(gems):
    n = len(gems)
    gems_type = len(set(gems))
    gems_dict = {}
    ans = [1,n]

    # 투포인터
    left, right = 0, 0
    # 오른쪽 보석 하나씩 추가
    for right in range(n):    
        gems_dict[gems[right]] = gems_dict.get(gems[right], 0) + 1
        
        while len(gems_dict) == gems_type:
            if (right - left) < (ans[1] - ans[0]):
                ans = [left+1, right+1]
                
            # 왼쪽 보석 하나씩 빼기
            gems_dict[gems[left]] -= 1
            if gems_dict[gems[left]] == 0:
                del gems_dict[gems[left]]
            left += 1
            
    return ans