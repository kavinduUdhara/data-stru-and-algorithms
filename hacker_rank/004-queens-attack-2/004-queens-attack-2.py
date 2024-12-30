def queensAttack(n, k, r_q, c_q, obstacles):
    left = c_q -1
    bottom = r_q -1
    top = n - (bottom + 1)
    right = n - (left + 1)
    top_left = min(left, top)
    top_right = min(top, right)
    bottom_left = min(bottom, left)
    bottom_right = min(bottom, right)

    if k == 0:
        pass
    else:
        for i in obstacles:
            row = i[0]
            col = i[1]
            row_diff = r_q - row
            col_diff = c_q - col
            if row_diff == 0:
                if col > c_q:
                    right = min(right, abs(col_diff) - 1)
                else:
                    left = min(left, abs(col_diff) -1)
            elif col_diff == 0:
                if row > r_q:
                    top = min(top, abs(row_diff) -1)
                else:
                    bottom = min(bottom, abs(row_diff) -1)
            elif abs(row_diff) == abs(col_diff):
                if row < r_q and col < c_q:
                    bottom_left = min(bottom_left, abs(col_diff) -1)
                elif row < r_q and col > c_q:
                    bottom_right = min(abs(col_diff) - 1, bottom_right)
                elif row > r_q and col > c_q:
                    top_left = min(top_left, abs(col_diff) -1)
                else:
                    top_right = min(top_right, abs(col_diff) -1)
            else:
                pass
    ans = top + left + right + bottom + top_left + top_right + bottom_left + bottom_right
    print(ans)
    return(ans)


queensAttack(4, 0, 4, 4, [])
queensAttack(5, 3, 4, 3, [[5, 5], [4, 2], [2, 3]])
queensAttack(1, 0, 1, 1, [])
