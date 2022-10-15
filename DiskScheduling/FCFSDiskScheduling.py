n = int(input("Enter the number of blocks: "))

data = list(map(int , input("Enter the data: ").split(" ")))

startingPoint = int(input("Enter the starting location of the pointer: "))


sum = 0
start = startingPoint
for i in range(n):
    sum += abs(start - data[i])
    start = data[i]

print("The total seek time is: "+str(sum))