with open("input.txt", "r") as f:
    commands = f.readlines()

# Part 1
hpos = 0
depth = 0
for cmd in commands:
    c, v = cmd.split(" ")
    
    if c == "forward":
        hpos += int(v)
    elif c == "up":
        depth -= int(v)
    else:
        depth += int(v)

print(hpos * depth)

# Part 2
aim = 0
hpos = 0
depth = 0
for cmd in commands:
    c, v = cmd.split(" ")
    
    if c == "forward":
        hpos += int(v)
        depth += aim * int(v)
    elif c == "up":
        aim -= int(v)
    else:
        aim += int(v)

print(hpos * depth)
