"""
File: time_tracker.py
----------------
This program tracks the time a user takes to finish a project and returns the amount the user has earned on the project
based on the hours spent on the project and the dollars earned per hour spent. The user has to input the project name,
and a start and stop prompt for the timer to start and stop. After timer stops, the hours spent on the project are 
calculated and multiplied by the dollars earned per hour to determined the amount earned on the project.
The program inputs and outputs are initially saved in a dictionary and finally saved to a csv file.
"""
import time
import csv
# todo: write a code that excludes the time the person takes to enter the start/stop if they made a mistake initially
# todo: convert time spent to two decimal places
# todo: create spaces and some kind of waiting message for user to finish project
# todo: add messages that tell user the time they started and the time they finished project
# todo: add comments to make code more understandable
# todo: import decimals to format floats to two decimal places
# todo: include comments to make code readable
# todo: include in readme that csv file should not be open in excel while running the code


def main():
    data = {}
    project_name = input("What is the name of your project?")
    data["Project_Name"] = project_name
    start_time = input("Enter 'Start' to begin time tracker")
    while start_time != "Start":
        start_time = input("Remember, 'Start' is case-sensitive")
    start_time = time.time()
    print(start_time)
    print(time.ctime(start_time))
    data["Start_Time"] = time.ctime(start_time)

    stop_time = input("Enter 'Stop' to stop time tracker")
    while stop_time != "Stop":
        stop_time = input("Remember, 'Stop' is case-sensitive")
    stop_time = time.time()
    print(stop_time)
    print(time.ctime(stop_time))
    data["Stop_Time"] = time.ctime(stop_time)

    time_spent = (stop_time - start_time) / 3600
    print(time_spent)
    data["Time_Spent(hours)"] = time_spent

    amount_earned = 5 * time_spent
    print("Congratulations! You earned $ " + str(amount_earned) + " in " + str(time_spent) + " hours.")
    data["Amount_Earned($)"] = amount_earned

    with open("time_tracker_data.csv", "a", newline="") as outfile:
        fieldnames = ["Project_Name", "Start_Time", "Stop_Time", "Time_Spent(hours)", "Amount_Earned($)"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        with open("time_tracker_data.csv", "r")as reader:
            read = csv.DictReader(reader)
            headers = read.fieldnames
        if headers == None:
            writer.writeheader()
            writer.writerow(data)
        else:
            writer.writerow(data)


if __name__ == '__main__':
    main()


