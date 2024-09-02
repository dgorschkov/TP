from sys import stdin

names = set()
for line in stdin:
    if len(line) <= 5:
        continue
    line = ' '.join(line.strip().split()[:2])
    names.add(line)
f = open('res.txt', mode='w+', encoding='utf8')
print(len(names), file=f)
print(*sorted(names), sep=', ', file=f)