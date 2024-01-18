def bubblesort(arrival_time, burst_time, n):
    for i in range(n):
        for j in range(0, n - i - 1):
            # Compare based on arrival time first
            if arrival_time[j] > arrival_time[j + 1]:
                arrival_time[j], arrival_time[j + 1] = arrival_time[j + 1], arrival_time[j]
                burst_time[j], burst_time[j + 1] = burst_time[j + 1], burst_time[j]
            # If arrival times are equal, compare based on burst time
            elif arrival_time[j] == arrival_time[j + 1] and burst_time[j] > burst_time[j + 1]:
                arrival_time[j], arrival_time[j + 1] = arrival_time[j + 1], arrival_time[j]
                burst_time[j], burst_time[j + 1] = burst_time[j + 1], burst_time[j]

def sjf(arrival_time, burst_time, n):
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    total_wait = 0
    total_turn = 0

    for i in range(n):
        if i == 0:
            completion_time[i] = arrival_time[i] + burst_time[i]
        else:
            completion_time[i] = completion_time[i - 1] + burst_time[i]
        
        turnaround_time[i] = completion_time[i] - arrival_time[i]
        waiting_time[i] = turnaround_time[i] - burst_time[i]
        total_wait += waiting_time[i]
        total_turn += turnaround_time[i]

    print("PROCESS\t ARRIVAL TIME \t BURST TIME \t TURNAROUND TIME \t WAITING TIME\t")
    for i in range(n):
        print("P[{}]\t\t{}\t\t{}\t\t{}\t\t{}".format(i + 1, arrival_time[i], burst_time[i], turnaround_time[i],
                                                       waiting_time[i]))

    avgw = total_wait / n
    avgt = total_turn / n
    print("average waiting time=", avgw)
    print("average TAT time=", avgt)

n = int(input("Enter process number: "))
arrival_time = [0] * n
burst_time = [0] * n

for i in range(n):
    arrival_time[i] = int(input(f"Enter process P[{i + 1}] arrival time: "))
    burst_time[i] = int(input(f"Enter process P[{i + 1}] burst time: "))


bubblesort(arrival_time, burst_time, n)
sjf(arrival_time, burst_time, n)