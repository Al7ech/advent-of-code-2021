with open("input.txt", "r") as f:
    lines = f.readlines()

edge_list = list(map(lambda x: x.strip().split("-"), lines))
edge = {}
visit = {}

def count_paths_part1(p='start'):
    if p == 'end':
        return 1

    visit[p] += 1
    ret = sum(count_paths_part1(pt) for pt in edge[p] if (pt.isupper() or not visit[pt]))
    visit[p] -= 1

    return ret

visited_twice = False
def count_paths_part2(p='start'):
    if p == 'end':
        return 1

    global visited_twice

    visit[p] += 1
    if visit[p] > 1 and not p.isupper():
        visited_twice = True

    ret = sum(count_paths_part2(pt) for pt in edge[p] if ((pt.isupper() or (not visit[pt]) or (not visited_twice)) and pt != 'start'))
        
    if visit[p] > 1 and not p.isupper():
        visited_twice = False
    visit[p] -= 1

    return ret

for s, e in edge_list:
    visit[s] = 0
    visit[e] = 0

for v in visit.keys():
    edge[v] = []

for s, e in edge_list:
    edge[s].append(e)
    edge[e].append(s)
    
print(count_paths_part1())
print(count_paths_part2())
