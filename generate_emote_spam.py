# This is my love letter to dank memes.

# Python 2 compatibility
from six.moves import input

# Shorthand for convenience
X = "{letter}"
o = "{filler}"

ALPHABET = {}
# Organized by how final output will look. ...alternative org isn't much better
#    May want to look into an external font solution TBH
# Beware, the " " char is also basically the padding
ALPHABET[" "] = [o,
                 o,
                 o,
                 o,
                 o]
ALPHABET["A"] = [o + X + o,
                 X + o + X,
                 X + X + X,
                 X + o + X,
                 X + o + X]
ALPHABET["B"] = [X + X + o,
                 X + o + X,
                 X + X + o,
                 X + o + X,
                 X + X + o]
ALPHABET["C"] = [X + X + X,
                 X + o + o,
                 X + o + o,
                 X + o + o,
                 X + X + X]
ALPHABET["D"] = [X + X + o,
                 X + o + X,
                 X + o + X,
                 X + o + X,
                 X + X + o]
ALPHABET["E"] = [X + X + X,
                 X + o + o,
                 X + X + X,
                 X + o + o,
                 X + X + X]
ALPHABET["F"] = [X + X + X,
                 X + o + o,
                 X + X + o,
                 X + o + o,
                 X + o + o]
ALPHABET["G"] = [X + X + X + X,
                 X + o + o + o,
                 X + o + X + X,
                 X + o + o + X,
                 X + X + X + X]
ALPHABET["H"] = [X + o + X,
                 X + o + X,
                 X + X + X,
                 X + o + X,
                 X + o + X]
ALPHABET["I"] = [X + X + X,
                 o + X + o,
                 o + X + o,
                 o + X + o,
                 X + X + X]
ALPHABET["J"] = [o + o + X,
                 o + o + X,
                 o + o + X,
                 X + o + X,
                 o + X + o]
ALPHABET["K"] = [X + o + o + X,
                 X + o + X + o,
                 X + X + o + o,
                 X + o + X + o,
                 X + o + o + X]
ALPHABET["L"] = [X + o + o,
                 X + o + o,
                 X + o + o,
                 X + o + o,
                 X + X + X]
ALPHABET["M"] = [X + o + o + o + X,
                 X + X + o + X + X,
                 X + o + X + o + X,
                 X + o + o + o + X,
                 X + o + o + o + X]
ALPHABET["N"] = [X + o + o + X,
                 X + o + o + X,
                 X + X + o + X,
                 X + o + X + X,
                 X + o + o + X]
ALPHABET["O"] = [X + X + X,
                 X + o + X,
                 X + o + X,
                 X + o + X,
                 X + X + X]
ALPHABET["P"] = [X + X + X,
                 X + o + X,
                 X + X + X,
                 X + o + o,
                 X + o + o]
ALPHABET["Q"] = [X + X + X,
                 X + o + X,
                 X + o + X,
                 X + X + X,
                 o + o + X]
ALPHABET["R"] = [X + X + X,
                 X + o + X,
                 X + X + X,
                 X + X + o,
                 X + o + X]
ALPHABET["S"] = [X + X + X,
                 X + o + o,
                 X + X + X,
                 o + o + X,
                 X + X + X]
ALPHABET["T"] = [X + X + X,
                 o + X + o,
                 o + X + o,
                 o + X + o,
                 o + X + o]
ALPHABET["U"] = [X + o + X,
                 X + o + X,
                 X + o + X,
                 X + o + X,
                 X + X + X]
ALPHABET["V"] = [X + o + X,
                 X + o + X,
                 X + o + X,
                 o + X + o,
                 o + X + o]
ALPHABET["W"] = [X + o + o + o + X,
                 X + o + X + o + X,
                 X + o + X + o + X,
                 X + o + X + o + X,
                 o + X + o + X + o]
ALPHABET["X"] = [X + o + X,
                 X + o + X,
                 o + X + o,
                 X + o + X,
                 X + o + X]
ALPHABET["Y"] = [X + o + X,
                 X + o + X,
                 o + X + o,
                 o + X + o,
                 o + X + o]
ALPHABET["Z"] = [X + X + X,
                 o + o + X,
                 o + X + o,
                 X + o + o,
                 X + X + X]
ALPHABET["1"] = [X + X + o,
                 o + X + o,
                 o + X + o,
                 o + X + o,
                 X + X + X]
ALPHABET["2"] = [X + X + X,
                 o + o + X,
                 X + X + X,
                 X + o + o,
                 X + X + X]
ALPHABET["3"] = [X + X + X,
                 o + o + X,
                 o + X + X,
                 o + o + X,
                 X + X + X]
ALPHABET["4"] = [X + o + X,
                 X + o + X,
                 X + X + X,
                 o + o + X,
                 o + o + X]
ALPHABET["5"] = [X + X + X,
                 X + o + o,
                 X + X + X,
                 o + o + X,
                 X + X + X]
ALPHABET["6"] = [X + X + X,
                 X + o + o,
                 X + X + X,
                 X + o + X,
                 X + X + X]
ALPHABET["7"] = [X + X + X,
                 o + o + X,
                 o + o + X,
                 o + X + o,
                 o + X + o]
ALPHABET["8"] = [X + X + X,
                 X + o + X,
                 X + X + X,
                 X + o + X,
                 X + X + X]
ALPHABET["9"] = [X + X + X,
                 X + o + X,
                 X + X + X,
                 o + o + X,
                 o + o + X]
ALPHABET["0"] = [X + X + X + X + X,
                 X + o + o + X + X,
                 X + o + X + o + X,
                 X + X + o + o + X,
                 X + X + X + X + X]


def make_spam(spam, emote_letter, emote_filler):
    """Generate 5-row-tall memes!"""

    copypasta = [""] * 5  # Initialize row strings

    for letter in spam:
        block_letter = ALPHABET[letter.upper()]
        for row in range(0, 5):  # Put letter into copypasta row-wise
            copypasta[row] += o + block_letter[row]  # Pad left of letter

    for row in range(0, 5):
        copypasta[row] += o  # Pad end of string
        print(copypasta[row].format(letter=emote_letter, filler=emote_filler))


if __name__ == "__main__":
    spam = input("What's your spam? ")
    emote_letter = input("What's the letter emote? ")
    emote_filler = input("What's the filler emote? ")
    make_spam(spam, emote_letter, emote_filler)
