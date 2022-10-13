#!/usr/bin/env python3
# -*- bouncing_ball_revised -*-
"""
Bouncing Ball Calculator
Qi Nohr Chen 11/10/21

Main function is to take in the initial and stopping height of a bouncing
ball. It will also ask the user for the energy loss rate. Then the function
will return the numbers of bounces rounded to the nearest interger.

The bouncy ball calculator has 3 different validation functions and one main
function. It will count the number of bounces OVER the stopping height,
otherwise known as height_min, as well as the total time.
At the end of the program, it will ask whether the user wants to rerun the
code to do additional calculations without having to manually run it again.
"""
import time
import numpy as np

print("Welcome to Bouncy Ball Calculator!")
print("The simulator will calculate the amount of bounces that the ball " \
      "will complete before it reaches the minimum height.")
print("____________________________________________________________" \
      "________________________")
GRAVITY = 9.81 # in m/s^-2

def run_again_function():
    '''
    This function is used to ask the user whether they want to use the
    calculator again. The try and except will validate the users answer, such
    that they will have to type in either 1 or 0. 1 will restart the program
    and 0 will end the program and kindly thank the user for using the
    program. It will reject any answers that are not 1 or 0

    Raises:
        ValueError: When the user types in anything other than an integer,
        such as a string.
    '''
    while True:
        try:
            print("Would you like to calculate it again?")
            print("If you'd like to calculate again, please type either " \
                  "1 or 0")
            replay = int(input("1 or 0:")) #Integer input
            if replay == 1:
                print("Let us begin!")
                _main_()
            elif replay == 0:
                print("Thank you very much for using the Bouncy Ball " \
                      "Calculator")
                break
            else:
                print("That was not 1 or 0")
        except ValueError:
            print("That was not 1 or 0")

def validation_function_height_initial():
    '''
    Returns height_initial which will be a float.
    Validation function will check such that the input of the user is actually
    a float rather than a string. If given a string, the function will run
    again.
    Returns:
    height_initial : float
        Initial height of the ball that the user inputs into the calculator.
    Raises:
        ValueError: if the user inputs something that can't be converted
        into a float
    '''
    while True:
        try:
            print("Please input a float for a MAX HEIGHT")
            height_initial = float(input("MAX HEIGHT:")) #in m
            if height_initial < 0:
                print("That doesn't work.")
            else:
                break
        except ValueError:
            print("That wasn't a float.")
    return height_initial



def validation_function_restitution():
    '''
    Returns restitution which will be a float.
    Validation function will check such that the input of the user is actually
    a float between 0 and 1 and not anything but a float.If given a string,
    the function will run again.
    Returns:
    Bounce_efficiency: float
        Restitution of bounce that the user inputs for the ball
    Raises:
        ValueError:  if the user inputs something that can't be converted
        into a float
    '''
    while True:
        try:
            print("Please input a float for a BOUNCE EFFICIENCY between" \
                  " 0 and 1")
            bounce_efficiency = float(input("Bounce Efficiency:"))
            if bounce_efficiency >= 1 or bounce_efficiency <= 0:
                print("It has to be between 0 and 1.")
            else:
                break
        except ValueError:
            print("That wasn't a float.")
    return bounce_efficiency

def validation_function_height_min(height_validation):
    '''
    Returns height_minimum which will be a float at which the ball stops.
    Validation function will check such that the input of the user is actually
    a float rather than a string. If given a string, the function will run
    again. If the stopping height is larger than the initial, then it will
    also run again. Intial height the ball is dropped from will be the
    height_validation argument
    Args:
       height_validation: float
    Returns:
        height_minimum: float
    '''
    while True:
        try:
            print("Please input a float for the STOPPING HEIGHT")
            height_minimum = float(input("Stopping Height:")) #in m
            if height_minimum > height_validation:
                print("It has to be smaller than or equal to the max height.")
            elif height_minimum < 0:
                print("This will not work.")
            else:
                break
        except ValueError:
            print("That wasn't a float.")
    return height_minimum


def _main_():
    """
    function that runs the main code and calls all the validation functions.
    The purpose of it is to calculate the number of bounces and the individual
    times and heights using while loops. The commands outside the while loop
    will take care of the 0th bounce, as the time for that will differ from
    the n bounces that are not 0. When refering to n in any of the comments,
    it is used to refer to the number of bounces.

    The main equations used are:
         s = 1 / 2 g t^2 , to find the time

         height_after_nth_bounce = height_initial ^ bounce_efficiency
    """
    #Next few lines will use empty sets as placeholders for the height, bounce
    #number and times
    bounce_counter = [0]
    height_counter = [] #in m
    time_counter = [] #in s
    #Calling all functions and assigning variables to them
    #The printed lines are used to distinct the different sections
    height_initial = validation_function_height_initial() #in m
    print("____________________________________________________________" \
          "________________________")
    height_minimum = validation_function_height_min(height_initial) #in m
    print("____________________________________________________________" \
          "________________________")
    bounce_efficiency = validation_function_restitution()
    start_time = time.time() #Execution time start
    #Placeholder variables for the total time and number of bounces
    time_total = 0 #in s
    number = 0 #number of bounces
    height_counter.append(height_initial)
    print("____________________________________________________________" \
          "________________________")
    print("Bounce Number: ", bounce_counter[-1])
    height_counter.append(float(height_initial))
    print("Height for 0 bounces is: ", height_counter[-1], "m.")
    time_after_n_bounce = np.sqrt((2*height_initial)/GRAVITY) #in s
    time_total += time_after_n_bounce #in s
    time_counter.append(time_total)
    bounce_counter.append(1)
    height_initial = float(height_initial* bounce_efficiency)
    print("The time after 0 " \
              "bounces, is: {0:3.2f}s.".format(time_total))
    while height_initial > height_minimum: #While loop after 0th bounce
        number = number + 1  #A variable to track the number of bounces
        bounce_counter.append(number)
        print("____________________________________________________________" \
          "________________________")
        print("Bounce Number: ", number)
        height_counter.append(float(height_counter[-1]* bounce_efficiency))
        print("Height after", number, "bounces is", height_counter[-1], "m.")
        #Time calculated after the nth bounce
        time_after_n_bounce = 2*np.sqrt((2*height_counter[-1])/GRAVITY) #in s
        time_total += time_after_n_bounce #in s
        time_counter.append(time_total)
        print("The time after ", number, \
              " bounces, is: {0:3.2f}s.".format(time_after_n_bounce))
        #The next will change the height initial to the next calculated
        #height
        height_initial = (float(height_counter[-1]* bounce_efficiency))
    execution_time = (time.time() - start_time)
    print("____________________________________________________________" \
          "________________________")
    print("the total time is {0:3.2f}"  \
          "s the total bounces are {1}, with code" \
          " execution time {2:2.3f}s.".format(time_total, number,
                                              execution_time))

_main_()
run_again_function()
