"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

# TODO: define the 'EXPECTED_BAKE_TIME' constant
# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(time:int):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - time

# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here

def preparation_time_in_minutes(layers:int):
    """
    :param layers: int total of layers of lasagna
    :return: int total time of preparation of layers derived from 'PREPARATION_TIME'
 
    Function that takes the number of layers that will be prepared to lasagna and returns how many minutes it will take to get done
    """
    return PREPARATION_TIME * layers

# TODO: define the 'elapsed_time_in_minutes()' function

def elapsed_time_in_minutes(layers:int, elapsed_bake_time:int):
     """
    :param layers: int total of lasagna's layers
    :param time: int baking time already elapsed
    :return: int total of time elapsed into the prepare of lasagna
 
    Function that takes as param elapsed time and total of layers and returns the sum of time elapsed in prepare and in oven
    """
     return preparation_time_in_minutes(layers) + elapsed_bake_time