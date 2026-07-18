"""
Create a Wordle program, which, given a 5 character string 
as a target word, and a 5 character string as a guess, 
return a 5 character string where:
2 = this letter is in this position
1 = this letter is in the target word but not this position
0 = this letter is either not in the target word, 
    or is not in the target word as many times as it is in the guess
"""
# Secret word to guess
target_word = "assed".lower()
# The guess
guess = "ossas".lower()
# Empty object to store result
result = ""
letter_results = []

# Loop over guess word and check each letter to see if it appears and where.
# Store each letter and it's result together in a list
for i in range(0,len(guess)):
    # If the letter is in the same place for both words, output "2"
    if guess[i] == target_word[i]:
        # result += "2"
        letter_results += [[guess[i],"2"]]
    # If the letter is in the word but not in the same place, do additional check for dupe letters
    elif guess[i] in target_word:
        if guess[0:i+1].count(guess[i]) > target_word.count(guess[i]):
            # result += "0"
            letter_results += [[guess[i],"0"]]
        else:
            # result += "1"
            letter_results += [[guess[i],"1"]]
    # If the letter isn't in the secret word, output "0"
    else:
        # result += "0"
        letter_results += [[guess[i],"0"]]

# Check if dupe letter is already in correct place,
# if so replace any "1"s with "0"s
n=0
for i in letter_results:
    # Check where more instances of letter in guess than target word
    if i[1] == "1" and guess.count(i[0]) > target_word.count(i[0]):
        # Check if letter already in a correct space. If so, replace "1 with "0"
        if ["2" if x=="1" else x for x in i] in letter_results:
            # Make sure we're not replacing "1"s that are correct
            if letter_results[0:n+1].count(i[0]) > target_word.count(i[0]):
                result += "0"
            else:
                result += i[1]
    # Otherwise keep previously calculated result
    else:
        result += i[1]
    n += 1

# Print answers
print(f"Guess was: {guess}")
print(f"Result is: {result}")