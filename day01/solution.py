with open("input.txt", "r") as f:
    depths = f.readlines()

depths = list(map(int, depths))

# Part 1
count = 0
for i in range(1, len(depths)):
    if depths[i-1] < depths[i]:
        count += 1

print(count)

# Part 2
def get_window_value(idx: int) -> int:
    return sum(depths[idx:idx+3])

count = 0
for i in range(0, len(depths)-3):
    if get_window_value(i) < get_window_value(i+1):
        count += 1

print(count)