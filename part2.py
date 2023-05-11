# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20221038

# Date: 13th December 2022

#variables to store the credits
pass_credits = 0
defer_credits = 0
fail_credits = 0

numbers = [0, 20, 40, 60, 80, 100, 120] #a list to check against the input data is within the range

outcome = "" #to store the return outcome of progress and use it in other functions

close = "" # to store output of run again

#variables to count the number of input data
progress_count = 0
trailer_count = 0
retriever_count = 0
excluded_count = 0

# four empty lists to store the outcome
progress = []
trailer = []
retriever = []
exclude = []


#a function to validate the input and loop through untill the correct inputs are entered by the user
def validation():
    global pass_credits, defer_credits, fail_credits #global used to modify global variable

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



#a fucntions to print the histogram
def histogram_print():
    print("\n")
    print("-" * 60)
    print("Histogram\n")
    print("Progress", progress_count, " :", "*" * progress_count)
    print("Trailer", trailer_count, "  :", "*" * trailer_count)
    print("Retriever", retriever_count, ":", "*" * retriever_count)
    print("Excluded", excluded_count, " :", "*" * excluded_count)
    total_outcomes = progress_count + trailer_count + retriever_count + excluded_count
    print("\n")
    print(total_outcomes, "outcomes in total.")
    print("-" * 60)


#Code reference
#https://youtu.be/xlkf9eECcSw

def list_print(): #a function to print the list on to the screen
    print("Part 2:\n")
    seperator = ","
    for i in range(len(progress)):
        print("Progress -",seperator.join(map(str, progress[i])))
        i+=1
    for i in range(len(trailer)):
        print("Progress (module trailer) -", seperator.join(map(str, trailer[i])))
        i+=1
    for i in range(len(retriever)):
        print("Module retriever -", seperator.join(map(str, retriever[i])))
        i+=1
    for i in range(len(exclude)):
        print("Exclude -", seperator.join(map(str, exclude[i])))
        i+=1



print("-" * 60)
while True:
    validation()
    if (pass_credits + defer_credits + fail_credits) != 120:
        print("Total incorrect")
    elif pass_credits == 120:
        outcome = "Progress"
        print(outcome)
        progress_count += 1
        progress.append([pass_credits, defer_credits, fail_credits])
    elif pass_credits == 100:
        outcome = "Progress(module trailer)"
        print(outcome)
        trailer_count += 1
        trailer.append([pass_credits, defer_credits, fail_credits])
    elif fail_credits in range(61):
        outcome = "Do not Progress – module retriever"
        print(outcome)
        retriever_count += 1
        retriever.append([pass_credits, defer_credits, fail_credits])
    elif fail_credits >= 80:
        outcome = "Exclude"
        print(outcome)
        excluded_count += 1
        exclude.append([pass_credits, defer_credits, fail_credits])
    close = run_again()
    if close == 'q':
        histogram_print()
        list_print()
        break
