import random


def random_number_in_range(min_number, max_number):
    """
    Generate a random number within the specified scope.

    :param min_number: The minimum value of the range.
    :param max_number: The maximum value of the range.
    :return: A random integer between min_number and max_number.
    """

    return random.randint(min_number, max_number)
