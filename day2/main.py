def main():
    f = open("day_2_input.txt")
    text = f.read()
    ranges = text.split(",")
    total = 0
    for r in ranges:
        temp = r.split("-")
        first = int(temp[0])
        last = int(temp[1])
        for i in range(first, last+1):
            s = str(i)
            invalid = False
            a = len(s)//2
            for l in range(a, 0, -1):
                if len(s)%l != 0:
                    invalid = False
                else:
                    invalid = True
                    for k in range(1, len(s)//l):
                        if s[:l] != s[k*l:(k+1)*l]:
                            invalid = False
                            break
                if invalid:
                    break
            if invalid:
                total += i
                print(f"{s} is invalid")
    print(total)

if __name__ == "__main__":
    main()
