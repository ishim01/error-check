# Reflection

## Activity Description
For EA1 I participated in a small independent development activity focused on building a simple developer tool. My goal was to create a Python program that helps explain common programming errors in simple language. The program accepts an error message as input and searches for known error keywords. It then prints a clear explanation of the error.

## Technical Decisions
The main technical decision in this project was using a dictionary to map error keywords to explanations. This dictionary functions similarly to a map in c++. This allowed the program to quickly search for known errors and display the appropriate message. I used substring matching so that users could paste a full error message instead of typing an exact command. This improves usability and makes the program more practical. 

## Contributions
I completed this project independently. My contributions include designing the program logic, implementing the Python code, testing the program with example errors, and documenting the project in the README.md file.

## Quality Assessment
The program successfully detects common programming errors and prints simple explanations. While the tool works well for basic cases, it is limited by the number of errors included in the dictionary. To improve the program I would expand the dictionary of errors and possible allow the program to read error definitions from an external file. I would also consider adding support for different programming languages and improving the user interface.