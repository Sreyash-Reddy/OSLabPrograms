blockSize = list(map(int , input("Enter the block sizes: ").split(" ")))
processSize = list(map(int , input("Enter the process sizes: ").split(" ")))

sum = 0
for each1 in processSize:
    wastage = -1
    diff = 0
    j = -1
    for i in range(len(blockSize)):
        if(each1 <= blockSize[i]):
            diff = blockSize[i] - each1
            if(wastage < diff):
                wastage = diff
                j = i         
        
        if(i == len(blockSize)-1 and j != -1):
            print(str(each1) + " -> "+ str(blockSize[j])+" "+str(j+1))
            sum += wastage
            blockSize[j] = -1
        elif(i == len(blockSize)-1 and j == -1):
            print(str(each1) + " -> Unallocated")

print(blockSize)
for each in blockSize:
    if(each != -1):
        sum += each
print("The total memory wastage is: "+str(sum))