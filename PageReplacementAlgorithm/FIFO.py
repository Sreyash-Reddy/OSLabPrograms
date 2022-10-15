nFrames = int(input("Enter the number of Frames: "))
pages = list(map(int,input("Enter the pages: ").split(" ")))

frames = []

k = 0
miss = 0
for each in pages:
    if each in frames:
        continue
    else:
        miss += 1
        if(len(frames) < nFrames):
            frames.append(each)
        else:
            frames.pop(k)
            frames.insert(k , each)
            if(k == nFrames-1):
                k = 0
            else:
                k += 1

print("The number of page faults: "+str(miss))
