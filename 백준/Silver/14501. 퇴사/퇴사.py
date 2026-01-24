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
    temp = 0
    if i != 1:
      for j in range(i-1):
        d1,t1,p1 = com[j]
        d2,t2,p2 = com[j+1]
        if d1+t1 > d2:
          temp = 0
          break
      
        temp += (p1+p2) if j == i-2 else p1
    else:
      temp += com[0][2]
    ans = max(ans, temp)

print(ans)