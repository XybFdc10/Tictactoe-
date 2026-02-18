import random

slots = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

def board():
    print("\n\n")
    for i in range(len(slots)):
        display_row = [f" {cell} "for cell in slots[i]]
        print("|".join(display_row))
        if i < len(slots)-1:
            print("---+---+---")
    print("\n\n")

xr = ["X", "O"]

def choose_symbol():
    get_move = random.choice(xr)
    xr.remove(get_move)
    return get_move

computer_symbol = choose_symbol()
user_symbol = choose_symbol()

def computer_move():
    space_position = []
    for r_idx, row in enumerate(slots):
        for c_idx, val in enumerate(row):
            if val == " ":
                space_position.append((r_idx, c_idx))
    if space_position:
        target_r, target_c = random.choice(space_position)
        slots[target_r][target_c] = computer_symbol
        return True
    return False

def is_win():
    n = len(slots)
    #player's win
    for row in slots:
        if all(cell == user_symbol for cell in row):
            board()
            print("you win!")
            return True
    for col in range(n):
        if all(slots[row][col] == user_symbol for row in range(n)):
            board()
            print("you win!")
            return True
    if all(slots[i][i] == user_symbol for i in range(n)):
        board()
        print("you win!")
        return True
    if all(slots[i][n - 1 - i] == user_symbol for i in range(n)):
        board()
        print("you win!")
        return True
    #computer's win
    for row in slots:
        if all(cell == computer_symbol for cell in row):
            board()
            print("computer win!")
            return True
    for col in range(n):
        if all(slots[row][col] == computer_symbol for row in range(n)):
            board()
            print("computer win!")
            return True
    if all(slots[i][i] == computer_symbol for i in range(n)):
        board()
        print("computer win!")
        return True
    if all(slots[i][n - 1 - i] == computer_symbol for i in range(n)):
        board()
        print("computer win!")
        return True
    return False

def is_draw():
    space_position = []
    for i in range(len(slots)):
        if " " in slots[i]:
            space_position.append(0)
        else:
            space_position.append(1)
    if all(space_position) == True:
        board()
        print("The Match Is Draw!")
        return True
    return False

def main():
    user_input = input("Enter A Number (1 / 0): ")
    if user_input == "1":
        print("User's First")
        board()
        while True:
            try:
                user_move = int(input(f"You Are {user_symbol}: Enter A Number (1 - 9): "))
                move_made = False
                #row 1 - column 1 - 3
                if 1 <= user_move <= 3:
                    if slots[0][user_move - 1] == " ":
                        slots[0][user_move - 1] = user_symbol
                        move_made = True
                #row 2 - column 1 - 3
                if 4 <= user_move <= 6:
                    if slots[1][user_move - 4] == " ":
                        slots[1][user_move - 4] = user_symbol
                        move_made = True
                #row 3 - column 1 - 3
                if 7 <= user_move <= 9:
                    if slots[2][user_move - 7] == " ":
                        slots[2][user_move - 7] = user_symbol
                        move_made = True

                #validating win and draw
                if move_made:
                    if is_win():
                        break
                    if is_draw():
                        break

                    computer_move()
                    if is_win():
                        break
                    if is_draw():
                        break
                    board()
                else:
                    print("the slot is already taken!")
            except ValueError:
                print("Enter a number")
    elif user_input == "0":
        print("computer's first")
        computer_move()
        board()
        while True:
            try:
                user_move = int(input(f"You Are {user_symbol}: Enter A Number (1 - 9): "))
                move_made = False
                #row 1 - column 1 - 3
                if 1 <= user_move <= 3:
                    if slots[0][user_move - 1] == " ":
                        slots[0][user_move - 1] = user_symbol
                        move_made = True
                #row 2 - column 1 - 3
                if 4 <= user_move <= 6:
                    if slots[1][user_move - 4] == " ":
                        slots[1][user_move - 4] = user_symbol
                        move_made = True
                #row 3 - column 1 - 3
                if 7 <= user_move <= 9:
                    if slots[2][user_move - 7] == " ":
                        slots[2][user_move - 7] = user_symbol
                        move_made = True

                #validating win and draw
                if move_made:
                    if is_win():
                        break
                    if is_draw():
                        break

                    computer_move()
                    if is_win():
                        break
                    if is_draw():
                        break
                    board()
                else:
                    print("the slot is already taken!")
            except ValueError:
                print("Enter A number")
    else:
        print("Please enter 1 or 0.")

if __name__ == "__main__":
    main()
