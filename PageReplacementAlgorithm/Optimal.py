nFrames = int(input("Enter the number of Frames: "))
pages = list(map(int,input("Enter the pages: ").split(" ")))

frames = []

miss = 0
for i in range(len(pages)):
    if pages[i] in frames:
        print(frames , end=" - Hit\n")      
    else:
        miss += 1
        if(len(frames) < nFrames):
            frames.append(pages[i])
        else:
            pageStatus = []
            for each in frames:
                count = 0
                k = 999999
                for j in range(i , len(pages)):
                    if pages[j] == each :
                        k = min(k,j)
                        count += 1
                pageStatus.append([k , count ,each])       
            pageStatus.sort()
            x = frames.index(pageStatus[-1][-1])

            frames[x] = pages[i]
        print(frames , end=" - Miss\n")      

        
                
print("The number of page faults: "+str(miss))

            