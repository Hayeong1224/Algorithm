# import sys
# sys.stdin = open("input.txt", "r")

def dfs(count, nums, visited):
    curV = int("".join(nums))

    # 가지 치기 - 그때 나온 값 리턴
    if (count, curV) in visited:
        return visited[(count, curV)]

    if count == 0:
        return curV

    # 가능한 두 곳 모두 교환
    local_max = 0
    n = len(nums)

    for i in range(n-1):
        for j in range(i+1, n):
            # 교환
            nums[i], nums[j] = nums[j], nums[i]

            # 다음 단계 재귀의 최댓값과 현재 max 비교
            result = dfs(count - 1, nums, visited)
            local_max = max(local_max, result)

            # 원상복구
            nums[i], nums[j] = nums[j], nums[i]

    visited[(count, curV)] = local_max
    return local_max

T = int(input())
for test_case in range(1, T+1):
    # 일단 횟수만큼 교환 -> 조합임 -> DFS
    number, target_count = input().split()
    nums = list(number)
    target_count = int(target_count)

    maxV = dfs(target_count, nums, {})

    print(f"#{test_case} {maxV}")