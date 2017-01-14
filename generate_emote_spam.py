# This is my love letter to dank memes.


def get_alphabet():
    """Get alphabet in accordance with meme standards."""
    alphabet = {}

    alphabet["A"] = [[0, 1, 0], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 0, 1]]
    alphabet["B"] = [[1, 1, 0], [1, 0, 1], [1, 1, 0], [1, 0, 1], [1, 1, 0]]
    alphabet["C"] = [[1, 1, 1], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 1, 1]]
    alphabet["D"] = [[1, 1, 0], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 0]]
    alphabet["E"] = [[1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 0, 0], [1, 1, 1]]
    alphabet["F"] = [[1, 1, 1], [1, 0, 0], [1, 1, 0], [1, 0, 0], [1, 0, 0]]
    alphabet["G"] = [[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1]]
    alphabet["H"] = [[1, 0, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 0, 1]]
    alphabet["I"] = [[1, 1, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]]
    alphabet["J"] = [[0, 0, 1], [0, 0, 1], [0, 0, 1], [1, 0, 1], [0, 1, 0]]
    alphabet["K"] = [[1, 0, 0, 1], [1, 0, 1, 0], [1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1]]
    alphabet["L"] = [[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 1, 1]]
    alphabet["M"] = [[1, 0, 0, 0, 1], [1, 1, 0, 1, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1]]
    alphabet["N"] = [[1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 0, 1]]
    alphabet["O"] = [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]]
    alphabet["P"] = [[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 0], [1, 0, 0]]
    alphabet["Q"] = [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1]]
    alphabet["R"] = [[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 1, 0], [1, 0, 1]]
    alphabet["S"] = [[1, 1, 1], [1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1]]
    alphabet["T"] = [[1, 1, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]]
    alphabet["U"] = [[1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]]
    alphabet["V"] = [[1, 0, 1], [1, 0, 1], [1, 0, 1], [0, 1, 0], [0, 1, 0]]
    alphabet["W"] = [[1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]]
    alphabet["X"] = [[1, 0, 1], [1, 0, 1], [0, 1, 0], [1, 0, 1], [1, 0, 1]]
    alphabet["Y"] = [[1, 0, 1], [1, 0, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0]]
    alphabet["Z"] = [[1, 1, 1], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

    return alphabet


def make_spam(spam, emote_letter, emote_filler):
    """Generate memes!"""
    alphabet = get_alphabet()

    copypasta = []

    for row in range(0, 5):
        row_string = emote_filler + " "  # Sum of one row; start with filler
        for letter in spam:
            if letter is " ":  # Blank space (baby, and I'll write your name)
                row_string += (emote_filler + " ")
                continue
            for unit in alphabet[letter.upper()][row]:
                if unit:  # if unit is true (in other words, 1)
                    row_string += (emote_letter + " ")
                else:  # 0
                    row_string += (emote_filler + " ")
            row_string += (emote_filler + " ")
        row_string += emote_filler
        copypasta.append(row_string)

    for row in range(0, 5):
        print copypasta[row]


if __name__ == "__main__":
    spam = raw_input("What's your spam? ")
    emote_letter = raw_input("What's the letter emote? ")
    emote_filler = raw_input("What's the filler emote? ")
    make_spam(spam, emote_letter, emote_filler)
