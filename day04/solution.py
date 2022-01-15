import copy

with open("input.txt", "r") as f:
    lines = f.readlines()

numbers = list(map(int, lines.pop(0).split(",")))

class Bingo:
    def __init__(self, bingo_str):
        self.row = [0] * 5
        self.col = [0] * 5
        self.get_pos = {}
        self.sum = 0
        self.has_win = False

        for i in range(25):
            n = int(bingo_str[:2])
            bingo_str = bingo_str[3:]
            self.get_pos[n] = (i//5, i%5)
            self.sum += n
    
    def update(self, value):
        if self.has_win:
            return -1

        if value in self.get_pos:
            self.sum -= value

            y, x = self.get_pos[value]
            self.row[y] += 1
            self.col[x] += 1
            if self.row[y] == 5 or self.col[x] == 5:
                self.has_win = True
                return self.sum * value
        return -1

bingos = []
for i in range(1, len(lines), 6):
    bingos.append(Bingo(' '.join(lines[i:i+5]).replace('\n', '')))

has_win = False
first_win_value = -2
last_win_value = -2

for n in numbers:
    for b in bingos:
        r = b.update(n)
        if r != -1:
            # Part 2
            last_win_value = r
            # Part 1
            if first_win_value == -2:
                first_win_value = r

print(first_win_value, last_win_value)

            