with open('./inputs.txt') as f:
    inputs = f.readlines()

chars = '.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

sum_priority = 0
for line in inputs:
    line = line.strip()
    mid = round(len(line) / 2)
    part_1 = line[:mid]
    part_2 = line[mid:]

    item = [w for w in part_1 if w in part_2][0]

    sum_priority += chars.index(item)

print(sum_priority)
