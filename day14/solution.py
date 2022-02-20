from collections import Counter
from string import ascii_uppercase

max_step = 45

with open("input.txt", "r") as f:
    lines = f.readlines()

polymer = lines[0].strip()
rules = {}
d = {}

def get_empty_dict():
    ret = {}
    for char in ascii_uppercase:
        ret[char] = 0

    return ret

def add_up(dict_list):
    ret = get_empty_dict()
    for d in dict_list:
        for k, v in d.items():
            ret[k] += v
    return ret

def polymer_collection(step=10):
    ret = add_up(rule_collection(polymer[i:i+2], step) for i in range(len(polymer) - 1))
    for char in polymer[1:-1]:
        ret[char] -= 1
    return ret

def rule_collection(rule, step):
    if d[rule][step]:
        return d[rule][step]
    
    d[rule][step] = add_up([rule_collection(rule[0] + rules[rule], step-1), rule_collection(rules[rule] + rule[1], step-1)])
    d[rule][step][rules[rule]] -= 1
    return d[rule][step]

for line in lines[2:]:
    line = line.strip()
    k, v = line.split(' -> ')
    rules[k] = v
    init_dict = get_empty_dict()
    init_dict[k[0]] += 1
    init_dict[k[1]] += 1
    d[k] = [init_dict] + [None] * (max_step - 1)

values = [v for v in polymer_collection().values() if v]
print(max(values) - min(values))

values = [v for v in polymer_collection(40).values() if v]
print(max(values) - min(values))