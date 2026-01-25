def dfs(n, temp, op_list):
  global min_ans, max_ans
  
  if n == N:
    min_ans = min(min_ans, temp)
    max_ans = max(max_ans, temp)
    return

  if op_list[0] > 0:
    new_op = op_list.copy()
    new_op[0] -= 1
    dfs(n+1, temp+array[n], new_op)

  if op_list[1] > 0:
    new_op = op_list.copy()
    new_op[1] -= 1
    dfs(n+1, temp-array[n], new_op)

  if op_list[2] > 0:
    new_op = op_list.copy()
    new_op[2] -= 1
    dfs(n+1, temp*array[n], new_op)

  if op_list[3] > 0:
    new_op = op_list.copy()
    new_op[3] -= 1
    dfs(n+1, int(temp/array[n]), new_op)


N = int(input())
array = list(map(int, input().split()))
op = list(map(int, input().split()))
      
min_ans, max_ans = float('inf'), -float('inf')
dfs(1,array[0],op)
print(max_ans, min_ans, sep='\n')