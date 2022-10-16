blockSize = list(map(int , input("Enter the block sizes: ").split(" ")))
processSize = list(map(int , input("Enter the process sizes: ").split(" ")))

sum = 0
for each1 in processSize:
    for i in range(len(blockSize)):
        if(each1 <= blockSize[i]):
            print(str(each1) + " -> "+ str(blockSize[i])+" -> "+str(i+1))
            sum += blockSize[i] - each1
            blockSize[i] = blockSize[i] - each1
            break
        else:
            if(i == len(blockSize)-1):
                print(str(each1) + " -> Not Allocated")
            else:
                continue

for each in blockSize:
    sum += each
print("The total memory wastage is: "+str(sum))