import pytest
from main import hopcroft_minimize

def test_simple_dfa():
    accepting = {1}
    alphabet = {'a', 'b'}
    inverse_trans = {
        ('a', 0): {0, 1},
        ('b', 0): {0},
        ('a', 1): {0},
        ('b', 1): {1},
    }
    result = hopcroft_minimize(accepting, alphabet, inverse_trans)
    assert result == {frozenset({0}), frozenset({1})}

# [Include all other test cases from earlier]
