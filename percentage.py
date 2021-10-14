#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Oct 2021
# This program convert levels to percentage


def calculate_percent(level):
    # This function convert levels to percentage
    # process
    if level == "4+":
        percentage = "97%"
    elif level == "4":
        percentage = "90%"
    elif level == "4-":
        percentage = "83%"
    elif level == "3+":
        percentage = "78%"
    elif level == "3":
        percentage = "75%"
    elif level == "3-":
        percentage = "71%"
    elif level == "2+":
        percentage = "68%"
    elif level == "2":
        percentage = "65%"
    elif level == "2-":
        percentage = "61%"
    elif level == "1+":
        percentage = "58%"
    elif level == "1":
        percentage = "54%"
    elif level == "1-":
        percentage = "51%"
    elif level == "R":
        percentage = "25%"
    else:
        percentage = "-1"

    return percentage


def main():
    # this is the main function
    user_level = input("Enter the level you want converted to a percentage : ")
    some_var = calculate_percent(user_level)

    # call functions & output
    if some_var == -1:
        print("{0} is an invalid input".format(user_level))
    else:
        print(
            "Level {0} has a percentage of {1}.".format(
                user_level, calculate_percent(user_level)
            )
        )

    print("\nDone.")


if __name__ == "__main__":
    main()
