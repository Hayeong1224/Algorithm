from collections import deque
n = int(input())

q = deque([i for i in range(1,n+1)])

while len(q) != 1:
  # 제일 위에 있는 거 버리기
  q.popleft()
  # 제일 위에 있는 카드 제일 아래에 있는 카드 밑으로 옮기기
  top = q.popleft()
  q.append(top)

print(q.pop())