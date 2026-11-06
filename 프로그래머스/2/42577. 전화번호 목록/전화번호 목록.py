def solution(phone_book):
    book = {}
    phone_book.sort()
    for p in phone_book:
        n = len(p)
        for i in range(1, n+1):
            if p[:i] in book:
                return False
        
        book[p] = book.get(p, 0) + 1
        
    return True