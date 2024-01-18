def priority_scheduling(processes, burst_time, arrival_time, priority):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    total_waiting_time = 0
    total_turnaround_time = 0

    # Sort processes based on priority (lower priority first)
    sorted_processes = [x for _, x in sorted(zip(priority, processes), reverse=False)]
    sorted_burst_time = [x for _, x in sorted(zip(priority, burst_time), reverse=False)]
    sorted_arrival_time = [x for _, x in sorted(zip(priority, arrival_time), reverse=False)]

    time = 0

    for i in range(n):
        waiting_time[i] = time
        turnaround_time[i] = waiting_time[i] + sorted_burst_time[i]
        time += sorted_burst_time[i]

    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)

    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n

    return waiting_time, turnaround_time, average_waiting_time, average_turnaround_time

# Example usage with user input for Lower Priority First
if __name__ == "__main__":
    n = int(input("Enter the number of processes: "))

    processes = []
    burst_time = []
    arrival_time = []
    priority = []

    print("\nEnter burst time, arrival time, and priority for each process:")
    for i in range(n):
        burst = int(input(f"Enter burst time for process {i + 1}: "))
        arrival = int(input(f"Enter arrival time for process {i + 1}: "))
        prio = int(input(f"Enter priority for process {i + 1}: "))
        processes.append(i + 1)
        burst_time.append(burst)
        arrival_time.append(arrival)
        priority.append(prio)

    waiting_time, turnaround_time, avg_waiting_time, avg_turnaround_time = priority_scheduling(
        processes, burst_time, arrival_time, priority
    )

    print("\nProcess\tArrival Time\tBurst Time\tPriority\tWaiting Time\tTurnaround Time")
    for i in range(len(processes)):
        print(
            f"{processes[i]}\t\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{priority[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}"
        )

    print("\nAverage Waiting Time:", avg_waiting_time)
    print("Average Turnaround Time:", avg_turnaround_time)
