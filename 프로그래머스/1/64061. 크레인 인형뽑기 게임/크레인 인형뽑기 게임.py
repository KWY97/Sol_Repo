def solution(board, moves):
    answer = 0
    n = len(board)
    stack = []

    for move in moves:
        target_index = move - 1

        for i in range(n):
            if board[i][target_index] == 0:
                continue
            stack.append(board[i][target_index])
            board[i][target_index] = 0

            if len(stack) == 1:
                break
            elif stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2
                break
            else:
                break
    return answer