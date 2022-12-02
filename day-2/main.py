with open('day-2/inputs.txt', 'r') as f:
    inputs = f.readlines()

win_pts = { 'A': 2, 'B': 3, 'C': 1 }
draw_pts = { 'A': 1, 'B': 2, 'C': 3 }
lose_pts = { 'A': 3, 'B': 1, 'C': 2 }
score = 0
for line in inputs:
    match = line.strip().split(' ')

    if match[1] == 'Z':
        score += 6 + win_pts[match[0]]
    elif match[1] == 'Y':
        score += 3 + draw_pts[match[0]]
    else:
        score += lose_pts[match[0]]

print(score)
