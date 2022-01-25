from array import array
with open("input.txt", "r") as f:
    line = f.read()

fish_pool = [0]*9
for s_day in line.split(","):
    fish_pool[int(s_day)] += 1

# Part 1
fishes = array('Q', fish_pool)
for _ in range(80):
    rep_fish = fishes[0]
    fishes = fishes[1:] + array('Q', [rep_fish])
    fishes[6] += rep_fish

print(sum(fishes))

# Part 2
fishes = array('Q', fish_pool)
for _ in range(256):
    rep_fish = fishes[0]
    fishes = fishes[1:] + array('Q', [rep_fish])
    fishes[6] += rep_fish

print(sum(fishes))
