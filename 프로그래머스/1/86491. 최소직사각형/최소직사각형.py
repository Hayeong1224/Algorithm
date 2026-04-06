def solution(sizes):
    # 둘 중 큰 걸 한 쪽으로 몰아버리자!
    mw, mh = 0, 0
    for w, h in sizes:
        temp_w = max(w, h)
        temp_h = min(w, h)
        mw = max(mw, temp_w)
        mh = max(mh, temp_h)
    return mw * mh 