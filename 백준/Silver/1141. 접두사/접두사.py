from itertools import combinations

n = int(input())
array = [input() for _ in range(n)]
array.sort() # 바로 다음 순서랑만 비교하면 됨

remove = [False] * n

for i in range(n-1):
  if array[i+1].startswith(array[i]):
    remove[i] = True
    
print(remove.count(False))