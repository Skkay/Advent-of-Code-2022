with open('day-1/inputs.txt', 'r') as f:
    inputs = f.readlines()

max = 0
n = 0
for line in inputs:
    if line == '\n':
        if n > max:
            max = n
        n = 0
        continue

    n += int(line)

print(max)
