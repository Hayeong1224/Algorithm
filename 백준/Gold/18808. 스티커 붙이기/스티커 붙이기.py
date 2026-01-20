import sys
input = sys.stdin.readline

def rotate(sticker):
  R = len(sticker)
  C = len(sticker[0])
  
  # 가로x세로 -> 세로x가로니까 크기 변경
  new_sticker = [[0] * R for _ in range(C)]

  for r in range(R):
    for c in range(C):
      new_sticker[c][R-1-r] = sticker[r][c]

  return new_sticker

# x,y에 sticker의 i번째가 들어가는가?
def fit(x, y, sticker, notebook):
  R = len(sticker)
  C = len(sticker[0])

  if x + R > n or y + C > m:
    return False
  
  for r in range(R):
    for c in range(C):
      if sticker[r][c] == 1 and notebook[x+r][y+c] == 1:
        return False

  return True

# notebook에 붙이기
def attach(x, y, sticker, notebook):
  for r in range(len(sticker)):
    for c in range(len(sticker[0])):
      if sticker[r][c] == 1:
        notebook[x+r][y+c] = 1


n, m, k = map(int, input().split())
notebook = [[0] * m for _ in range(n)]
stickers = list()

for _ in range(k):
  r, c = map(int, input().split())
  temp = list()
  for i in range(r):
    row = list(map(int, input().split()))
    temp.append(row)
  stickers.append(temp)
  
for s in stickers:
  for i in range(4):
    if i != 0:
      s = rotate(s)
    is_attached = False  
    
    for r in range(n):
      for c in range(m):
        if fit(r,c,s,notebook):
          attach(r,c,s,notebook)
          is_attached = True
          break
      if is_attached: break
    if is_attached: break

total_count = sum(row.count(1) for row in notebook)
print(total_count)