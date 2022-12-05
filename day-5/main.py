with open('./day-5/inputs.txt') as f:
    inputs = f.readlines()

# Split crates representation from the rearrangement procedure
structure = []
movements = []
for index, line in enumerate(inputs):
    line = line[:-1]

    if line == '':
        movements = inputs[index + 1:]
        break

    structure.append(line)

# Isolate stack number
stack_numbers = [n.strip() for n in structure[-1].split('  ')]

# Build dictionary representing the stack number and its crates
obj = {}
for n in stack_numbers:
    obj[n] = []
    for crates in structure[:-1]:
        crates = [crates[i:i + 4] for i in range(0, len(crates), 4)] # Split every 4 characters
        crate = crates[int(n) -1].strip()
        if crate != '':
            obj[n].append(crate[1])
    
    obj[n].reverse() # Reverse to get the stack from bottom to top

# Move crates
for movement in movements:
    movement = movement.strip().split(' ')
    for i in range(int(movement[1])):
        obj[movement[5]].append(obj[movement[3]].pop())

result = ''
for n in stack_numbers:
    result += obj[n][-1]

print(result)
