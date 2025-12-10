def main():
    f = open("day_4_input.txt")
    text = f.read()
    temp = text.split()
    limitofrolls = 4
    accessible = 0
    removing = True
    rowsize = len(temp[0])
    grid = []
    for i in range(len(temp)):
        row = []
        for j in range(rowsize):
            if temp[i][j] == "@":
                row.append(True)
            else:
                row.append(False)
        grid.append(row)

    last = -1
    while(last != accessible):
        last = accessible
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                around = 0
                if grid[i][j]:
                    if i > 0:
                        if j > 0:
                            if grid[i-1][j-1]:
                                around += 1
                        if j < rowsize-1:
                            if grid[i-1][j+1]:
                                around += 1
                        if grid[i-1][j]:
                            around += 1
                    if i < rowsize-1:
                        if j > 0:
                            if grid[i+1][j-1]:
                                around += 1
                        if j < rowsize-1:
                            if grid[i+1][j+1]:
                                around += 1
                        if grid[i+1][j]:
                            around += 1
                    if j > 0:
                        if grid[i][j-1]:
                            around += 1
                    if j < rowsize-1:
                        if grid[i][j+1]:
                            around += 1
                    if around < limitofrolls:
                        accessible += 1
                        if removing:
                            grid[i][j] = False
                            
    print(accessible)



if __name__ == "__main__":
    main() 
