with open('day-2/inputs.txt', 'r') as f:
    inputs = f.readlines()

score = 0
for line in inputs:
    match = line.strip().split(' ')
    if (match[0] == 'A' and match[1] == 'Y') or (match[0] == 'B' and match[1] == 'Z') or (match[0] == 'C' and match[1] == 'X'):
        score += 6

    elif (match[0] == 'A' and match[1] == 'X') or (match[0] == 'B' and match[1] == 'Y') or (match[0] == 'C' and match[1] == 'Z'):
        score += 3

    if match[1] == 'X':
        score += 1
    elif match[1] == 'Y':
        score += 2
    elif match[1] == 'Z':
        score += 3

print(score)
