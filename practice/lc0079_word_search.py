def word_exists(matrix, word):
    rows, cols = len(matrix), len(matrix[0])
    # visited_path = set()  # using set, we lost the order
    visited_path = []  # change to use [], we can have the order othe path
    path_record = []

    def backtrack(r, c, i):
        if i == len(word):
            path_record.append(visited_path.copy())
            return True

        if (r < 0 or c < 0 or 
            r >= rows or c >= cols or
            word[i] != matrix[r][c] or
            (r,c) in visited_path):
            return False

        visited_path.append((r,c))
        # visited_path.add((r,c))
        res = (backtrack(r+1, c, i+1) or
               backtrack(r-1, c, i+1) or
               backtrack(r, c+1, i+1) or
               backtrack(r, c-1, i+1))
        # visited_path.remove((r,c))
        visited_path.pop()
        return res

    ret = backtrack(0, 0, 0)
    return (ret, path_record)

matrix = [["A", "B", "C", "E"],
          ["S", "F", "C", "S"],
          ["A", "D", "E", "E"]]
word = "ABCCED"
ret = word_exists(matrix, word)
print(ret)

