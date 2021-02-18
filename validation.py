
def letter_check(guess_word, word):
    counter = False
    length = len(word)
    for i in range(length):
        guess_word += '_'

    i = 0
    while i < 5:
        letter = input("Enter trial number {}:  ".format(i + 1))
        letter_len = len(letter)

        for j in range(length):
            if letter_len == 1:
                if letter[0] == word[j]:
                    if letter[0] == guess_word[j]:
                        print("Letter already used in guess. PLease try again")
                        i -= 1
                        counter = False
                        break
                    else:
                        guess_word = guess_word[:j] + letter + guess_word[j + 1:]
                        counter = True
            else:
                print("Enter only a single character.")
                break
        if counter:
            i = i - 1
            print(guess_word)
            if guess_word == word:
                break
        else:
            print("letter not found. Try again")
        counter = False
        i += 1

    return guess_word
