# Error Check

## Description
Error Check is a simple command line tool written in Python that explains common programming errors in easy to understand language. It allows users to paste an error message into the console. Error Check then searches the message for known keywords that exist in the programs dictionary. If a match is found, Error Check prints a simple explanation of the error. The main goal is to help beginner programmers better understand common programming errors and what they entail. 

## Deliverable
The deliverable for this project is a Python program that detects common programming errors using keyword matching. The program has a collection of errors with explanations attached inside a dictionary and searches the user input for specific keywords using substring matching. This allows the program to be flexible and recognize errors even when a user pastes a full error message instead of requiring the specific key words.

## Files
Files for this project include:

error_check.py - The main Python file containing the Error Check program that detects error keywords and outputs their explanataions
README.md - Documentation that describes the project and how to run it.
reflection.md - Reflection report for this project.

## How Error Check Works
The program uses a dictionary in python to map keywords to explanations. When a user inputs an error message the program first converts the entire string into lowercase before checking if any of the stored keywords appear within the message. If a keyword is found the corresponding explanation is printed. If not found the program will inform the user that the error inputed is not recognized

## How to Run
1. Clone the repository 
https://github.com/ishim01/error-check

2. Navigate to the project directory
cd error-check

3. Run the program using the command
python3 error_check.py

4. Input the error message when prompted 

## Example
Example input:

Welcome to Error Check!
This small program takes an error and prints out a simple easy to read explanation.
Please copy and paste your entire error into the console.
Error message: Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
ZeroDivisionError: division by zero

Example output:
Explanation:
A program attempted to divide a number by zero.

Video Example here:
https://vimeo.com/1171440504

## Technologies Used
Python 
Command Line Interface
