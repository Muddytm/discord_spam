# This is my love letter to dank memes.

# Python 2 compatibility
from six.moves import input

ALPHABET = {}
ALPHABET["A"] = [[0, 1, 0], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 0, 1]]
ALPHABET["B"] = [[1, 1, 0], [1, 0, 1], [1, 1, 0], [1, 0, 1], [1, 1, 0]]
ALPHABET["C"] = [[1, 1, 1], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 1, 1]]
ALPHABET["D"] = [[1, 1, 0], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 0]]
ALPHABET["E"] = [[1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 0, 0], [1, 1, 1]]
ALPHABET["F"] = [[1, 1, 1], [1, 0, 0], [1, 1, 0], [1, 0, 0], [1, 0, 0]]
ALPHABET["G"] = [[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1]]
ALPHABET["H"] = [[1, 0, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 0, 1]]
ALPHABET["I"] = [[1, 1, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]]
ALPHABET["J"] = [[0, 0, 1], [0, 0, 1], [0, 0, 1], [1, 0, 1], [0, 1, 0]]
ALPHABET["K"] = [[1, 0, 0, 1], [1, 0, 1, 0], [1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1]]
ALPHABET["L"] = [[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 1, 1]]
ALPHABET["M"] = [[1, 0, 0, 0, 1], [1, 1, 0, 1, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1]]
ALPHABET["N"] = [[1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 0, 1]]
ALPHABET["O"] = [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]]
ALPHABET["P"] = [[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 0], [1, 0, 0]]
ALPHABET["Q"] = [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1]]
ALPHABET["R"] = [[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 1, 0], [1, 0, 1]]
ALPHABET["S"] = [[1, 1, 1], [1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1]]
ALPHABET["T"] = [[1, 1, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]]
ALPHABET["U"] = [[1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]]
ALPHABET["V"] = [[1, 0, 1], [1, 0, 1], [1, 0, 1], [0, 1, 0], [0, 1, 0]]
ALPHABET["W"] = [[1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]]
ALPHABET["X"] = [[1, 0, 1], [1, 0, 1], [0, 1, 0], [1, 0, 1], [1, 0, 1]]
ALPHABET["Y"] = [[1, 0, 1], [1, 0, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0]]
ALPHABET["Z"] = [[1, 1, 1], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
ALPHABET["1"] = [[1, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]]
ALPHABET["2"] = [[1, 1, 1], [0, 0, 1], [1, 1, 1], [1, 0, 0], [1, 1, 1]]
ALPHABET["3"] = [[1, 1, 1], [0, 0, 1], [0, 1, 1], [0, 0, 1], [1, 1, 1]]
ALPHABET["4"] = [[1, 0, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [0, 0, 1]]
ALPHABET["5"] = [[1, 1, 1], [1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1]]
ALPHABET["6"] = [[1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1]]
ALPHABET["7"] = [[1, 1, 1], [0, 0, 1], [0, 0, 1], [0, 1, 0], [0, 1, 0]]
ALPHABET["8"] = [[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1]]
ALPHABET["9"] = [[1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [0, 0, 1]]
ALPHABET["0"] = [[1, 1, 1, 1, 1], [1, 0, 0, 1, 1], [1, 0, 1, 0, 1], [1, 1, 0, 0, 1], [1, 1, 1, 1, 1]]

def make_spam(spam, emote_letter, emote_filler):
    """Generate memes!"""

    copypasta = []

    for row in range(0, 5):
        row_string = emote_filler + " "  # Sum of one row; start with filler
        for letter in spam:
            if letter is " ":  # Blank space (baby, and I'll write your name)
                row_string += (emote_filler + " ")
                continue
            for unit in ALPHABET[letter.upper()][row]:
                if unit:  # if unit is true (in other words, 1)
                    row_string += (emote_letter + " ")
                else:  # 0
                    row_string += (emote_filler + " ")
            row_string += (emote_filler + " ")
        row_string += emote_filler
        copypasta.append(row_string)

    for row in range(0, 5):
        print(copypasta[row])


if __name__ == "__main__":
    spam = input("What's your spam? ")
    emote_letter = input("What's the letter emote? ")
    emote_filler = input("What's the filler emote? ")
    make_spam(spam, emote_letter, emote_filler)
