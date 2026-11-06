def solution(phone_book):
    book = {}
    for p in phone_book:
        book[p] = 1
        
    for p in phone_book:
        n = len(p)
        for i in range(1, n+1):
            if p[:i] in book and p[:i] != p:
                return False
        
    return True