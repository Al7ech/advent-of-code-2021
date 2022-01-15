import copy

with open("input.txt", "r") as f:
    reports = f.readlines()

reports = list(map(lambda x: x.strip(), reports))
    

# Part 1
def common_value(it, invert=False):

    l = len(it[0])
    ret = ''

    for i in range(l):
        bit_count = sum([int(r[i]) for r in it])
        if invert:
            ret += '0' if bit_count >= len(it)/2 else '1'
        else:
            ret += '1' if bit_count >= len(it)/2 else '0'

    return ret

l = len(reports[0])
gamma = common_value(reports)
epsilon = common_value(reports, invert=True)

print(int(gamma, 2) * int(epsilon, 2))

# Part 2
matches = copy.deepcopy(reports)

for i in range(l):
    c = common_value(matches)
    matches = [r for r in matches if r[i] == c[i]]
    if len(matches) == 1:
        o2 = int(matches[0], 2)
        break

matches = copy.deepcopy(reports)

for i in range(l):
    c = common_value(matches, invert=True)
    matches = [r for r in matches if r[i] == c[i]]
    if len(matches) == 1:
        co2 = int(matches[0], 2)
        break

print(o2 * co2)
