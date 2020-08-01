# PYG_32-Time-Tracker

This is a python project of a time tracking program for user projects. The user can choose to track time spent on a live project. 
The user can also choose to enter the time he/she started and ended a project that he/she has worked on.

The program then calculates the time the user spent on the project and returns the amount the user has earned working on the project. 
The project includes a csv file that contains test data collected on the program input and outputs.

To access and use the project, clone the project to your local machine and run the time_tracker.py file in your python IDE.
To contribute to the project, fork the project to your git hub repository, make the changes and create a pull request.


File: time_tracker.py
--------------------
This python file contains the main program of the project.
This file can be run in any Python supported IDE, the IDLE environment or the command line. 
The user must have python 3 installed since some program features might not be supported by python 2.

The modules imported in this program are in-built in python and you do not need to install any modules.
When you run this project, you would need to input some information in the command prompt to help track the project time and calculate amount earned.

After you run the project, you will get an output for the time spent on the project and the amount earned on the project.
The program output is also stored in a csv file for future reference.


File: time_tracker_data.csv
---------------------------
This file contains some sample data collected from the instances the program has been run. Data collected in the file
is for testing purposes only and can be cleared. When running the program, make sure this csv file is not open in Excel
as it blocks writing permissions. 

The csv file contains columns for the type of project being run(whether an old project or a current project), the times
the project starts and ends, the hours spent on the project and the amount earned for working on the project.

Every time the project runs, the new data collected is appended to previously collected data.

If the csv filename is changed in the program, a new csv file will be created and only data that is subsequently collected will be saved in that file.
The previous data collected will still be available in the old csv file.


Contributors
------------
1. Priscilla Baah: https://github.com/Priscilla-B
2. Sarah Addai: https://github.com/mansasarah
