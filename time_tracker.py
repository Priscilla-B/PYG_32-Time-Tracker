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
# todo: import decimals to format floats to two decimal places
# todo: include in readme that csv file should not be open in excel while running the code
# todo: include in readme that this program requires a python ide or text editor or the python idle to run

PAY_PER_HOUR = 5  # constant


def main():
    data = {}  # empty dictionary to collect data on the project
    get_data(data)
    save_data(data)


def get_data(data):
    """This function collects both input and output data on the project and saves the data into a dictionary.
        Input data is collected by telling user to enter project name and a 'start' or 'stop' prompt to start
        or stop a project respectively. Output data is collected on the time spent on project and the amount earned
        within that time.
    """

    project_name = input("What is the name of your project?")
    data["Project_Name"] = project_name  # append project name to dictionary
    start_time = input("\nEnter 'Start' to begin time tracker")

    while start_time != "Start":  # ensures program doesn't break if user doesn't enter the 'Start'correctly
        start_time = input("Remember, 'Start' is case-sensitive")
    start_time = time.time()  # returns time project started in seconds
    start_time_date_format = time.ctime(start_time)  # converts time in seconds to date format
    print("\nYou started work at "+start_time_date_format+" prompt.")  #
    data["Start_Time"] = time.ctime(start_time)  # append time started to dictionary

    print("\nWaiting to finish project....\n")

    stop_time = input("Enter 'Stop' to stop time tracker")
    while stop_time != "Stop":  # ensures program doesn't break if user doesn't enter the 'Stop'correctly
        stop_time = input("Remember, 'Stop' is case-sensitive")
    stop_time = time.time()
    stop_time_date_format = time.ctime(stop_time)
    print("\nYou finished your project at "+str(stop_time_date_format))
    data["Stop_Time"] = time.ctime(stop_time)  # append time stopped to dictionary

    # divides time spent(in secs) by number of secs in in hour to get hour equivalent
    time_spent = (stop_time - start_time) / 3600
    print("\nAwesome! You spent "+str(time_spent)+" hours on the project")  # tells user time spent in hours
    data["Time_Spent(hours)"] = time_spent  # append time spent to dictionary

    # calculating amount earned on project
    amount_earned = PAY_PER_HOUR * time_spent
    print("\nCongratulations! You earned $ " + str(amount_earned) + " in " + str(time_spent) + " hours.")
    data["Amount_Earned($)"] = amount_earned  # append amount earned to dictionary
    return data  # returns data collected on the project for saving purpose


def save_data(data):
    """This function takes in a dictionary containing data from the program(both input and output data)
        When it gets the data, it saves it as a csv file. In saving the data as a csv file, the function makes sure
        that new data does not write over old data every time the program runs. It also ensures that fieldnames are not
        repeated every time new data is collected.
    """

    # creating csv file
    with open("time_tracker_data.csv", "a", newline="") as outfile:
        fieldnames = ["Project_Name", "Start_Time", "Stop_Time", "Time_Spent(hours)", "Amount_Earned($)"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        # reading csv file to extract fieldnames
        with open("time_tracker_data.csv", "r")as reader:
            read = csv.DictReader(reader)
            headers = read.fieldnames

        # ensures headers are not repeated if there are already headers present
        if headers == None:
            writer.writeheader()
            writer.writerow(data)
        else:
            writer.writerow(data)


if __name__ == '__main__':
    main()


