with open('input.txt') as file:
    directions = file.readlines()

xOffset = 0
yOffset = 0

for direction in directions:
    direction = direction.strip().split(' ')
    distance = int(direction[1])
    match direction[0]:
        case 'forward':
            xOffset += distance
        case 'down':
            yOffset += distance
        case 'up':
            yOffset -= distance

print('Total distance: ' + str(xOffset * yOffset))
