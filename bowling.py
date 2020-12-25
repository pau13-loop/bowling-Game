def bowling_game(frames):
    frames = str(frames)
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    strike = False
    punctutation = 0
    strike_counter = 1
    i = 0
    while i < len(frames):
        if frames[i] in numbers:
            if strike == True:
                punctutation += int(frames[i]) * 2
                strike_counter += 1
            else:
                punctutation += int(frames[i])
            strike = False
            strike_counter = 0
            i += 1
# In case the throw has been a strike we go inside the "elif" conditional. If the strike variable is set to True we add to the punctutation 10 pins plus the strike counter that keeps the count of how many strikes we have done before this throw, if strike is not set to True means that we didn't have done an strike before and we just add to the punctutation the 10 pins we shoot down
        elif frames[i] == 'X':
            if strike == True:
                punctutation += 10 * strike_counter
            else:
                punctutation += 10
# If the strike counter is not equal to the number 3 and the throw we are looking is below the number 9 we add one to the strike counter, because we want to remember that we have done an strike for the next throws. In case we are in the last throws, the number 9, 10 or 11 we want to rest one to the strike counter because we can't still multiplying the next throws because we can't do anymore after the 12 throw
            if strike_counter != 3 and i < 9:
                strike_counter += 1
            elif i == 9 or i == 10 or i == 11:
                strike_counter -= 1
# Finally we want to add plus one to the i just to keep moving in the string of bowling frames and we want to set up the variable of strikes to True because we just have done a strike in the game
            i += 1
            strike = True
    return punctutation


if __name__ == "__main__":
    #assert bowling_game(12345123451234512345) == 60
    assert bowling_game('XXXXXXXXXXXX') == 300
