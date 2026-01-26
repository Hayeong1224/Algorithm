data = [list(map(int, input())) for _ in range(4)]
K = int(input())

# 맞닿는 부분(L,R) 관리
p = [[6,2] for _ in range(4)]

def rotate(i, d, l_check, r_check):
  global p
  if not l_check and 0 < i and data[i][p[i][0]] != data[i-1][p[i-1][1]]:
    rotate(i-1,-d,False,True)
  if not r_check and i < 3 and data[i][p[i][1]] != data[i+1][p[i+1][0]]:
    rotate(i+1,-d,True,False)

  if d == -1: # 반시계
    p[i][0], p[i][1] = (p[i][0]+1)%8, (p[i][1]+1)%8
  else: # 시계
    p[i][0], p[i][1] = (p[i][0]+7)%8, (p[i][1]+7)%8

for i in range(K):
  # 톱니바퀴 번호, 방향
  num, d = map(int, input().split())
  rotate(num-1, d, False, False)

ans = 0
for i in range(4):
  if data[i][(p[i][0]+2)%8] == 1:
    ans += 2 ** i

print(ans)