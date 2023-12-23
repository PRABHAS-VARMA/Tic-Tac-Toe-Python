# Type "python math.py" to start the game
# It might be a little frustrating and confusing to play the game considering it is hard to keep of track of row and column for every chance 



def grid(x):
    for i in x:
        print(" | ".join(i))
        print("-" * 9)

def win(grid):
    for i in grid:
        if i[0] == i[1] == i[2] and i[0] != ' ':
            return True

    for j in range(3):
        if grid[0][j] == grid[1][j] == grid[2][j] and grid[0][j] != ' ':
            return True

    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != ' ':
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != ' ':
        return True

    return False

def fillingGrid(grid):
    for i in grid:
        if ' ' in i:
            return False
    return True

def main():
    a = [[' ' for _ in range(3)] for _ in range(3)]
    presentPlayer = 'X'

    while True:
        grid(a)

        row = int(input(f"Player {presentPlayer}, enter row (0, 1, or 2): "))
        col = int(input(f"Player {presentPlayer}, enter column (0, 1, or 2): "))

        if a[row][col] == ' ':
            a[row][col] = presentPlayer
        else:
            print("Cell already taken. Try again.")
            continue

        if win(a):
            grid(a)
            print(f"Player {presentPlayer} wins!")
            break

        if fillingGrid(a):
            grid(a)
            print("It's a tie!")
            break

        presentPlayer = 'O' if presentPlayer == 'X' else 'X'

main()
