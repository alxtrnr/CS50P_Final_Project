# The Hundred Pushups Training Program

### **Video Demo:** [VID DEMO]()

### **Description:** 
Coded for my [CS50’s Introduction to Programming with Python](https://cs50.harvard.edu/python/2022/) final project. A 
terminal based python app to go through The Hundred Pushups Training Program. Inspired by and taken from 
[The Hundred Pushups Training Program](https://hundredpushups.com/). I completed the program myself a few years ago and 
completed 100 pushups!

Functionality includes: create/save username and age; record test results; automatically calculate rank at each key 
stage of the program; view the training program for each day and week of the six-week program.

* ```project.py```Contains the base class and functions of the app. A "Person" class creates a user instance. An instance 
method works on user entered values (instance attributes) to calculate a rank. This may be referenced to measure 
progress through the training program.  
\
Username is called to name the file to save details and progress to. The Pickle
module is used for saving details. This keeps things simple. Security risk mitigated as only data created by the user is
unpickled.  
\
Functions to display a menu, to create a user, to access each day/week of the program, to perform and record test
results, to save progress and to exit the program are all coded here.  
\
Effort has been made to catch exception errors from user input. Mostly while loops and try statements.  
\
Three additional functions have been added for testing / project submission purposes. These functions simply return 
default instance attributes as called. The main tests coded apply to the class instance methods. While more "advanced" 
these tests alone do not fulfill project submission requirements, hence the extra functions and testing. The value and 
process of TDD is acknowledged. Lesson learned! 


* ```text_blocks.py``` Text describing and guiding the user as they work through the training program. Coded to be 
imported to aid the review and navigation of ```project.py``` Lots of text made it a chore to work on. Each block of 
text has instead been wrapped within its own function making it simple to call when needed thus avoiding clutter in 
the main code. 


* ```pushup_tables.py``` Tables displaying sets/reps of pushups for each day of the training program. Coded to be imported
for the reasons described above.


* ```test_project.py``` Tests to check the functionality of class and instance method (calculate rank). Three additional 
tests were included simply to meet project requirements. 


* ```requirements.txt``` A simple text file that saves a list of the modules and packages required by the project. The 
creation of a Python ```requirements.txt``` file, saves you the hassle of having to track down and install all the 
required modules manually.


* ```README.md``` You are reading it! Contains information about the project.





    
