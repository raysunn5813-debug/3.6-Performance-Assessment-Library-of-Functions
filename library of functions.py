def functionOne():
    print("My Student ID is raycan2849")

def functionTwo():
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter a number: "))
    totalSum = num1 + num2
    print(f"The sum of {num1} and {num2} is {totalSum}.")
    return totalSum

def functionThree(totalSum):
    if totalSum > 5:
        print("The sum is greater than 5.")
    else:
        print("The sum is 5 or less.")
    return 2849

def main():
    # Call functionOne to execute its print statement and output the Student ID.
    functionOne()
    # Call functionTwo to get user input, calculate the sum, and store its returned value in the variable sumResult.
    sumResult = functionTwo()
    # Call functionThree, pass sumResult as a parameter, and store the returned numeric student ID in the variable returnedId.
    returnedId = functionThree(sumResult)
    # Output the final required message displaying the numeric value returned from functionThree.
    print(f"functionThree returned the value of {returnedId}.")

main()
