import math

boxes = [list(map(int, line.split(","))) for line in open("day_8_input.txt") ] 
circuits = []
connections = 1000
    
def day_eight():
    distances = []
    for i in range(len(boxes)):
        for k in range(i+1, len(boxes)):
            distances.append([distance(boxes[i], boxes[k]), (i,k)])
    sort_distances(distances)
    i = 0
    count = 0
    while i < len(distances):
        if add_circuit(*distances[i][1]):
            count += 1
        i += 1
        if len(circuits[0]) == len(boxes):
            break
    b = distances[i-1][1]
    x1 = boxes[b[0]][0]
    x2 = boxes[b[1]][0]
    print(x1*x2)
#    sizes = []
#    for c in circuits:
#        sizes.append(len(c))
#    sizes.sort(reverse = True)
#    size = sizes[0]*sizes[1]*sizes[2]
#    print(sizes)
#    print(size)

def add_circuit(b1, b2):
    exist = False
    for i in range(len(circuits)):
        if b1 in circuits[i]:
            exist = True
            circuits[i].add(b2)
        if b2 in circuits[i]:
            exist = True
            circuits[i].add(b1)
    if not exist:
        circuits.append({b1, b2})
    for i in range(len(circuits)):
        for j in range(i+1, len(circuits)):
            if not circuits[i].isdisjoint(circuits[j]):
                circuits[i] = circuits[i].union(circuits[j])
                circuits.pop(j)
                break
    
def sort_distances(distances):
    if len(distances) > 1:
        mid = len(distances) // 2
        left_half = distances[:mid]
        right_half = distances[mid:]
        sort_distances(left_half)
        sort_distances(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i][0] < right_half[j][0]:
                distances[k] = left_half[i]
                i += 1
            else:
                distances[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            distances[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            distances[k] = right_half[j]
            j += 1
            k += 1

def distance(a, b):
    x = (a[0] - b[0])**2
    y = (a[1] - b[1])**2
    z = (a[2] - b[2])**2
    d = math.sqrt(x + y + z)
    return d

if __name__ == "__main__":
    day_eight()
