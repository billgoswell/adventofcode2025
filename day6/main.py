def daySix():
    f = open("day_6_input.txt").read()
    temp = f.split("\n")
    if temp[-1] == '':
        temp.pop()
    lengths = determineLengths(temp[-1])
    operators = temp[-1].split()
    temp.pop()
    currentLoc = 0
    nums = []
    for i in range(len(lengths)):
        row = []
        for k in range(lengths[i]):
            num = ""
            for j in range(len(temp)):
                if temp[j][currentLoc] != " ":
                    num += temp[j][currentLoc]
            row.append(int(num))
            currentLoc += 1
        nums.append(row)
        currentLoc += 1
    partTwo(operators,nums)
        


def determineLengths(tempoperators):
    print(tempoperators)
    print(len(tempoperators))
    lengths = []
    length = 0
    for i in range(1,len(tempoperators)):
        if tempoperators[i] == " ":
            length += 1
        else:
            lengths.append(length)
            length = 0
    lengths.append(length+1)
    return lengths

    
        
def partTwo(operators, nums):
    total = 0
    for i in range(len(operators)):
        rowtotal = 0
        for num in nums[i]:
            if operators[i] == "+":
                rowtotal += num
            else:
                if rowtotal == 0:
                    rowtotal = num
                else:
                    rowtotal *= num
        total += rowtotal
    print(f"Part Two Total is: {total}")

def partOne(temp):
    operators = temp[-1].split()
    temp.pop()
    nums = []
    for i in range(len(temp)):
        nums.append(temp[i].split())
    total = 0
    for i in range(len(operators)):
        rowtotal = 0
        if operators[i] == "+":
            for j in range(len(nums)):
                rowtotal += int(nums[j][i])
        if operators[i] == "*":
            rowtotal = int(nums[0][i])
            for j in range(1, len(nums)):
                rowtotal *= int(nums[j][i])
        total += rowtotal
    print(f"Part One Total is: {total}")

                



if __name__ == "__main__":
    daySix()
