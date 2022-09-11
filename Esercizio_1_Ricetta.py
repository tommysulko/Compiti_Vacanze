
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time




def preparation_time_in_minutes(num_strati):
    """
    Calculate the preparation time in minutes 
    """
    return PREPARATION_TIME * num_strati 


def elapsed_time_in_minutes(num_strati, elapsed_bake_time):
    """
    Calculate the elapsed time in minutes 
    """
    return preparation_time_in_minutes(num_strati) + elapsed_bake_time

