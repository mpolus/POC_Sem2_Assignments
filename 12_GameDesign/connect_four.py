grid = [
    ["1", "2", "3", "4", "5", "6", "7"],     # [R0C0, R0C1, R0C2]
    ["8", "9", "10", "11", "12", "13", "14"],     # [R1C0, R1C1, R1C2]
    ["15", "16", "17", "18", "19", "20", "21"],     # [R2C0, R2C1, R2C2]
    ["22", "23", "24", "25", "26", "27", "28"],
    ["29", "30", "31", "32", "33", "34", "35"],
    ["36", "37", "38", "39", "40", "41", "42"],
]

current_piece = "R"

def print_grid():
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if col != 2:
                print(grid[row][col], end="  ")            
            else:
                print(grid[row][col])
                print()

def is_bad_num_string(choice : str):
    if (choice.isnumeric() and int(choice) >= 1 and int(choice) <= 42):
        return False
    return True
                
def is_bad_choice(choice : str):
    if(choice.__eq__("STOP")):
        return False
    return is_bad_num_string(choice)

# def get_row(grid_spot):
#     if grid_spot == 1 or grid_spot == 2 or grid_spot == 3:
#         return 0
#     elif grid_spot == 4 or grid_spot == 5 or grid_spot == 6:
#         return 1
#     else:
#         return 2                    

def game_loop():
    global current_piece
    print("Welcome to TIC TAC TOE")
    user_choice = ""
    while(True):
        print_grid()
        while(is_bad_choice(user_choice)):
            user_choice = input("Enter STOP to end.  Or a number (1-9) where to put the piece: ")
        if user_choice.__eq__("STOP"):
            break
        grid_spot = int(user_choice)
        place_piece(grid_spot)
        if(check_game_over()):
            print_grid()
            break
        current_piece = "O" if current_piece.__eq__("X") else "X"
        user_choice = ""
    print("GAME OVER")
        
game_loop()
