def fcfs_scheduling():
    # Step 2: Input the number of processes, arrival time, and burst time
    n = int(input("Enter the number of processes: "))
    arrival_time = []
    burst_time = []

    for i in range(n):
        arrival_time.append(int(input(f"Enter arrival time for process {i + 1}: ")))
        burst_time.append(int(input(f"Enter burst time for process {i + 1}: ")))

    # Step 5: Sort processes based on arrival time
    processes = sorted(range(n), key=lambda k: arrival_time[k])

    # Step 6: Initialize variables
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    current_time = 0

    # Step 7: Calculate completion time, turnaround time, and waiting time
    for i in processes:
        completion_time[i] = max(current_time, arrival_time[i]) + burst_time[i]
        turnaround_time[i] = completion_time[i] - arrival_time[i]
        waiting_time[i] = turnaround_time[i] - burst_time[i]
        current_time = completion_time[i]

    # Step 8: Calculate and display Average Waiting Time (AWT) and Average Turnaround Time (ATAT)
    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)
    awt = total_waiting_time / n
    atat = total_turnaround_time / n

    print("\nProcess\t Arrival Time\t Burst Time\t Completion Time\t Turnaround Time\t Waiting Time")
    for i in range(n):
        print(f"{i + 1}\t {arrival_time[i]}\t\t {burst_time[i]}\t\t {completion_time[i]}\t\t {turnaround_time[i]}\t\t {waiting_time[i]}")

    print(f"\nAverage Waiting Time: {awt:.2f}")
    print(f"Average Turnaround Time: {atat:.2f}")

# Step 1: Start
fcfs_scheduling()
# Step 9: Stop
