# Creating a Script that can calculate the score of a bowling game given a valid sequence of rolls for one line of American Ten-Pin bowling.

# def digit_sum(n):
#     num_str = str(n)
#     sum = 0
#     for i in range(0, len(num_str)):
#         sum += int(num_str[i])
#     return sum  

def calculate_bowling_score(bowling_line):
    score = 0
    # Separate out each frame so we can grab the final one separately. Final frame can have 3 rolls.
    line = bowling_line.upper().split(" ")
    final_frame = line[-1]
    first_nine_list = line[:-1]
    # Put values back into string for calculating the score of the first 9 frames.
    first_nine = "".join(first_nine_list)

    for i in range(len(first_nine)):
        # First deal with strike logic for the first 7 frames to avoid out of range errors. Then deal with 8th and 9th separately.
        if first_nine[i] == "X" and i < len(first_nine) - 2:
            score += 10 + int(first_nine[i+1].replace("X", "10")) + int(first_nine[i+2].replace("X", "10"))
        # Calc strike on 8th frame using final frame data.
        elif first_nine[i] == "X" and i == len(first_nine) - 2:
            score += 10 + int(first_nine[i+1].replace("X", "10")) + int(final_frame[0].replace("X", "10"))
        # Calc strike on 9th frame using final frame data.
        elif first_nine[i] == "X" and i == len(first_nine) - 1:
                # Check for spare in final frame. If spare, add 20 to score. If not, add 10 + the two rolls in the final frame.
                if final_frame[1] == "/":
                    score += 20
                else:
                    score += 10 +int(final_frame[0].replace("X", "10")) + int(final_frame[1].replace("X", "10"))
        # Logic for spares in first 8 frames. If spare, value equal to 10 + next roll. If not, add the two rolls in the frame.
        elif first_nine[i] == "/" and i < len(first_nine) - 1:
            score += 10 - int(first_nine[i-1]) + int(first_nine[i+1].replace("X", "10"))
        # Logic for spare in 9th frame. If spare, value equal to 10 + first roll of final frame. If not, add the two rolls in the frame.
        elif first_nine[i] == "/" and i == len(first_nine) - 1:
            score += 10 - int(first_nine[i-1]) + int(final_frame[0].replace("X", "10"))

        else:
            score += int(first_nine[i].replace("X", "10"))

    # Add the final frame score. Need to first check if final frame contains bonus roll or not.
    if len(final_frame) == 3:
        # check for spare, if so just to 10 + third roll.
        if final_frame[1] == "/":
            score += 10 + int(final_frame[2].replace("X", "10"))
        # If no spare, just add the three rolls, replacing any strikes with 10.
        else:
            score += int(final_frame[0].replace("X", "10")) + int(final_frame[1].replace("X", "10")) + int(final_frame[2].replace("X", "10"))
    # If no bonus roll, just need to add the two rolls as we know there can't be a spare or a strike.
    if len(final_frame) == 2:
        score += int(final_frame[0]) + int(final_frame[1])

    print(f"FINAL SCORE:: {score}")
    

bowling_line_strikes = "X X X X X X X X X XXX" # Test Strike Logic
bowling_line_spares = "1/ 2/ 3/ 4/ 5/ 6/ 7/ 8/ 9/ 1/2" # Test Spare Logic
bowling_line_numbers = "11 22 33 44 11 22 33 44 11 22" # Test Number Logic
MD_example_line = "X 45 4/ 32"

calculate_bowling_score(bowling_line_numbers)
calculate_bowling_score(bowling_line_spares)
calculate_bowling_score(bowling_line_strikes)
calculate_bowling_score(MD_example_line)
