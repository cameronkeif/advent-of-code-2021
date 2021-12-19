with open('input.txt') as file:
    directions = file.readlines()

xOffset = 0
yOffset = 0
aim =0

for direction in directions:
  direction = direction.strip().split(' ')
  magnitude = int(direction[1])

  match direction[0]:
    case 'forward':
      xOffset += magnitude
      yOffset += magnitude * aim
    case 'down':
      aim += magnitude
    case 'up':
      aim -= magnitude

print('Total distance: ' + str(xOffset * yOffset))
