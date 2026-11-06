def solution(phone_book):
    book = {}
    for p in phone_book:
        book[p] = 1
        
    for p in phone_book:
        n = len(p)
        for i in range(1, n):
            if p[:i] in book:
                return False
        
    return True