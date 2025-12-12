
locs = [list(map(int, line.split(","))) for line in open("day_9_input.txt")]

def day_nine():
    max = 0
    for i in range(len(locs)):
        for j in range(i+1, len(locs)):
            a = area(locs[i], locs[j])
            if a > max:
                max = a
    print(f"Part 1 has a max area of {max}")

def area(p1, p2):
    return (1 + abs(p1[0]-p2[0]))*(1 + abs((p1[1]-p2[1])))
if __name__ == "__main__":
    day_nine()
