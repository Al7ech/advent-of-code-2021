with open("input.txt", "r") as f:
    line = f.read()

pos = sorted(list(map(int, line.split(','))))

# Part 1
target_pos = pos[len(pos)//2]

print(sum([abs(p - target_pos) for p in pos]))

# Part 2
ans = int(1e+20)

for p in range(pos[0], pos[-1] + 1):
    s = 0
    for p2 in pos:
        d = abs(p2 - p)
        s += d*(d+1)//2
    ans = min(ans, s)

print(ans)