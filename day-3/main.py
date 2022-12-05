with open('./inputs.txt') as f:
    inputs = f.readlines()

chars = '.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

sum_priority = 0
line_nb = -1
current_group = []
for line in inputs:
    line = line.strip()
    line_nb += 1

    if line_nb % 3 == 2:
        current_group.append(line)

        item = [w for w in current_group[0] if w in current_group[1] and w in current_group[2]][0]
        sum_priority += chars.index(item)

        current_group = []
        continue

    current_group.append(line)

print(sum_priority)
