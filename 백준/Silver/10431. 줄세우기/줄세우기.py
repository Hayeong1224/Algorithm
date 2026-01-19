import sys
input = sys.stdin.readline

p = int(input())
for _ in range(p):
  line = list(map(int,input().split()))
  case_num, order = line[0], line[1:]
  ans = 0

  for i in range(len(order)-1):
    for j in range(i+1,len(order)):
      if order[i] > order[j]:
        ans += 1

  print(case_num, ans)