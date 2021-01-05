from src.main import Bowling
import pytest


# INTEGRES tests
def test_integres():
    assert 60 == Bowling('12345123451234512345').bowling_game()
    assert 71 == Bowling('32611661144527814225').bowling_game()
    #assert Bowling('32611661144527814225').bowling_game() == 71
    #assert Bowling('12345123451234512345').bowling_game() == 60
    #assert Bowling('32611661144527814225').bowling_game() == 71


# SPARES tests
def test_spare():
    assert Bowling('5/5/5/5/5/5/5/5/5/5/5').bowling_game() == 150
    assert Bowling('5/324/5/343152424152').bowling_game() == 82
    assert Bowling('3/4/5/3/1/421/8/2/6/7').bowling_game() == 136


# NULLS tests
def test_null():
    assert Bowling('9-9-9-9-9-9-9-9-9-9-').bowling_game() == 90
    assert Bowling('2-452763----4245326-').bowling_game() == 55


# STRIKES tests
# First throw is a strike and the following next two throws the following examples

#!First throw after a strike is an integer
#INT - INT
def test_strike_int_int():
    assert Bowling('X24X17332542143517').bowling_game() == 88
    assert Bowling('42X4225X5224524536').bowling_game() == 90
    assert Bowling('3518X54X24X71X31').bowling_game() == 111


#INT - NULL
def test_strike_int_null():
    assert Bowling('X6-52X7-4245722662').bowling_game() == 93


#INT - SPARE
def test_strike_int_spare():
    assert Bowling('X5/35X2/4235712116').bowling_game() == 107


#! First throw after a strike is a null
#NULL -INT
def test_strike_null_integer():
    assert Bowling('X-471X-84215724571').bowling_game() == 90


#NULL - SPARE
def test_strike_null_spare():
    assert Bowling('X-/42X-/5215423681').bowling_game() == 112


#NULL -NULL
def test_strike_null_null():
    assert Bowling('X--42X--5234411836').bowling_game() == 63


#!First throw after strike is another strike
#STRIKE - INT

def test_strike_strike_integer():
    assert Bowling('XX6272X6235721662').bowling_game() == 119
    assert Bowling('XX5326XX52523651').bowling_game() == 130


#STRIKE - STRIKE
# def test_strike_strike_strike():
    assert Bowling('XXXXXXXXXXXX').bowling_game() == 300


#STRIKE - NULL
def test_strike_strike_null():
    assert Bowling('XX-625XX-5136235').bowling_game() == 109


# MIXED random test cases
def test_mixed():
    assert Bowling('625/6353X436/2441-5').bowling_game() == 93
    assert Bowling('26X3/4281X422/5/2/5').bowling_game() == 121
    assert Bowling('5/3/X9---2/4/XXX4/').bowling_game() == 169
    assert Bowling('XX4/4/3/XX2-1-XX9').bowling_game() == 157
    assert Bowling('317/4/-79/532/X4/XXX').bowling_game() == 148
    assert Bowling('X7/326/XX5/435/XXX').bowling_game() == 174
    assert Bowling('13635/6/8/X6/545/X7/').bowling_game() == 151
    assert Bowling('4/6/XX9/X8/XXXXX').bowling_game() == 235
    assert Bowling('4/X-/4/-/XX7/4/7/X').bowling_game() == 182
    assert Bowling('2/6/X639/6/-4XXXXX').bowling_game() == 184
