with open('day-1/inputs.txt', 'r') as f:
    inputs = f.readlines()

max = []
n = 0
for line in inputs:
    if line == '\n':
        max.append(n)
        n = 0
        continue

    n += int(line)

max.sort(reverse=True)

print(sum(max[:3]))
