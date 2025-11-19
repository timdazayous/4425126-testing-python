def to_absolute(number):
    """
        Return the absolute value

        :param number: Initial number
        :return:  The absolute value

        >>> to_absolute(3)
        3
        >>> to_absolute(-10)
        10
        >>> to_absolute(-10)
        -10
    """
    if number <= 0:
        return -number
    return number

from source import reverse_str

def test_should_reverse_string():
    assert reverse_str('abc') == 'cba'