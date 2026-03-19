"""
Day 4: Printing Department
"""

def read_input(file_path):
    grid = []
    with open(file_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            grid.append([ch for ch in line])
    return grid

def compute_rolls_access_part1(grid):
    # edge case
    n = len(grid)
    m = len(grid[0]) if n > 0 else 0
    if m == 0:
        return 0
    
    res = 0
    dir_adjacent = ((1,1),(1,0), (1,-1),
                    (0,1), (0,-1),
                    (-1,1),(-1,0), (-1,-1))
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '@':
                continue
            count_roll = 0
            for di, dj in dir_adjacent:
                if 0 <= i+di < n and 0 <= j+dj < m and grid[i+di][j+dj] == '@':
                    count_roll += 1
                if count_roll >= 4:
                    break
            if count_roll < 4:
                res += 1
    
    return res

def compute_rolls_access_part1(grid):
    # edge case
    n = len(grid)
    m = len(grid[0]) if n > 0 else 0
    if m == 0:
        return 0
    
    res = 0
    dir_adjacent = ((1,1),(1,0), (1,-1),
                    (0,1), (0,-1),
                    (-1,1),(-1,0), (-1,-1))
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '@':
                continue
            count_roll = 0
            for di, dj in dir_adjacent:
                if 0 <= i+di < n and 0 <= j+dj < m and grid[i+di][j+dj] == '@':
                    count_roll += 1
                if count_roll >= 4:
                    break
            if count_roll < 4:
                res += 1
    
    return res

def check_accessibility(cell, grid,n,m):
    (i,j) = cell
    res = 0
    dir_adjacent = ((-1,-1),(-1,0),(-1,1),
                    (0,-1),        (0,1),
                    (1,-1),(1,0), (1,1)
                    )
    # check accessibility of cell
    count_roll = 0
    for di, dj in dir_adjacent:
        if 0 <= i+di < n and 0 <= j+dj < m and grid[i+di][j+dj] == '@':
            count_roll += 1
        if count_roll >= 4:
            break
    # if accessible
    if count_roll < 4:
        # update res, grid
        res += 1
        grid[i][j] = '.' # no longer a roll
        # run same function for adjacent cells
        for di, dj in dir_adjacent:
            if 0 <= i+di < n and 0 <= j+dj < m and grid[i+di][j+dj] == '@':
                res_adj = check_accessibility((i+di, j+dj), grid, n,m)
                res += res_adj
    
    return res

def compute_rolls_access_part2(grid):
    n = len(grid)
    m = len(grid[0]) if n > 0 else 0
    if m == 0:
        return 0
    
    res = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] != '@':
                continue
            # count all the accessible rolls adjacent between them 
            # and including (i,j) 
            count = check_accessibility((i,j), grid,n,m)
            res += count

    return res

if __name__ == "__main__":
    file_path = "challenge4/test_input.txt"
    grid = read_input(file_path)
    res1 = compute_rolls_access_part1(grid)
    res2 = compute_rolls_access_part2(grid)
    print(f"The number of accessible rolls part 1 is: {res1}")
    print(f"The number of accessible rolls part 2 is: {res2}")

