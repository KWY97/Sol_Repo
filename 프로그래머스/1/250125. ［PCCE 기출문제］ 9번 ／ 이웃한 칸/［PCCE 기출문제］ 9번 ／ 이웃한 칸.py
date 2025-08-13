import sys
input = sys.stdin.readline

def solution(board, h, w):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    n = len(board)
    m = len(board[0])
    ans = 0

    point = board[h][w]

    for i in range(4):
        nx = h + dx[i]
        ny = w + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue

        if board[nx][ny] == point:
            ans += 1

    return ans