def solution(brown, yellow):
    # 1) brown + yellow = w*h
    # 2) yellow = (w-2) * (h-2)
    
    total = brown + yellow # total = w*h
    for h in range(3, int(total ** 0.5) + 1): # total의 약수 h,w 쌍 구하기. yellow가 존재하려면 h가 무조건 3 이상
        if total % h == 0:
            w = total // h
            
            if (w-2) * (h-2) == yellow:
                return [w,h] # h를 최소값부터 보니까 w>=h 만족