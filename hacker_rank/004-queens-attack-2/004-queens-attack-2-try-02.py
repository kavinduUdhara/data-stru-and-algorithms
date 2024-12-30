#overall time complexity: O(k) where k = len(obstacles)
#in best case, time complextiy: O(1) if k == 0
def queensAttack(n, k, r_q, c_q, obstacles):
    closest_obs = {}
    if k > 0:
        closest_obs = find_close_obs(obstacles, r_q , c_q, n)
        print(closest_obs)
    move = {
        "left": min(closest_obs.get("left", n) -1, c_q - 1),
        "right": min(closest_obs.get("right", n) - 1, n - (c_q)),
        "top" : min(closest_obs.get("top", n) - 1, n-(r_q)),
        "bottom": min(closest_obs.get("bottom", n) -1, r_q -1),
    }
    move["top-left"] = min(closest_obs.get("top-left", n) -1, n-(r_q), c_q - 1)
    move["top-right"] = min(closest_obs.get("top-right", n) -1, n-(r_q), n - (c_q))
    move["bottom-left"] = min(closest_obs.get("bottom-left", n) -1, r_q -1,c_q - 1)
    move["bottom-right"] = min(closest_obs.get("bottom-right", n) -1, r_q -1, n - (c_q))
    print(move)
    total = 0
    for i in move.values():
        total += i
    print(total)
    return total

#time complexity: O(k) where k is the length of obstacles (l = len(obstacles))
def find_close_obs(obs:list, r_q:int, c_q:int, n:int)->dict:
    result = {}
    for i in obs:
        row = i[0]
        col = i[1]
        row_diff = row - r_q
        col_diff = col - c_q
        if abs(row_diff) == abs(col_diff):
            if row > r_q:#top
                if col > c_q:#right
                    result["top-right"] = min(result.get("top-right", n), abs(row_diff))
                else:#left
                    result["top-left"] = min(result.get("top-left", n), abs(row_diff))
            else:#bottom
                if col > c_q:#right
                    result["bottom-right"] = min(result.get("bottom-right", n), abs(row_diff))
                else:#left
                    result["bottom-left"] = min(result.get("bottom-left", n), abs(row_diff))
        elif row_diff == 0 or col_diff == 0:
            if row_diff == 0:#same-row (left/right)
                if col > c_q:#right
                    result["right"] = min(result.get("right", n), abs(col_diff))
                else:#left
                    result["left"] = min(result.get("left", n), abs(col_diff))
            else:#same-col (top/bottom)
                if row > r_q:#top
                    result["top"] = min(result.get("top", n), abs(row_diff))
                else: #bottom
                    result["bottom"] = min(result.get("bottom", n), abs(row_diff))
    return result

    


queensAttack(4, 0, 4, 4, [])
queensAttack(5, 3, 4, 3, [[5, 5], [4, 2], [2, 3]])
queensAttack(1, 0, 1, 1, [])
