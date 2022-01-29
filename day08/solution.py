from collections import Counter

with open("input.txt", "r") as f:
    lines = f.readlines()

query_mapper = {
    int('1110111', 2): 0,
    int('0100100', 2): 1,
    int('1011101', 2): 2,
    int('1101101', 2): 3,
    int('0101110', 2): 4,
    int('1101011', 2): 5,
    int('1111011', 2): 6,
    int('0100101', 2): 7,
    int('1111111', 2): 8,
    int('1101111', 2): 9
}

ans_count = 0
ans_sum = 0

for line in lines:
    hint, query = line.split(' | ')
    seg_count = {}
    ans = {}
    for seg in 'abcdefg':
        seg_count[seg] = hint.count(seg)

    pops = []
    for seg, count in seg_count.items():
        if count == 4:
            ans[seg] = 4
            pops.append(seg)
        if count == 6:
            ans[seg] = 1
            pops.append(seg)
        if count == 9:
            ans[seg] = 5
            pops.append(seg)

    for seg in pops:
        seg_count.pop(seg)

    pops = []
    for h in hint.split(' '):
        if len(h) == 4:
            for seg in h:
                if seg not in seg_count: continue
                if seg_count[seg] == 8:
                    ans[seg] = 2
                    pops.append(seg)
                elif seg_count[seg] == 7:
                    ans[seg] = 3
                    pops.append(seg)
    
    for seg in pops:
        seg_count.pop(seg)

    for seg, count in seg_count.items():
        if count == 8:
            ans[seg] = 0
        if count == 7:
            ans[seg] = 6

    ans_str = ''
    for q in query.split(' '):
        s = 0
        for seg in q.strip():
            s += (1 << ans[seg])
        
        ans_str += str(query_mapper[s])

    # Part 1
    c = Counter(ans_str)
    ans_count += sum([c[s] for s in '1478'])
    
    # Part 2
    ans_sum += int(ans_str)


# Part 1
print('count:',ans_count)
# Part 2
print('sum:', ans_sum)