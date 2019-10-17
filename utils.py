"""
All utilities for project
"""

def type_assert(name, obj, expectation):
    """ Asserts obj has type expectation """
    assert isinstance(obj, expectation), (f'{name} expected {expectation}, '
                                          f'but found type {type(obj)}.')
