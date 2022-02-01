with open("input.txt", "r") as f:
    lines = f.readlines()

octopuses = [list(map(int, line.strip())) for line in lines]
n = len(octopuses)
m = len(octopuses[0])

def is_valid_coordinate(i, j):
    return (-1 < i < n) and (-1 < j < m)

def increase(x1, y1, x2, y2):
    x1 = max(x1, 0)
    x2 = min(x2, n)
    y1 = max(y1, 0)
    y2 = min(y2, m)

    for i in range(x1, x2):
        for j in range(y1, y2):
            octopuses[i][j] += 1

part1_ans = 0
part2_ans = 1

while True:
    increase(0, 0, n, m)
    step_flashers = []
    while True:
        flashers = [(i, j) for i in range(0,n) for j in range(0,m) if octopuses[i][j] > 9]
        if not flashers:
            break
        for f in flashers:
            increase(f[0]-1, f[1]-1, f[0]+2, f[1]+2)
            octopuses[f[0]][f[1]] = 0
            if part2_ans < 101:
                part1_ans += 1

        step_flashers.extend(flashers)

    if len(step_flashers) == n * m:
        break

    for f in step_flashers:
        octopuses[f[0]][f[1]] = 0

    part2_ans += 1


print(part1_ans)
print(part2_ans)
