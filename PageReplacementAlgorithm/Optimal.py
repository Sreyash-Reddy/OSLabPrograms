nFrames = int(input("Enter the number of Frames: "))
pages = list(map(int,input("Enter the pages: ").split(" ")))

frames = []

miss = 0
for i in range(len(pages)):
    if pages[i] in frames:
        continue
    else:
        miss += 1
        if(len(frames) < nFrames):
            frames.append(pages[i])
        else:
            for each in frames:
                count = 0
                k = 999999
                for j in range(i , len(pages)):
                    if each == pages[i] :
                        k = min(k,j)
                        count += 1
                
        
                    




print("The number of page faults: "+str(miss))

            