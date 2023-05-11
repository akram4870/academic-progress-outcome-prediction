# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20221038, w1956088

# Date: 13th December 2022

#variables to store the credits
pass_credits = 0
defer_credits = 0
fail_credits = 0

numbers = [0, 20, 40, 60, 80, 100, 120] #a list to check against the input data is within the range

outcome = "" #to store the return outcome of progress and use it in other functions

close = "" # to store output of run again

student_id = 0 # variable to store student id
student_marks = {} # dictionary to store the student marks and outcomes


#a function to validate the input and loop through untill the correct inputs are entered by the user
def validation():
    global pass_credits, defer_credits, fail_credits, student_id
    student_id = str(input("Please enter your student id: "))

    while True:
        try:
            pass_credits = int(input("Please enter your credits at pass: "))
        except ValueError:
            print("Integer required")
            continue
        else:
            if pass_credits not in numbers:
                print("Out of range")
            elif pass_credits in numbers:
                break

    while True:
        try:
            defer_credits = int(input("Please enter your credits at defer: "))
        except ValueError:
            print("Integer required")
            continue
        else:
            if defer_credits not in numbers:
                print("Out of range")
            elif defer_credits in numbers:
                break

    while True:
        try:
            fail_credits = int(input("Please enter your credits at fail: "))
        except ValueError:
            print("Integer required")
            continue
        else:
            if fail_credits not in numbers:
                print("Out of range")
            elif fail_credits in numbers:
                break


#a function to loop the program and ask to enter again
def run_again():
    global close
    while True:
        print("\n")
        try:
            close = input("Would you like to enter another set of data?\n"
                          "Enter 'y' for yes or 'q' to quit and view results: ").lower()
            print("-" * 60)
        except ValueError:
            print("Please Enter 'y' or 'q'")
        else:
            if close == "q":
                break
            elif close == "y":
                break

            else:
                print("Please Enter 'y' or 'q'")

    return close


# a function to print the dictionary using a for loop and key, value pairs
def print_dictionary():
    print("Part 4")

    for key, value in student_marks.items():
        print(key, ':', value)



print("-" * 60)
while True:
    validation()
    if (pass_credits + defer_credits + fail_credits) != 120:
        print("Total incorrect")
    elif pass_credits == 120:
        outcome = "Progress"
        print(outcome)
        #to store the items to the dictionary as key and value pairs
        student_marks[student_id] = (f"{outcome} - {pass_credits} , {defer_credits}, {fail_credits}")
    elif pass_credits == 100:
        outcome = "Progress(module trailer)"
        print(outcome)
        student_marks[student_id] = (f"{outcome} - {pass_credits} ,{defer_credits}, {fail_credits}")
    elif fail_credits in range(61):
        outcome = "Do not Progress – module retriever"
        print(outcome)
        student_marks[student_id] = (f"{outcome} - {pass_credits} ,{defer_credits}, {fail_credits}")
    elif fail_credits >= 80:
        outcome = "Exclude"
        print(outcome)
        student_marks[student_id] = (f"{outcome} - {pass_credits} ,{defer_credits}, {fail_credits}")
    close = run_again()
    if close == 'q':
        print_dictionary()
        break
