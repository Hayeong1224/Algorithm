def solve():
  N = int(input())
  p = [list(map(int, input().split())) for _ in range(N)]
  result = [0,0,0] # -1, 0, 1

  def check(r, c, size):
    # 현재 영역이 모두 같은 수인지 확인
    num = p[r][c]
    for i in range(r, r + size):
      for j in range(c, c + size):
        # 다르다면 9등분해서 재귀 호출
        if p[i][j] != num:
          new_size = size // 3
          for row in range(3):
            for col in range(3):
              check(r + row * new_size, c + col * new_size, new_size)
          return
    # 모두 같다면 카운드
    result[num+1] += 1
    
  check(0,0,N)
  
  for r in result:
    print(r)

solve()