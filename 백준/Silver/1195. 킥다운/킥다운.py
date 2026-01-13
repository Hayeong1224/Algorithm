f_gear = input().strip()
s_gear = input().strip()

n, m = len(f_gear), len(s_gear)

# 모든 가능한 시작점 d (f의 시작점): -n부터 m까지
ans = n+m

for d in range(-n, m+1):
  check = True
  for i in range(n):
    # i + d는 s_gear의 인덱스, 이 값이 유효한 범위(0~m-1)일 때만 체크
    if 0 <= i + d < m:
      if f_gear[i] == '2' and s_gear[i+d] == '2':
        check = False
        break

  if check:
    #현재 위치 d에서 겹쳤을 때 전체 길이
    #왼쪽 끝은 min(0,d), 오른쪽 끝은 max(m, d+n)
    left = min(0,d)
    right = max(m, d+n)
    ans = min(ans, right - left)

print(ans)