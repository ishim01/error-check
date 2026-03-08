# Creating a dictionary or map to creates pairs of errors with their explanation
errors = {
    "segmentation fault": "This error occurs when a program tries to access memory it's not allowed to use.",
    "syntax error": "The code violates the rules of the programming language.",
    "index out of range": "The program attempted to access an element that does not exist in a list or array.",
    "division by zero": "A program attempted to divide a number by zero.",
    "null pointer": "The program tried to use a variable that does not reference an object."
}

print("\nWelcome to Error Check!")
print("This small program takes an error and prints out a simple easy to read explanation.")
print("Please copy and paste your entire error into the console.")

user_error_input = input("Error message: ").lower()

found = False

# If the error(key) is found at all within the user input then the explanation(value) is outputed to the screen
for error in errors:
    if error in user_error_input:
        print("Explanation:")
        print(errors[error])
        found = True
        break

#Else try again.
if not found:
    print("Error not recognized. Try another please.")