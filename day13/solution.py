with open("input.txt", "r") as f:
    lines = f.readlines()

idx = lines.index('\n')
input_lines = list(map(lambda x: x.strip().split(','), lines[:idx]))
query_lines = list(map(lambda x: x[11:].split('='),lines[idx+1:]))

dots = set()
def fold(side, value):
    edit_list = []
    if side == 'x':
        for x, y in dots:
            if x > value:
                edit_list.append((x, y))

        for x, y in edit_list:
            dots.remove((x, y))
            dots.add((2*value - x, y))

    elif side == 'y':
        for x, y in dots:
            if y > value:
                edit_list.append((x, y))

        for x, y in edit_list:
            dots.remove((x, y))
            dots.add((x, 2*value - y))

for x, y in input_lines:
    x = int(x)
    y = int(y)
    dots.add((x,y))

for idx, (side, value) in enumerate(query_lines):
    fold(side, int(value))

    # Part 1
    if not idx:
        print(len(dots))

maxes = [-1, -1]
for x, y in dots:
    maxes[0] = max(maxes[0], x+1)
    maxes[1] = max(maxes[1], y+1)

print_list = [[0]*maxes[0] for _ in range(maxes[1])]
for x, y in dots:
    print_list[y][x] = 1

# Part 2
for line in print_list:
    for char in line:
        print('*' if char else ' ', end='')
    print()