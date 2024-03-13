import collections

with open("input.txt") as file:
    lines = [line.strip() for line in file]

m = {}
q = collections.deque()
for i, line in enumerate(lines):
    l = line.strip()
    for j, c in enumerate(l):
        m[(i,j)] = c
        if c == 'S':
            q.append((i,j))
        
steps = 0
total_p1 = 64
total = 26501365
directions = [(0,1),(-1,0),(0,-1),(1,0)]
viz = set()
quadratic = []
while steps < total:
    steps += 1
    new_q = collections.deque()
    viz = set()
    while len(q):
        x = q.popleft()
        row, col = x
        for d in directions:
            new_pos = (row+d[0], col+d[1])
            new_pos_ref = ((row+d[0])%len(lines), (col+d[1])%len(lines[0]))
            if m[new_pos_ref] != '#':
                if new_pos not in viz:
                    viz.add(new_pos)
                    new_q.append(new_pos)
    
    q = new_q
    if (steps % (len(lines)) == (total % len(lines))):
        quadratic.append(len(viz))
        if len(quadratic) == 3:
            import numpy
            xs = [i for i in range(3)]
            ys = [i for i in quadratic]
            f = numpy.polyfit(xs,ys,2)
            x = (total - (total % len(lines))) // len(lines)
            part2 = int(f[0]*x**2 + f[1]*x + f[2])
            print(part2)
            break
    if steps == total_p1:
        print(len(viz))

