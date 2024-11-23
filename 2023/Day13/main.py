# Refactored mostly by gpt to correspond with the readability of the case.
f = lambda p, s: next((i for i in range(len(p)) if sum(c != d for l, m in zip(p[i-1::-1], p[i:]) for c, d in zip(l, m)) == s), 0)
print('\n'.join(str(sum(100 * f(p, s) + f([*zip(*p)], s) for p in map(str.split, open('input.txt').read().strip().split('\n\n')))) for s in [0, 1]))
