def main():
    f = open("day_5_input.txt").read()
    temp = f.split("\n\n")
    tempranges = temp[0].split()
    available = temp[1].split()
    ranges = []
    for r in tempranges:
        t = r.split("-")
        ranges.append([int(t[0]), int(t[1])])
    ranges = orderRanges(ranges)
    ranges = removeOverlappingRanges(ranges)
    total = 0
    for r in ranges:
        total += r[1]-r[0]+1
    print(total)
    
def orderRanges(ranges):
    for i in range(len(ranges)-1):
        for j in range(len(ranges)-1-i):
            if ranges[j][0] > ranges[j +1][0]:
                ranges[j], ranges[j+1] = ranges[j+1], ranges[j]
    return ranges

def removeOverlappingRanges(ranges):
    newRanges = [ranges[0]]
    for i in range(1, len(ranges)):
        if newRanges[-1][1] >= ranges[i][0]:
            if newRanges[-1][1] < ranges[i][1]:
                newRanges[-1][1] = ranges[i][1]
        else:
            newRanges.append(ranges[i])
    return newRanges


def partOne(ranges, available):
    fresh = []
    for r in ranges:
        to_remove = []
        for a in available:
            if r[0] <= int(a) <= r[1]:
                yfresh.append(a)
                to_remove.append(a)
        for item in to_remove:
            available.remove(item)

    print(fresh)
    print(len(fresh))




if __name__ == "__main__":
    main()
