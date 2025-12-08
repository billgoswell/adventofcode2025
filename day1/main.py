

def main():
    f = open("day_1_input.txt")
    text = f.read()
    commands = text.split()
    endzero = 0
    totalzeros = 0
    dial = 50
    print(f"The dial starts by point at {dial}")
    for i in range(len(commands)):
        command = commands[i]   
        direction = command[0]
        string_rotation = command[1:]
        rotation = int(string_rotation)
        if direction == 'L':
            if rotation > 100:
                totalzeros += rotation//100
                rotation = rotation%100
            if rotation == dial:
                dial = 0;
                endzero += 1
                totalzeros += 1
            elif rotation < dial:
                dial -= rotation
            else:
                if dial != 0:
                    totalzeros += 1
                rotation -= dial
                dial = 100 - rotation
        if direction == 'R':
            if rotation > 100:
                totalzeros += rotation//100
                rotation = rotation%100
            if rotation == 100-dial:
                dial = 0;
                endzero += 1
                totalzeros += 1
            elif rotation < 100-dial:
                dial += rotation
            else:
                if dial != 0:
                    totalzeros += 1
                rotation -= 100-dial
                dial = rotation
        print(f"The dial is rotated {command} to point at {dial}, there are {endzero} endzeros and {totalzeros} zeros")

if __name__ == "__main__":
    main()
