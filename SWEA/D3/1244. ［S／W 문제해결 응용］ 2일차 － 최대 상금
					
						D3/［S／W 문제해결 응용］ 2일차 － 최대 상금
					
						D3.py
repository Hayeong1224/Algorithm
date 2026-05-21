# import sys
# sys.stdin = open("input.txt", "r")

def dfs(count):
    global maxV
    curV = int("".join(nums))

    # 가지 치기
    if (count, curV) in visited:
        return
    visited.add((count, curV))

    if count == target_count:
        maxV = max(maxV, curV)
        return

    # 가능한 두 곳 모두 교환
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1, n):
            nums[i], nums[j] = nums[j], nums[i]
            dfs(count + 1)
            nums[i], nums[j] = nums[j], nums[i]

T = int(input())
for test_case in range(1, T+1):
    # 일단 횟수만큼 교환 -> 조합임 -> DFS
    number, target_count = input().split()
    nums = list(number)
    target_count = int(target_count)

    maxV = 0
    visited = set()

    dfs(0)
    print(f"#{test_case} {maxV}")