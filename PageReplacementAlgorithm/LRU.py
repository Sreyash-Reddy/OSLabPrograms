nFrames = int(input("Enter the number of Frames: "))
pages = list(map(int,input("Enter the pages: ").split(" ")))

frames = []
priorty = []


miss = 0
for each in pages:
    if each in frames:
        x = frames.index(each)
        y = priorty[x]
        for i in range(len(priorty)):
            if(priorty[i] < y):
                priorty[i] += 1
        priorty[x] = 1
    else:
        miss += 1
        if(len(frames) < nFrames):
            frames.append(each)
            for i in range(len(priorty)):
                priorty[i] += 1
            priorty.append(1)
        else:
            x = priorty.index(max(priorty))
            frames.pop(x)
            frames.insert(x,each)
            for i in range(len(priorty)):
                priorty[i] += 1
            priorty[x] = 1
print("The number of page faults: "+str(miss))

            