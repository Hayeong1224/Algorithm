def solution(citations):
    citations.sort(reverse=True)
    h = len(citations)
    while(h > 0):
        count = 0
        for i in range(len(citations)):
            if citations[i] >= h:
                count += 1
        if count >= h:
            return h
        else:
            h -= 1
    return h