# This is my love letter to dank memes.

# Python 2 compatibility
from six.moves import input

# Shorthand for convenience
X = "{letter}"
o = "{filler}"


def get_alphabet():
    """Get alphabet in accordance with meme standards."""

    alphabet = {}
    # Organized by how final output will look. ...alternative org isn't much better
    #    May want to look into an external font solution TBH
    # Beware, the " " char is also basically the padding
    alphabet[" "] = [o,
                     o,
                     o,
                     o,
                     o]
    alphabet["A"] = [o + X + o,
                     X + o + X,
                     X + X + X,
                     X + o + X,
                     X + o + X]
    alphabet["B"] = [X + X + o,
                     X + o + X,
                     X + X + o,
                     X + o + X,
                     X + X + o]
    alphabet["C"] = [X + X + X,
                     X + o + o,
                     X + o + o,
                     X + o + o,
                     X + X + X]
    alphabet["D"] = [X + X + o,
                     X + o + X,
                     X + o + X,
                     X + o + X,
                     X + X + o]
    alphabet["E"] = [X + X + X,
                     X + o + o,
                     X + X + X,
                     X + o + o,
                     X + X + X]
    alphabet["F"] = [X + X + X,
                     X + o + o,
                     X + X + o,
                     X + o + o,
                     X + o + o]
    alphabet["G"] = [X + X + X + X,
                     X + o + o + o,
                     X + o + X + X,
                     X + o + o + X,
                     X + X + X + X]
    alphabet["H"] = [X + o + X,
                     X + o + X,
                     X + X + X,
                     X + o + X,
                     X + o + X]
    alphabet["I"] = [X + X + X,
                     o + X + o,
                     o + X + o,
                     o + X + o,
                     X + X + X]
    alphabet["J"] = [o + o + X,
                     o + o + X,
                     o + o + X,
                     X + o + X,
                     o + X + o]
    alphabet["K"] = [X + o + o + X,
                     X + o + X + o,
                     X + X + o + o,
                     X + o + X + o,
                     X + o + o + X]
    alphabet["L"] = [X + o + o,
                     X + o + o,
                     X + o + o,
                     X + o + o,
                     X + X + X]
    alphabet["M"] = [X + o + o + o + X,
                     X + X + o + X + X,
                     X + o + X + o + X,
                     X + o + o + o + X,
                     X + o + o + o + X]
    alphabet["N"] = [X + o + o + X,
                     X + o + o + X,
                     X + X + o + X,
                     X + o + X + X,
                     X + o + o + X]
    alphabet["O"] = [X + X + X,
                     X + o + X,
                     X + o + X,
                     X + o + X,
                     X + X + X]
    alphabet["P"] = [X + X + X,
                     X + o + X,
                     X + X + X,
                     X + o + o,
                     X + o + o]
    alphabet["Q"] = [X + X + X,
                     X + o + X,
                     X + o + X,
                     X + X + X,
                     o + o + X]
    alphabet["R"] = [X + X + X,
                     X + o + X,
                     X + X + X,
                     X + X + o,
                     X + o + X]
    alphabet["S"] = [X + X + X,
                     X + o + o,
                     X + X + X,
                     o + o + X,
                     X + X + X]
    alphabet["T"] = [X + X + X,
                     o + X + o,
                     o + X + o,
                     o + X + o,
                     o + X + o]
    alphabet["U"] = [X + o + X,
                     X + o + X,
                     X + o + X,
                     X + o + X,
                     X + X + X]
    alphabet["V"] = [X + o + X,
                     X + o + X,
                     X + o + X,
                     o + X + o,
                     o + X + o]
    alphabet["W"] = [X + o + o + o + X,
                     X + o + X + o + X,
                     X + o + X + o + X,
                     X + o + X + o + X,
                     o + X + o + X + o]
    alphabet["X"] = [X + o + X,
                     X + o + X,
                     o + X + o,
                     X + o + X,
                     X + o + X]
    alphabet["Y"] = [X + o + X,
                     X + o + X,
                     o + X + o,
                     o + X + o,
                     o + X + o]
    alphabet["Z"] = [X + X + X,
                     o + o + X,
                     o + X + o,
                     X + o + o,
                     X + X + X]
    alphabet["1"] = [X + X + o,
                     o + X + o,
                     o + X + o,
                     o + X + o,
                     X + X + X]
    alphabet["2"] = [X + X + X,
                     o + o + X,
                     X + X + X,
                     X + o + o,
                     X + X + X]
    alphabet["3"] = [X + X + X,
                     o + o + X,
                     o + X + X,
                     o + o + X,
                     X + X + X]
    alphabet["4"] = [X + o + X,
                     X + o + X,
                     X + X + X,
                     o + o + X,
                     o + o + X]
    alphabet["5"] = [X + X + X,
                     X + o + o,
                     X + X + X,
                     o + o + X,
                     X + X + X]
    alphabet["6"] = [X + X + X,
                     X + o + o,
                     X + X + X,
                     X + o + X,
                     X + X + X]
    alphabet["7"] = [X + X + X,
                     o + o + X,
                     o + o + X,
                     o + X + o,
                     o + X + o]
    alphabet["8"] = [X + X + X,
                     X + o + X,
                     X + X + X,
                     X + o + X,
                     X + X + X]
    alphabet["9"] = [X + X + X,
                     X + o + X,
                     X + X + X,
                     o + o + X,
                     o + o + X]
    alphabet["0"] = [X + X + X + X + X,
                     X + o + o + X + X,
                     X + o + X + o + X,
                     X + X + o + o + X,
                     X + X + X + X + X]

    return alphabet


def make_spam(spam, emote_letter, emote_filler):
    """Generate 5-row-tall memes!"""

    block_font = get_alphabet()

    copypasta = [""] * 5  # Initialize row strings

    for letter in spam:
        block_letter = block_font[letter.upper()]
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
