from itertools import product
def solution(word):
    # 다 만들고 정렬
    vowels = ['A', 'E', 'I', 'O', 'U']
    word_list = []
    for i in range(1, 6):
        for pr in product(vowels, repeat=i):
            word_list.append(''.join(pr))

    word_list.sort()
    
    return word_list.index(word) + 1

    
    
    