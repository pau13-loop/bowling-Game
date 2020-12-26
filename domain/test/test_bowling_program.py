from src.bowling_program import bowling_game
import pytest


# Integres tests
def test_integres():
    assert bowling_game(12345123451234512345) == 60
    assert bowling_game(32611661144527814225) == 71


# Nulls tests
def test_null():
    assert bowling_game('9-9-9-9-9-9-9-9-9-9-') == 90
    assert bowling_game('2-452763----4245326-') == 55


# Spares tests
def test_spare():
    assert bowling_game('5/5/5/5/5/5/5/5/5/5/5') == 150
    assert bowling_game('5/324/5/343152424152') == 82
    assert bowling_game('3/4/5/3/1/421/8/2/6/7') == 136


# Strikes spares
def test_strike():
    assert bowling_game('XXXXXXXXXXXX') == 300
    assert bowling_game('42X4225X5224524536') == 87


# Mixed tests
def test_mixed():
    assert bowling_game('625/6353X436/2441-5') == 93
