def solution(sizes):
    # 가로, 세로 중 큰 값을 가로로 몰고 작은 값을 세로로 몰아서 최대값 구하기
    w_max, h_max = 0, 0
    for w, h in sizes:
        if w < h:
            w, h = h, w
        w_max = max(w_max, w)
        h_max = max(h_max, h)
        
    return w_max * h_max