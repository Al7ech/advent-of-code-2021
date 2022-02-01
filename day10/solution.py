with open("input.txt", "r") as f:
    lines = f.readlines()

pairs = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,

    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

part1_ans = 0
part2_list = []

for line in lines:
    stack = []
    corrupted = False
    for char in line.strip():
        if char in pairs.values():
            stack.append(char)
        else:
            if stack and pairs[char] == stack[-1]:
                stack.pop()
            else:
                part1_ans += points[char]
                corrupted = True
                break
    
    if not corrupted and stack:
        score = 0
        for s in stack[::-1]:
            score = score * 5 + points[s]
        part2_list.append(score)

print(part1_ans)
print(sorted(part2_list)[len(part2_list)//2])
