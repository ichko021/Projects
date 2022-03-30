#TICTACTOE GAME

sector = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def print_display():
    """prints out the display"""
    print(f"{sector[0][0]}|{sector[0][1]}|{sector[0][2]}")
    print("-----")
    print(f"{sector[1][0]}|{sector[1][1]}|{sector[1][2]}")
    print("-----")
    print(f"{sector[2][0]}|{sector[2][1]}|{sector[2][2]}")


def mark_sector_p1():
    """
    PLAYER 1
    marks with X sector that was chosen
    by player 1"""
    print("Player 1's turn")
    choose_row = int(input("Choose row: "))
    if choose_row not in [1, 2, 3]:
        print("Invalid number")
        mark_sector_p1()
    choose_column = int(input("Choose column: "))
    if choose_column not in [1, 2, 3]:
        print("Invalid number")
        mark_sector_p1()
    if sector[choose_row - 1][choose_column - 1] == " ":
        sector[choose_row - 1][choose_column - 1] = "X"
    else:
        print("Invalid sector")
        mark_sector_p1()


def mark_sector_p2():
    """
    PLAYER 2
    marks with O sector that was chosen
    by player2"""
    print("Player 2's turn")
    choose_row = int(input("Choose row: "))
    if choose_row not in [1, 2, 3]:
        print("Invalid number")
        mark_sector_p2()
    choose_column = int(input("Choose column: "))
    if choose_column not in [1, 2, 3]:
        print("Invalid number")
        mark_sector_p2()
    if sector[choose_row - 1][choose_column - 1] == " ":
        sector[choose_row - 1][choose_column - 1] = "O"
    else:
        print("Invalid sector")
        mark_sector_p2()


def win_condition():
    """Will check if rows, columns or diagonals
    are equal. If condition is true, player 1 or 2 wins"""
    ver_check = []
    diag_check = []
    diag_check_1 = [sector[2][0], sector[1][1], sector[0][2]]
    for i in range(len(sector)):
        diag_check.append(sector[i][i])
        if diag_check == ["X", "X", "X"]:
            print("We have a winner!")
            return "q"
        elif diag_check == ["O", "O", "O"]:
            print("We have a winner!")
            return "q"
        elif diag_check_1 == ["X", "X", "X"]:
            print("We have a winner!")
            return "q"
        elif diag_check_1 == ["O", "O", "O"]:
            print("We have a winner!")
            return "q"
        elif sector[i] == ["X", "X", "X"]:
            print("We have a winner!")
            return "q"
        elif sector[i] == ["O", "O", "O"]:
            print("We have a winner!")
            return "q"
        for x in range(len(sector)):
            ver_check.append(sector[x][i])
            if ver_check == ["X", "X", "X"]:
                print("We have a winner!")
                return "q"
            elif ver_check == ["O", "O", "O"]:
                print("We have a winner!")
                return "q"

def game_on():
    """Deals with all the functions"""
    print("TIC TAC TOE")
    print("Choose rows(x) and columns(y). 1 for first, 2 for second and etc...")
    print_display()
    play = " "
    while play:
        mark_sector_p1()
        print_display()
        if win_condition() == "q":
            break
        mark_sector_p2()
        print_display()
        if win_condition() == "q":
            break


"""Choose whether you want to play another round"""
game_on()
while True:
    choice = input("Do you want to play again?(y/n)")
    if choice == "y":
        sector = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        game_on()
    else:
        print("Goodbye!")
        break