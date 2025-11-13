#!/usr/bin/env python3
# Created by: Shem
# Created on: 11/12/2025
# This program asks the user for a positive integer
# Then it adds all the numbers from 0 up to that integer using a while loop


def main():
    # initialize counter and total
    counter = 0
    sum = 0
    try:
        # ask user for a positive integer
        user_input = int(input("Enter a positive integer: "))
        # check if the number is positive
        if user_input < 0:
            print("Please enter a positive number.")
        else:
            # This uses a while loop to add numbers from 0 to the user input
            while counter <= user_input:
                print("Tracking", counter, "time's through loop.")
                sum = sum + counter
                counter = counter + 1
            # display the total sum
            print("The sum of the numbers from 0 to", user_input, "is:", sum)
    except ValueError:
        # if user enters something that's not an integer
        print("Invalid input! Please enter a valid positive integer.")


if __name__ == "__main__":
    main()
