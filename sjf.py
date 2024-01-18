def sjf(processes, n):
    # Sort the processes based on arrival time and burst time
    processes.sort(key=lambda x: (x[0], x[1]))

    # variables to store waiting time, turnaround time, completion time, and sums for average calculation
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n
    total_waiting_time = 0
    total_turnaround_time = 0

    # calculate completion time, waiting time, and turnaround time for each process
    for i in range(n):
        if i == 0:
            completion_time[i] = processes[i][0] + processes[i][1]
        else:
            completion_time[i] = completion_time[i - 1] + processes[i][1]

        waiting_time[i] = max(0, completion_time[i] - processes[i][1] - processes[i][0])
        turnaround_time[i] = waiting_time[i] + processes[i][1]

    # calculate total waiting time and total turnaround time for average calculation
    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)

    # calculate average waiting time and average turnaround time
    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n

    # print the result in the form of a table
    print("Process\tAT\tBT\tWT\tTAT\tCT")
    for i in range(n):
        print(f"{processes[i][2]}\t\t{processes[i][0]}\t\t{processes[i][1]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}\t\t{completion_time[i]}")

    # print average waiting time and average turnaround time
    print(f"\nAverage Waiting Time (AWT): {average_waiting_time:.2f}")
    print(f"Average Turnaround Time (ATAT): {average_turnaround_time:.2f}")

# Example usage with user input
if __name__ == "__main__":
    n = int(input("Enter the number of processes: "))

    processes = []
    print("\nEnter arrival time and burst time for each process:")
    for i in range(n):
        arrival = int(input(f"Enter arrival time for process {i + 1}: "))
        burst = int(input(f"Enter burst time for process {i + 1}: "))
        processes.append((arrival, burst, i + 1))

    sjf(processes, n)
