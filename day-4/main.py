with open('./inputs.txt') as f:
    inputs = f.readlines()

sum = 0
for line in inputs:
    line = line.strip()
    pair = line.split(',')

    pair_1_from = int(pair[0].split('-')[0])
    pair_1_to = int(pair[0].split('-')[1])

    pair_2_from = int(pair[1].split('-')[0])
    pair_2_to = int(pair[1].split('-')[1])

    if (pair_2_from >= pair_1_from and pair_2_to <= pair_1_to) or (pair_1_from >= pair_2_from and pair_1_to <= pair_2_to):
        sum += 1

print(sum)
