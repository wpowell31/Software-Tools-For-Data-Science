'''Test dedup.'''
import pytest
from dedup import is_in, dedup

def test_is_in():
    '''Test is_in()'''
    assert not is_in(['a', 'b'], 1)

def test_dedup_empty():
    '''Test dedup([]).'''
    assert dedup([]) == []


def test_dedup():
    '''Testing dedup().'''
    assert dedup([1,1,1]) == [1]
    assert dedup([1,2,3]) == [1,2,3]
    assert dedup([1, '1']) == [1, '1']



