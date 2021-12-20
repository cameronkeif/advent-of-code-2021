import queue


def is_bingo(board_to_check, numbers_drawn):
    for i in range(0, len(board_to_check)):
        if i % 5 == 0:
            for j in range(i, i + 5):
                if board_to_check[j] not in numbers_drawn:
                    break
                elif j == i + 4:
                    return True
        if i < 5:
            for j in range(i, len(board_to_check), 5):
                if board_to_check[j] not in numbers_drawn:
                    break
                elif j >= len(board_to_check) - 1:
                    return True


def generate_boards():
    boards = []
    board = []
    for input_line in inputLines:
        if input_line == '':
            boards.append(board)
            board = []
        else:
            board += input_line.strip().replace('  ', ' ').split(' ')

    return boards


def calculate_score(board_to_score, numbers_drawn, final_number):
    computed_sum = 0
    for num in board_to_score:
        if num not in numbers_drawn:
            computed_sum += int(num)

    return computed_sum * final_number


with open('input.txt') as file:
    inputLines = file.read().splitlines()

drawnNumbersQueue = queue.Queue()

for line in inputLines.pop(0).split(','):
    drawnNumbersQueue.put(line)

inputLines.pop(0)  # clear extra empty line

drawnNumbers = set()
generated_boards = generate_boards()

winning_board = None
last_drawn_number = None
while not drawnNumbersQueue.empty() and not winning_board:
    last_drawn_number = drawnNumbersQueue.get()
    drawnNumbers.add(last_drawn_number)
    for generated_board in generated_boards:
        if is_bingo(generated_board, drawnNumbers):
            winning_board = generated_board
            break

print(calculate_score(winning_board, drawnNumbers, int(last_drawn_number)))
