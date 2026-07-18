target = "stump".lower()

guess = input("Please enter a 5 letter word: ").lower()

if len(guess) != 5 or not guess.isalpha():
    guess = input("Invalid guess. Please enter a 5-letter word: ").lower()
else:
    print(guess)

result = ""
guess_letters = ""
for i in range(5):
    guess_letters += guess[i]
    if guess[i] == target[i]:
        result += "2"

    elif guess[i] in target:
        if guess_letters.count(guess[i]) > target.count(guess[i]):
            result += "0"
        else:
            result += "1"

    else:
        result += "0"
print(result)