import queue
import functools


def is_bingo(board_to_check, numbers_drawn):
    for i in range(0, len(board_to_check)):
        if i % 5 == 0:  # Horizontal Check
            for j in range(i, i + 5):
                if board_to_check[j] not in numbers_drawn:
                    break
                elif j == i + 4:
                    return True
        if i < 5:  # Vertical check
            for j in range(i, len(board_to_check), 5):
                if board_to_check[j] not in numbers_drawn:
                    break
                elif j >= len(board_to_check) - 1:
                    return True


def generate_boards(input_lines):
    boards = []
    board = []
    for input_line in input_lines:
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


def __main__():
    with open('input.txt') as file:
        input_lines = file.read().splitlines()

    drawn_numbers_queue = queue.Queue()

    for line in input_lines.pop(0).split(','):
        drawn_numbers_queue.put(line)

    input_lines.pop(0)  # clear extra empty line
    generated_boards = generate_boards(input_lines)

    final_winning_board = None
    last_drawn_number = None
    visited = set()
    drawn_numbers = set()
    while not drawn_numbers_queue.empty() and len(visited) < len(generated_boards):
        last_drawn_number = drawn_numbers_queue.get()
        drawn_numbers.add(last_drawn_number)
        for i in range(0, len(generated_boards)):
            if i in visited:
                continue
            generated_board = generated_boards[i]
            if is_bingo(generated_board, drawn_numbers):
                if last_drawn_number == '30':
                    print(1)
                final_winning_board = generated_board
                visited.add(i)

    print("The last winning board's score is: "
          + str(calculate_score(final_winning_board, drawn_numbers, int(last_drawn_number))))


__main__()
