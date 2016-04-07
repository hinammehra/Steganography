################################################################################
#
# Description:
#
# This module implements various bit manipulation functions.
# The main purpose of the module is to help students of The University
# of Melbourne subject COMP10001 "Foundations of Computing" with their
# project for steganography. When working with characters we assume they
# are within the ASCII set, and will be encoded in exactly 8 bits, with
# zeros padding on the left where necessary.
#
# Authors:
#
# Bernie Pope (bjpope@unimelb.edu.au)
#
# Date created:
#
# 1 August 2013
#
# Date modified and reason:
#
# 10 Aug 2013: Generalised functions for setting bits to any bit in
#              an integer, not just the LSB.
# 13 Sep 2013: Update code for COMP10001 project 2, semester 2 2013.
#              Added comments.
#
################################################################################

def char_to_bits(char):
    """char_to_bits(char) -> string

    Convert the input ASCII character to an 8 bit string of 1s and 0s.

    >>> char_to_bits('A')
    '01000001'
    """
    result = ''
    char_num = ord(char)
    for index in range(8):
        result = get_bit(char_num, index) + result
    return result

def bits_to_char(bits):
    """bits_to_char(bit_string) -> char
     
    Convert a string of bits (1s and 0s) into its corresponding integer value,
    and then convert that integer value to its corresponding ASCII character.

    The input bit_string should be non-empty, and must contain only the characters
    1 and 0.

    >>> bits_to_char('01000001')
    'A'
    """
    return chr(int(bits, 2))

def get_bit(int, position):
    """get_bit(int, position) -> bit

    Return the bit (as a character, '1' or '0') from a given position
    in a given integer (interpreted in base 2).

    The least significant bit is at position 0. The second-least significant
    bit is at position 1, and so forth.

    >>> for pos in range(8):
    ...     print(b.get_bit(167, pos))
    ... 
    1
    1
    1
    0
    0
    1
    0
    1
    """
    if int & (1 << position):
        return '1'
    else:
        return '0'

def set_bit_on(int, position):
    """set_bit_on(int, position) -> int

    Set the bit at a given position in a given integer to 1,
    regardless of its previous value, and return the new integer
    as the result.

    The least significant bit is at position 0. The second-least significant
    bit is at position 1, and so forth.

    >>> set_bit_on(0, 0)
    1
    >>> set_bit_on(0, 1)
    2
    >>> set_bit_on(167, 3)
    175
    """
    return int | (1 << position)

def set_bit_off(int, position):
    """set_bit_off(int, position) -> int

    Set the bit at a given position in a given integer to 0,
    regardless of its previous value, and return the new integer
    as the result.

    The least significant bit is at position 0. The second-least significant
    bit is at position 1, and so forth.

    >>> set_bit_off(0, 0)
    0
    >>> set_bit_off(1, 0)
    0
    >>> set_bit_off(167, 0)
    166
    >>> set_bit_off(175, 3)
    167
    """
    return int & ~(1 << position)

def set_bit(int, bit, position):
    """set_bit(int, bit, position) -> int

    Set the bit at a given position to the given bit (as a char, either
    '1' or '0') regardless of its previous value, and return the new integer
    as the result.

    The least significant bit is at position 0. The second-least significant
    bit is at position 1, and so forth.

    >>> set_bit(0, '1', 0)
    1
    >>> set_bit(0, '1', 1)
    2
    >>> set_bit(0, '1', 2)
    4
    >>> set_bit(0, '1', 3)
    8
    >>> set_bit(175, '0', 3)
    167
    >>> set_bit(175, '1', 3)
    175
    """

    if bit == '1':
        return set_bit_on(int, position)
    else:
        return set_bit_off(int, position)
