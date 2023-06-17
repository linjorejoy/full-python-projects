import numpy as np

grid = [[0, 0, 0, 6, 0, 0],
        [0, 6, 0, 0, 4, 2],
        [4, 0, 0, 0, 0, 0],
        [0, 2, 0, 1, 0, 0],
        [0, 0, 0, 0, 3, 0],
        [0, 0, 5, 0, 0, 0]]

print(np.array(grid))


def possible(y,x,n):
    global grid
    for i in range(0,6):
        if grid[y][i] == n:
            return False
    for i in range(0,6):
        if grid[i][x] == n:
            return False


    for i in range(0,2):
        for j in range(0,3):
            if grid[(y//2)*2+i][(x//3)*3+j] == n:
                return False
    return True


def solve():
    global grid
    global count
    for y in range(6):
        for x in range(6):
            if grid[y][x] == 0:
                for n in range(1,7):
                    if possible(y,x,n):
                        grid[y][x] = n
                        count +=1
                        solve()
                        grid[y][x] = 0
                return

    print(np.array(grid))
    print(count)
    input("More?")


count = 0
solve()
