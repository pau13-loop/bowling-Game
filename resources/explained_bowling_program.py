def bowling_game(frames):
    # We converted frames into a string because we want to iterate through the value of frames. We have made a list with the numbers from 1 to
    # 9, because is all possible pings we can shoot down without make a null or strike shoot. The first counter is for the punctutation of the
    # game that will be the variable that we return at the end of the program, the throw_counter to keep the number of the throws we have done
    # this game and the last one for iterate through the value of frames
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    frames = str(frames)
    score = 0
    throw_counter = 0
    i = 0
    # Loop that will work until the counter is equal or bigger than 20 because are all the possible
    # balls we can throw in a game, without count
    # the bonus ones. The first conditional statement work to check if the frame is a numerical one, the
    # second a spare, the third a null and the forth a strike.
    while throw_counter < 20:
        #! INTEGER FRAME
        # If the frame is an integer we add the number to the score we add one to the throw counter and
        # the counter 'i' to still iteratig through the frames
        if frames[i] in numbers:
            score += int(frames[i])
            throw_counter += 1
            i += 1
        #! null frame
        elif frames[i] == '-':
            i += 1
            throw_counter += 1
        #! SPARE FRAME
        # If the frame is an spare we check if the last frame has been in numbers, if it has we
        # substract it to the total number of pings, if it doesn't we add ten to the score
        elif frames[i] == '/':
            if frames[i - 1] in numbers:
                score += 10 - int(frames[i - 1])
            else:
                score += 10
            #! BONUS score for the SPARE
            # If the throw counter plus another shoot still under twenty the rules aloud the spare to get
            # the double score for the next throw. If is an strike we add ten to the score, if is an
            # integer we add the number and if is a null we add nothing. At the end we add the on shoot
            # to the throw counter from the spare and one to the counter 'i' to still iterating
            if throw_counter + 1 < 20:
                if frames[i + 1] == 'X':
                    score += 10
                elif frames[i + 1] in numbers:
                    score += int(frames[i + 1])
            throw_counter += 1
            i += 1
        #! STRIKE FRAME
        # In case the throw has been a strike. We add ten to the score, two to the throw counter because a strike accounts like two shoots and one to 'i' because we want to still iterating
        elif frames[i] == 'X':
            score += 10
            throw_counter += 2
            i += 1
            # Now we are going to check for the next two throws after a strike, because the bonus of the
            # strike is that the next two throws accounts double.
            # If the throw_counter is mminor than 20 and the next frame is an integer we add the number
            # to the score and now we check for the next frame. We check for the three possibilities
            # that can change our score, that this ones are a normal throw, a spare or a strike
            # We just made all the possible combinations that could happen after a strike.
            # INT - (INT, SPARE)
            if throw_counter < 20 and frames[i] in numbers:
                score += int(frames[i])
                # - INT
                if frames[i+1] in numbers:
                    score += int(frames[i+1])
                # - SPARE
                elif frames[i+1] == '/':
                    score += 10 - int(frames[i])
            # NULL - (INT, SPARE)
            elif frames[i] == '-':
                # - INT
                if frames[i+1] in numbers:
                    score += int(frames[i+1])
                # - SPARE
                elif frames[i+1] == '/':
                    score += 10
            # STRIKE - (INT, STRIKE)
            elif throw_counter < 20 and frames[i] == 'X':
                score += 10
                # - INT
                if frames[i+1] in numbers:
                    score += int(frames[i+1])
                # - STRIKE
                elif frames[i+1] == 'X':
                    score += 10
    #!EXTRA FRAMES
    # If we make an spare or strike in our last official frame of the game we have extra shoots. We know
    # that if we make a spare in our last throw we get an extra one and if we make a strike we get two
    # extra shootsows, but account different to our score. The bonus of strikes or spares not influence
    # our score in the extra frames
    while i < len(frames):
        if frames[i] in numbers:
            score += int(frames[i])
        elif frames[i] == 'X':
            score += 10
        elif frames[i] == '/':
            score += 10 - int(frames[i - 1])
        i += 1
    return score
