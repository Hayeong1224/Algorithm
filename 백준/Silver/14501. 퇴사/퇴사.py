from itertools import combinations
n = int(input())

counsels = [] # [날짜, 시간, 금액] 
for i in range(n): # 불가능한 상담(n-1일 이후) 빼고 받기 
  t, p = map(int, input().split())
  if i+t <= n:
    counsels.append([i+1,t,p])

ans = 0
for i in range(1,len(counsels)+1):  
  for com in combinations(counsels, i):
    possible = True
    for j in range(i-1):
        d1,t1,_ = com[j]
        d2,_,_ = com[j+1]

        if d1+t1 > d2:
          possible = False
          break

    if possible:
      ans = max(ans, sum(c[2] for c in com))

print(ans)