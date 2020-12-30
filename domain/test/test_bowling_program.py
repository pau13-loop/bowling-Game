from src.bowling_program import bowling_game
import pytest


# INTEGRES tests
def test_integres():
    assert bowling_game(12345123451234512345) == 60
    assert bowling_game(32611661144527814225) == 71


# NULLS tests
def test_null():
    assert bowling_game('9-9-9-9-9-9-9-9-9-9-') == 90
    assert bowling_game('2-452763----4245326-') == 55


# SPARES tests
def test_spare():
    assert bowling_game('5/5/5/5/5/5/5/5/5/5/5') == 150
    assert bowling_game('5/324/5/343152424152') == 82
    assert bowling_game('3/4/5/3/1/421/8/2/6/7') == 136


# STRIKES tests
# First throw is a strike and the following next two throws the following examples

#!First throw after a strike is an integer
#INT - INT
def test_strike_int_int():
    assert bowling_game('X24X17332542143517') == 88
    assert bowling_game('42X4225X5224524536') == 90
    assert bowling_game('3518X54X24X71X31') == 111


#INT - NULL
def test_strike_int_null():
    assert bowling_game('X6-52X7-4245722662') == 93


#INT - SPARE
def test_strike_int_spare():
    assert bowling_game('X5/35X2/4235712116') == 107


#! First throw after a strike is a null
#NULL -INT
def test_strike_null_integer():
    assert bowling_game('X-471X-84215724571') == 90


#NULL - SPARE
def test_strike_null_spare():
    assert bowling_game('X-/42X-/5215423681') == 112


#NULL -NULL
def test_strike_null_null():
    assert bowling_game('X--42X--5234411836') == 63


#!First throw after strike is another strike
#STRIKE - INT

def test_strike_strike_integer():
    assert bowling_game('XX6272X6235721662') == 119
    assert bowling_game('XX5326XX52523651') == 130


#STRIKE - STRIKE
# def test_strike_strike_strike():
    assert bowling_game('XXXXXXXXXXXX') == 300


#STRIKE - NULL
def test_strike_strike_null():
    assert bowling_game('XX-625XX-5136235') == 109


# MIXED random test cases
def test_mixed():
    assert bowling_game('625/6353X436/2441-5') == 93
    assert bowling_game('26X3/4281X422/5/2/5') == 121
    assert bowling_game('5/3/X9---2/4/XXX4/') == 169
    assert bowling_game('XX4/4/3/XX2-1-XX9') == 157
    assert bowling_game('317/4/-79/532/X4/XXX') == 148
    assert bowling_game('X7/326/XX5/435/XXX') == 174
    assert bowling_game('13635/6/8/X6/545/X7/') == 151
    assert bowling_game('4/6/XX9/X8/XXXXX') == 235
    assert bowling_game('4/X-/4/-/XX7/4/7/X') == 182
