def valid_solution(board):
    for i in range(9):
        # column check
        col_check = []
        for row in board:
            if 0 in row:
                return False
            if row[i] in col_check:
                return False
            col_check.append(row[i])
            # row check
            row_check = []
            for row_i in range(9):
                if row[row_i] in row_check:
                    return False
                row_check.append(row[row_i])
    # 3x3 grid check
    for col in [(0,3),(3,6),(6,9)]:
        for g in [(0,3),(3,6),(6,9)]:
            grid_sum = 0
            for r in range(col[0],col[1]):
                grid_sum += sum(board[r][g[0]:g[1]])
            if grid_sum != 45:
                return False
    return True
