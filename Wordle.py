"""
Create a Wordle program, which, given a 5 character string 
as a target word, and a 5 character string as a guess, 
return a 5 character string where:
2 = this letter is in this position
1 = this letter is in the target word but not this position
0 = this letter is either not in the target word, 
    or is not in the target word as many times as it is in the guess
"""

target_word = "Stink".lower()

guess = "Stops".lower()
result = ""

for i in range(0,len(guess)):
    if guess[i] == target_word[i]:
        result += "2"
    elif guess[i] in target_word:
        result += "1"
    else:
        result += "0"

print(f"Result is: {result}")