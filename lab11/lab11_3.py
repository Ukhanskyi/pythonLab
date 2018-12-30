#!/usr/bin/env python3
# -*-codding:utf-8 -*-


# Завдання реалізувати гру "хрестики-ноліки" людини з компютером. Гра
# відбувається на квадратному полі розміром 3 х 3. Гравці (компютер
# і людина) ставлять свої позначки (X та 0) під час свого ходу на
# вільні місця на полі. Той хто починає, ставить Х. Той хто сформує
# повну лінію з трьох позначок (три X або три 0) відразу перемогає.
# Лінії можуть бути горизонтальними, вертикальними або діагоналями
# (всього 8 можливих варіантів). Приблизний вигляд поля:

# 0 0 X
# X 0 X
# 0 X 0

# Стратегія компютера (вашої програми) має цілеспрямовано вести до
# перемоги над людиною.

# Жодних вимог до інтерфейсу користуавча не ставиться.


import random


def draw_board(board: list) -> None:
    """ Add place bord """

    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)


def input_choice(board: list, player_choice: str) -> None:
    """ Receive your values(move)"""

    valid = False
    while not valid:
        player_answer = input("Enter your move in coord(1-9): "
                              + player_choice + "? ")
        try:
            player_answer = int(player_answer)
        except:
            print("This is not a number.")
            continue
        if 1 <= player_answer <= 9:
            if str(board[player_answer - 1]) not in "XO":
                board[player_answer - 1] = player_choice
                valid = True
            else:
                print("This cell is occupied")
        else:
            print("This is not a number from 1 to 9.")


def bot_choice(board: list, player_choice: str) -> None:
    """ This function create bot logic"""

    win_coord = ((0, 4, 8), (2, 4, 6), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 1, 2), (3, 4, 5), (6, 7, 8))
    valid = False
    count = 0
    x_positions = ""
    o_positions = ""
    for i in board:
        if i == "X":
            x_positions += str(count) + ","
            count += 1
        if i == player_choice:
            o_positions += str(count) + ","
            count += 1
    while not valid:
        bot_answer = 5
        if str(board[bot_answer - 1]) not in "XO":
            if player_choice not in board:
                board[bot_answer - 1] = player_choice
                valid = True
                break
        else:
            bot_answer = random.randint(1, 9)
            if player_choice not in board:
                board[bot_answer - 1] = player_choice
                valid = True
                break
        for i in win_coord:
            if board[i[0]] == board[i[1]] == player_choice \
                    and str(board[i[2]]) not in "XO":
                board[i[2]] = player_choice
                valid = True
                break
            elif board[i[1]] == board[i[2]] == player_choice \
                    and str(board[i[0]]) not in "XO":
                board[i[0]] = player_choice
                valid = True
                break
            elif board[i[0]] == board[i[2]] == player_choice \
                    and str(board[i[1]]) not in "XO":
                board[i[1]] = player_choice
                valid = True
                break
            else:
                if board[i[0]] == board[i[1]] and str(board[i[2]]) not in "XO":
                    board[i[2]] = player_choice
                    valid = True
                    break
                elif board[i[1]] == board[i[2]] and str(board[i[0]]) not in "XO":
                    board[i[0]] = player_choice
                    valid = True
                    break
                elif board[i[0]] == board[i[2]] and str(board[i[1]]) not in "XO":
                    board[i[1]] = player_choice
                    valid = True
                    break
        if board[i[0]] != board[i[1]] and board[i[0]] != board[i[2]] \
                and board[i[1]] != board[i[2]] and count > 1:
            if str(board[i[1]]) not in "XO":
                board[i[1]] = player_choice
                valid = True
                break
            if str(board[i[0]]) not in "XO":
                board[i[0]] = player_choice
                valid = True
                break
            if str(board[i[2]]) not in "XO":
                board[i[2]] = player_choice
                valid = True
                break


def check_win(board: list) -> bool:
    """ Check who has 3 values in a row"""

    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in win_coord:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False


def main() -> None:
    """ Ths func. run game"""

    board = list(range(1, 10))
    counter = 0
    win = False
    first = random.choice([0, 1])
    (bot_letter, player_letter) = ('X', 'O') if first == 0 else ('O', 'X')
    while not win:
        if counter % 2 == first:
            bot_choice(board, bot_letter)
        else:
            draw_board(board)
            input_choice(board, player_letter)
        counter += 1
        if counter > 4:
            winner = check_win(board)
            if winner:
                draw_board(board)
                print(winner, "WIN!")
                win = True
                break
        if counter >= 9:
            draw_board(board)
            print("DRAW!")
            break


main()
