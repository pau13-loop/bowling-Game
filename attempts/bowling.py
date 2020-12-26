def bowling_game(frames):
    frames = str(frames)
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    spare = False
    punctutation = 0
    throw_counter = 0
    i = 0
    while i < len(frames):
        if frames[i] in numbers:
            # if strike == True and throw_counter < 20:
            # punctutation += int(frames[i]) * bonus_strike_punctutation
            if spare == True and throw_counter < 20:
                punctutation += int(frames[i]) * 2
                spare = False
            else:
                punctutation += int(frames[i])
            throw_counter += 1
            i += 1
# In case the throw has been a strike we go inside the "elif" conditional. If the strike variable is set to True we add to the punctutation 10 pins plus the strike counter that keeps the count of how many strikes we have done before this throw, if strike is not set to True means that we didn't have done an strike before and we just add to the punctutation the 10 pins we shoot down
        elif frames[i] == 'X':
            punctutation += 10
            i += 1
            throw_counter += 2
            # INT - (INT, SPARE, NULL)
            if frames[i] in numbers:
                punctutation += int(frames[i])
                # - INT
                if frames[i+1] in numbers:
                    punctutation += int(frames[i+1])
                # - SPARE
                elif frames[i+1] == '/':
                    punctutation += 10 - int(frames[i])
                # - NULL
                elif frames[i+1] == '-':
                    continue
            # NULL - (INT, SPARE, NULL)
            elif frames[i] == '-':
                # - INT
                if frames[i+1] in numbers:
                    punctutation += int(frames[i+1])
                # - SPARE
                elif frames[i+1] == '/':
                    if frames[i] == '-':
                        punctutation += 10
                    else:
                        punctutation += 10 - int(frames[i])
                # - NULL
                elif frames[i+1] == '-':
                    continue
            # STRIKE - (INT, STRIKE, NULL)
            elif frames[i] == 'X':
                punctutation += 10
                # - INT
                if frames[i+1] in numbers:
                    punctutation += int(frames[i+1])
                # - STRIKE
                elif frames[i+1] == 'X':
                    punctutation += 10
                # - NULL
                elif frames[i+1] == '-':
                    continue
            """
        if strike == True and throw_counter < 20:
            punctutation += 10 * bonus_strike_punctutation
        else:
            punctutation += 10
# If the strike counter is not equal to the number 3 and the throw we are looking is below the number 9 we add one to the strike counter, because we want to remember that we have done an strike for the next throws. In case we are in the last throws, the number 9, 10 or 11 we want to rest one to the strike counter because we can't still multiplying the next throws because we can't do anymore after the 12 throw
# Finally we want to add plus one to the i just to keep moving in the string of bowling frames and we want to set up the variable of strikes to True because we just have done a strike in the game
        bonus_strike_punctutation += 1
            """
        # strike = True
# Conditional for the wasted throws during the bowling game
        elif frames[i] == '-':
            i += 1
            throw_counter += 1
            continue
# Conditional in case the throw is a spare
        elif frames[i] == '/':
            if frames[i - 1] == '-':
                punctutation += 10
            else:
                punctutation += 10 - int(frames[i - 1])
            spare = True
            throw_counter += 1
            i += 1
    return punctutation


if __name__ == "__main__":
    #!INTEGRES
    # assert bowling_game(12345123451234512345) == 60
    #!NULL
    # assert bowling_game('9-9-9-9-9-9-9-9-9-9-') == 90
    #!SPARES
    # assert bowling_game('5/5/5/5/5/5/5/5/5/5/5') == 150
    # assert bowling_game('5/324/5/343152424152') == 82
    # assert bowling_game('3/4/5/3/1/421/8/2/6/7') == 136
    #!STRIKES
    #! FIRST IS AN INT
    # INT - INT
    assert bowling_game('X24X17332542143517') == 88
    assert bowling_game('42X4225X5224524536') == 90
    assert bowling_game('3518X54X24X71X31') == 111
    # INT - NULL
    # assert bowling_game('X6-52X7-4245722662') == 93
    # INT - SPARE
    # assert bowling_game('X5/35X2/4235712116') == 107
    #! FIRST IS A NULL
    # NULL - INT
    # assert bowling_game('X-471X-84215724571') == 90
    # NULL - SPARE
    # assert bowling_game('X-/42X-/5215423681') == 112
    # NULL - NULL
    # assert bowling_game('X--42X--5234411836') == 63
    #! FIRST IS A STRIKE
    # STRIKE - INT
    #assert bowling_game('XX6272X6235721662') == 119
    #assert bowling_game('XX5326XX52523651') == 130
    # STRIKE - STRIKE
    #!assert bowling_game('XXXXXXXXXXXX') == 300
    # STRIKE - NULL
    #assert bowling_game('XX-625XX-5136235') == 109
    #!MIXED

    #!assert bowling_game('625/6353X436/2441-5') == 93
