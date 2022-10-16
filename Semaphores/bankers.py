if __name__ == "__main__":
    alloc = []
    max = []
    n = int(input("Enter the number of processes: "))
    m = int(input("Enter the number of resources: "))
    for i in range(n):
        tmp = []
        print("For Process {}: ".format(i+1))
        for j in range(m):
            a = int(input("Enter the allocated resource to {}: ".format(i+1)))
            tmp.append(a)
        alloc.append(tmp)

    for i in range(n):
        tmp = []
        print("For Process {}: ".format(i+1))
        for j in range(m):
            a = int(input("Enter the maximum resource for {}: ".format(i+1)))
            tmp.append(a)
        max.append(tmp)

    avail = [3, 3, 2]

    f = [0] * n
    ans = [0] * n
    ind = 0

    need = [[0 for i in range(m)] for i in range(n)]
    print(need)
    for i in range(n):
        for j in range(m):
            need[i][j] = max[i][j] - alloc[i][j]
    y = 0
    for k in range(5):
        for i in range(n):
            if (f[i] == 0):
                flag = 0
                for j in range(m):
                    if (need[i][j] > avail[j]):
                        flag = 1
                        break

                if (flag == 0):
                    ans[ind] = i
                    ind += 1
                    for y in range(m):
                        avail[y] += alloc[i][y]
                    f[i] = 1

    print("Following is the SAFE Sequence")

    for i in range(n - 1):
        print(" P", ans[i], " ->", sep="", end="")
    print(" P", ans[n - 1], sep="")