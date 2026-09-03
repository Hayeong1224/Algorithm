def solution(clothes):
    cnt = 1
    cate_cnt = dict()
    
    for clothe in clothes:
        item, category = clothe
        cate_cnt[category] = cate_cnt.get(category, 0) + 1
    
    for val in cate_cnt.values():
        cnt *= (val + 1) # (수 + 안 입는 경우 1)
    
    # 다 안 입는 경우만 빼기
    return cnt - 1