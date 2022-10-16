def CalculateWaitingTime(at, bt, N):
    wt = [0]*N;
    wt[0] = 0;
    print("P.No.\tArrival Time\t" , "Burst Time\tWaiting Time");
    print("1" , "\t\t" , at[0] , "\t\t" , bt[0] , "\t\t" , wt[0]);
    for i in range(1,N):
        wt[i] = (at[i - 1] +bt[i - 1] + wt[i - 1]) - at[i];
        print(i + 1 , "\t\t" , at[i] , "\t\t" , bt[i] , "\t\t" , wt[i]);
    average = 0.0;
    sum = 0;
    for i in range(N):
        sum = sum + wt[i];
    average = sum / N;
    print("Average waiting time = " , average);
if __name__ == '__main__':
    N = int(input("enter the number of process:"));
    bt=list(map(int , input("Enter the burst times: ").split(" ")))
    at=list(map(int , input("Enter the arrival times: ").split(" ")))
    CalculateWaitingTime(at, bt, N);
