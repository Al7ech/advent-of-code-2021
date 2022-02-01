import math


with open("input.txt", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    lines[i] = list(map(int, line.strip()))

n = len(lines)
m = len(lines[0])

moveable = [[1, 0], [0, -1], [0, 1], [-1, 0]]

def is_valid_coordinate(i, j):
    return (-1 < i < n) and (-1 < j < m)

ans = 0
basin_sizes = []
count = 0

def get_basin_size(i, j):
    if lines[i][j] == 9:
        return 0
    lines[i][j] = 9
    
    ret_list = [get_basin_size(i+d[0], j+d[1]) for d in moveable if is_valid_coordinate(i+d[0], j+d[1])]
    return sum(ret_list) + 1

for i in range(n):
    for j in range(m):
        check_list = []
        for d in moveable:
            new_i = i + d[0]
            new_j = j + d[1]
            if is_valid_coordinate(new_i, new_j):
                check_list.append(lines[new_i][new_j])

        v = lines[i][j]
        if sum(v<c for c in check_list) == len(check_list):
            basin_sizes.append(get_basin_size(i, j))
            ans += 1 + v

# Part 1
print(ans)
# Part 2
print(math.prod(sorted(basin_sizes, reverse=True)[:3]))
