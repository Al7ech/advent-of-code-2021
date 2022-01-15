import copy

with open("input.txt", "r") as f:
    lines = f.readlines()

class Vent:
    def __init__(self, vent_str):
        points = vent_str.split(' -> ')
        self.points = [list(map(int, point.split(","))) for point in points]
    
    def points_gen(self):
        dx = self.points[1][0] - self.points[0][0]
        dy = self.points[1][1] - self.points[0][1]
        div = max(abs(dx), abs(dy))
        delta = [dx//div, dy//div]

        c = copy.deepcopy(self.points[0])
        for i in range(div+1):
            yield c
            c[0] += delta[0]; c[1] += delta[1]


vents = []
count_p1 = [[0]*1000 for _ in range(1000)]
count_p2 = [[0]*1000 for _ in range(1000)]
for l in lines:
    vents.append(Vent(l))

for vent in vents:
    p1 = vent.points[0]
    p2 = vent.points[1]
    if (p1[0] == p2[0] or p1[1] == p2[1]):
        for p in vent.points_gen():
            count_p1[p[0]][p[1]] += 1
    for p in vent.points_gen():
        count_p2[p[0]][p[1]] += 1

ans_p1 = 0
ans_p2 = 0

for i in range(1000):
    for j in range(1000):
        ans_p1 += (count_p1[i][j] > 1)
        ans_p2 += (count_p2[i][j] > 1)

print(ans_p1, ans_p2)