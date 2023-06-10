"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from Prac_6.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s]*n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_phrase_as_sentence(phrase):
    """
    Format a phrase as a sentence - starting with a capital and ending with a single full stop.
    >>> format_phrase_as_sentence('hello')
    'Hello.'
    >>> format_phrase_as_sentence('it is an ex parrot.')
    'It is an ex parrot.'
    >>> format_phrase_as_sentence('I love Python')
    'I love Python.'
    """
    # Capitalize the first character of the phrase
    sentence = phrase.capitalize()
    # If the sentence doesn't end with a period, add one
    if not sentence.endswith('.'):
        sentence += '.'
    return sentence


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should pass
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    # assert statements to show if Car sets the fuel correctly
    # Car's __init__ function sets the fuel to 0 by default
    test_car = Car()
    assert test_car.fuel == 0, "Car does not set fuel correctly"
    # Car's __init__ function sets the fuel to the value passed
    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Car does not set fuel correctly"


run_tests()

# Uncomment the following line and run the doctests
doctest.testmod()
