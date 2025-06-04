def get_receiver_top_orders(n, heights):
    stack = []  # (인덱스, 높이) 저장
    ans = [0] * n

    for i in range(n):
        while stack and stack[-1][1] <= heights[i]:
            stack.pop()

        if stack:
            ans[i] = stack[-1][0] + 1

        stack.append([i, heights[i]])

    return ans


N = int(input())
towers = list(map(int, input().split()))
ans = get_receiver_top_orders(N, towers)
print(' '.join(map(str, ans)))