from itertools import permutations
N = int(input())
array = list(map(int, input().split()))
op = []
line = list(map(int, input().split()))
for i in range(4): # 0: +, 1:-, 2:*, 3://
  while line[i] > 0 :
    op.append(i)
    line[i] -= 1
      
min_ans, max_ans = float('inf'), -float('inf')
for p in set(permutations(op, N-1)):
  temp = array[0]
  for i in range(N-1):
    if p[i] == 0:
      temp += array[i+1]
    elif p[i] == 1:
      temp -= array[i+1]
    elif p[i] == 2:
      temp *= array[i+1]
    else:
      temp = int(temp / array[i+1])
      
  min_ans = min(min_ans, temp)
  max_ans = max(max_ans, temp)

print(max_ans, min_ans, sep='\n')