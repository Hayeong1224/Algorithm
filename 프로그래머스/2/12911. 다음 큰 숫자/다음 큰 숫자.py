def solution(n):
    n2 = format(n, 'b')
    cnt = str(n2).count('1')
    
    while True:
        n += 1
        temp = format(n, 'b')
        if cnt == str(temp).count('1'):
            return n;