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
from datetime import time as tt

# todo: include in readme that csv file should not be open in excel while running the code
# todo: include in readme that this program requires a python ide or text editor or the python idle to run
# todo: when entering date, make date project starts optional
# todo: include a welcome message
# todo: add that modules are inbuilt and do not need to be downloaded to run the program

PAY_PER_HOUR = 5  # constant(in dollars)


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
    # welcome message
    print("----------------------------------\nWelcome to the PYG-32 Time Tracker\n----------------------------------\n")
    name = input("Enter your name: ")
    print("\nHello "+name+", are you working on a new project or do you want to know your earnings on an old project?")
    project_type = input("Enter 'new' for new project and 'old' for old project: ")

    if project_type == "new":
        data["Project_Type"] = "New Project"
        project_name = input("What is the name of your project?")
        data["Project_Name"] = project_name  # append project name to dictionary
        start_time = input("\nEnter 'Start' to begin time tracker: ")

        while start_time != "Start":  # ensures program doesn't break if user doesn't enter the 'Start'correctly
            start_time = input("Remember, 'Start' is case-sensitive")
        start_time = time.time()  # returns time project started in seconds
        start_time_date_format = time.ctime(start_time)  # converts time in seconds to date format
        print("\nYou started work at "+start_time_date_format+" prompt.")  #
        data["Start_Time"] = time.ctime(start_time)  # append time started to dictionary

        print("\nWaiting to finish project....\n")

        stop_time = input("Enter 'Stop' to stop time tracker:")
        while stop_time != "Stop":  # ensures program doesn't break if user doesn't enter the 'Stop'correctly
            stop_time = input("Remember, 'Stop' is case-sensitive")
        stop_time = time.time()
        stop_time_date_format = time.ctime(stop_time)
        print("\nYou finished your project at " + str(stop_time_date_format))
        data["Stop_Time"] = time.ctime(stop_time)  # append time stopped to dictionary

        # divides time spent(in secs) by number of secs in in hour to get hour equivalent
        time_spent = round((stop_time - start_time) / 3600, 2)
        print("\nAwesome! You spent " + str(time_spent) + " hours on the project")  # tells user time spent in hours
        data["Time_Spent(hours)"] = time_spent  # append time spent to dictionary

        # calculating amount earned on project
        amount_earned = PAY_PER_HOUR * time_spent
        print("\nCongratulations! You earned $" + str(amount_earned) + " in " + str(time_spent) + " hours.")
        data["Amount_Earned($)"] = amount_earned  # append amount earned to dictionary
        return data  # returns data collected on the project for saving purpose

    if project_type == "old":
        data["Project_Type"] = "Old Project"
        project_name = input("What is the name of the project?")
        data["Project_Name"] = project_name  # append project name to dictionary

        # getting time user started project
        start_hour = int(input("\nEnter hour project started(24-hour format): "))
        start_minute = int(input("Enter minute project started: "))
        start_time_min = start_hour*60 + start_minute  # converts time started to minutes
        start_time = tt(int(start_hour), int(start_minute))  # converts user input into a time format
        data["Start_Time"] = start_time

        # getting time user ended project
        stop_hour = float(input("\nEnter hour project ended(24-hour format): "))
        stop_minute = float(input("Enter minute project ended: "))
        stop_time_min = stop_hour * 60 + stop_minute  # converts time stopped to minutes
        stop_time = tt(int(stop_hour), int(stop_minute))  # converts user input to time format
        data["Stop_Time"] = stop_time

        # divides time spent(in secs) by number of secs in in hour to get hour equivalent
        time_spent = round((stop_time_min - start_time_min) / 3600, 2)
        print("\nAwesome! You spent "+str(time_spent)+" hours on the project")  # tells user time spent in hours
        data["Time_Spent(hours)"] = time_spent  # append time spent to dictionary

        # calculating amount earned on project
        amount_earned = PAY_PER_HOUR * time_spent
        print("\nCongratulations! You earned $" + str(amount_earned) + " in " + str(time_spent) + " hours.")
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
        fieldnames = ["Project_Type", "Project_Name", "Start_Time", "Stop_Time", "Time_Spent(hours)", "Amount_Earned($)"]
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
