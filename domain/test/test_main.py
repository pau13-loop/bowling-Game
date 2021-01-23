from src.main import BowlingScoreCard
import pytest

# INTEGRES tests


def test_integres():
    assert BowlingScoreCard('32611661144527814225').game_score() == 71
    assert BowlingScoreCard('12345123451234512345').game_score() == 60


# SPARES tests
def test_spare():
    assert BowlingScoreCard('5/5/5/5/5/5/5/5/5/5/5').game_score() == 150
    assert BowlingScoreCard('5/324/5/343152424152').game_score() == 82
    assert BowlingScoreCard('3/4/5/3/1/421/8/2/6/7').game_score() == 136


# NULLS tests
def test_null():
    assert BowlingScoreCard('9-9-9-9-9-9-9-9-9-9-').game_score() == 90
    assert BowlingScoreCard('2-452763----4245326-').game_score() == 55


# STRIKES tests
# First throw is a strike and the following next two throws the following examples

#!First throw after a strike is an integer
#INT - INT
def test_strike_int_int():
    assert BowlingScoreCard('X24X17332542143517').game_score() == 88
    assert BowlingScoreCard('42X4225X5224524536').game_score() == 90
    assert BowlingScoreCard('3518X54X24X71X31').game_score() == 111


#INT - NULL
def test_strike_int_null():
    assert BowlingScoreCard('X6-52X7-4245722662').game_score() == 93


#INT - SPARE
def test_strike_int_spare():
    assert BowlingScoreCard('X5/35X2/4235712116').game_score() == 107


#! First throw after a strike is a null
#NULL -INT
def test_strike_null_integer():
    assert BowlingScoreCard('X-471X-84215724571').game_score() == 90


#NULL - SPARE
def test_strike_null_spare():
    assert BowlingScoreCard('X-/42X-/5215423681').game_score() == 112


#NULL -NULL
def test_strike_null_null():
    assert BowlingScoreCard('X--42X--5234411836').game_score() == 63


#!First throw after strike is another strike
#STRIKE - INT

def test_strike_strike_integer():
    assert BowlingScoreCard('XX6272X6235721662').game_score() == 119
    assert BowlingScoreCard('XX5326XX52523651').game_score() == 130


#STRIKE - STRIKE
# def test_strike_strike_strike():
    assert BowlingScoreCard('XXXXXXXXXXXX').game_score() == 300


#STRIKE - NULL
def test_strike_strike_null():
    assert BowlingScoreCard('XX-625XX-5136235').game_score() == 109


# MIXED random test cases
def test_mixed():
    assert BowlingScoreCard('625/6353X436/2441-5').game_score() == 93
    assert BowlingScoreCard('26X3/4281X422/5/2/5').game_score() == 121
    assert BowlingScoreCard('5/3/X9---2/4/XXX4/').game_score() == 169
    assert BowlingScoreCard('XX4/4/3/XX2-1-XX9').game_score() == 157
    assert BowlingScoreCard('317/4/-79/532/X4/XXX').game_score() == 148
    assert BowlingScoreCard('X7/326/XX5/435/XXX').game_score() == 174
    assert BowlingScoreCard('13635/6/8/X6/545/X7/').game_score() == 151
    assert BowlingScoreCard('4/6/XX9/X8/XXXXX').game_score() == 235
    assert BowlingScoreCard('4/X-/4/-/XX7/4/7/X').game_score() == 182
    assert BowlingScoreCard('2/6/X639/6/-4XXXXX').game_score() == 184
