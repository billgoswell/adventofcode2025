from functools import cache
import sys
sys.setrecursionlimit(2000)

grid = [list(line.strip()) for line in open("day_7_input.txt")]

def daySeven():
    partOne(grid)
    partTwo(grid)

def partTwo(grid):
    intialBeamCol = 0
    for i in range(len(grid[0])):
        if grid[0][i] == "S":
            intialBeamCol = i

    intial = (1, intialBeamCol)
    answer = solve(*intial)
    print(f"Part Two Answer is {answer}")

@cache
def solve(r, c):
    if r >= len(grid): 
        return 1
    if grid[r][c] == "." or grid[r][c] == "S":
        return solve(r + 1, c)
    elif grid[r][c] == "^":
        return solve(r, c - 1) + solve(r, c + 1)

def partOne(grid):
    rows = len(grid)
    columns = len(grid[0])
    beams = []
    for i in range(columns):
        if grid[0][i] == ".":
            beams.append(0)
        else:
            beams.append(1)
    beamSplits = 0
    for i in range(1, rows):
        newBeams = beams
        for j in range(columns):
            if grid[i][j] == "^":
                if beams[j] == 1:
                    beamSplits += 1
                    newBeams[j] = 0
                    newBeams[j+1] = 1
                    newBeams[j-1] = 1
        beams = newBeams
    print(f"Part One Answer is {beamSplits}")


if __name__ == "__main__":
    daySeven()
