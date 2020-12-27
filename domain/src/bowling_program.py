def bowling_game(frames):
    frames = str(frames)
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    spare = False
    punctutation = 0
    throw_counter = 0
    i = 0
    while throw_counter < 20:
        if frames[i] in numbers:
            if spare == True and throw_counter < 20:
                punctutation += int(frames[i]) * 2
                spare = False
            else:
                punctutation += int(frames[i])
            throw_counter += 1
            i += 1
# In case the throw has been a strike we go inside the "elif" conditional. If the strike variable is set to True we add to the punctutation 10 pins plus the strike counter that keeps the count of how many strikes we have done before this throw, if strike is not set to True means that we didn't have done an strike before and we just add to the punctutation the 10 pins we shoot down
        elif frames[i] == 'X':
            if spare == True:
                punctutation += 10 * 2
                spare = False
            else:
                punctutation += 10
            i += 1
            throw_counter += 2
            # INT - (INT, SPARE, NULL)
            if throw_counter < 20:
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
# Conditional for the wasted throws during the bowling game
        elif frames[i] == '-':
            spare = False
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
    while i < len(frames):
        if frames[i] in numbers:
            punctutation += int(frames[i])
        elif frames[i] == 'X':
            punctutation += 10
        elif frames[i] == '/':
            punctutation += 10 - int(frames[i - 1])
        else:
            continue
        i += 1
    return punctutation
