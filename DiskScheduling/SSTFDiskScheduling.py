n = int(input("Enter the number of blocks: "))

data = list(map(int , input("Enter the data: ").split(" ")))

startingPoint = int(input("Enter the starting location of the pointer: "))

start = startingPoint
sum = 0
for i in range(n):
    temp = []
    for j in range(len(data)):
        temp.append(abs(data[j] - start))
    y = temp.index(min(temp))
    sum += abs(start - data[y])
    start = data[y]
    data.pop(y)

print("The total seek time is: "+str(sum))