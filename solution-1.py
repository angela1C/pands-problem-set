# solution-1.py
# This is my  solution to problem 1 on the Problem Set 2019.
# Angela Carpenter 
# 31st March 2019

# This program asks the user to input any positive integer and outputs the sum of all numbers between one and that number

# When an exception is detected by the statements between try and except, python jumps to the exception handling statement and executes these. 
# The program then continues at the next line after the exception handling clause.
# If no exception is raised then the exception handling statements are skipped.
# A ValueError is raised if the input is not an integer as it expects an integer. 
# A ValueError is when the right type of argument is received but an inappropriate value



# This code asks the user to input a valid positive integer until a valid input in entered
while True:
    # while True, execute the `try` statements. 
    try:
        x = int(input("Please enter a positive integer: ")) 
        if x < 0:
            ## raise a ValueError if the input is a negative number. This will be the right type but an inappropriate value
           raise ValueError
         # break out of the loop.
        break  
    ## if an exception does occur within the try clause, then skip the rest of the try statements and go to the except statements.
    except ValueError:

        print("That was not a positive integer. Please try again")

 # set up a variable called total to hold the total sum
total = 0 

# This program must calculate the sum of all integers between 1 and the number.
# The while loop will finish once the x gets to 1.
while x >= 1:
        # While x >1 add the value of x to total (which is 0 to start) so the total is increasing each time by the value of x
    total += x  
        # For each iteration of the while loop, reduce x by 1. Once x is 1, the while will evaluate to false and the loop ends. 
    x -= 1  
    # Print the final value that `total` returns from the while loop. 
print (total)

        



