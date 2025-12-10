def main():
    f = open("day_3_input.txt")
    text = f.read()
    banks = text.split()
    numdigits = 12
    voltage = 0
    for b in banks:
        digits = []
        last = -1
        for i in range(numdigits):
            digits.append(last+1)
            for j in range(last+1, len(b)-(numdigits-1-i)):
                if (b[j] > b[digits[i]]):
                    digits[i] = j
            last = digits[i]

        v = ""
        for d in digits:
            v += b[d]
        voltage += int(v)
        print(v)
    print(voltage)



if __name__ == "__main__":
    main() 
