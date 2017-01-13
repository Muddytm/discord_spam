# This is my love letter to dank memes.


def get_alphabet():
    """Get alphabet in accordance with meme standards."""
    alphabet = []

    alphabet.append([[0, 1, 0], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 0, 1]])  # A
    alphabet.append([[1, 1, 0], [1, 0, 1], [1, 1, 0], [1, 0, 1], [1, 1, 0]])  # B
    alphabet.append([[1, 1, 1], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 1, 1]])  # C
    alphabet.append([[1, 1, 0], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 0]])  # D
    alphabet.append([[1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 0, 0], [1, 1, 1]])  # E
    alphabet.append([[1, 1, 1], [1, 0, 0], [1, 1, 0], [1, 0, 0], [1, 0, 0]])  # F
    alphabet.append([[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1]])  # G, 4 columns long.
    alphabet.append([[1, 0, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 0, 1]])  # H
    alphabet.append([[1, 1, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]])  # I
    alphabet.append([[0, 0, 1], [0, 0, 1], [0, 0, 1], [1, 0, 1], [0, 1, 0]])  # J
    alphabet.append([[1, 0, 0, 1], [1, 0, 1, 0], [1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1]])  # K, 4 columns long.
    alphabet.append([[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 1, 1]])  # L
    alphabet.append([[1, 0, 0, 0, 1], [1, 1, 0, 1, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1]])  # M, 5 columns long
    alphabet.append([[1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 0, 1]])  # N, 4 columns long
    alphabet.append([[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]])  # O
    alphabet.append([[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 0], [1, 0, 0]])  # P
    alphabet.append([[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1]])  # Q
    alphabet.append([[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 1, 0], [1, 0, 1]])  # R
    alphabet.append([[1, 1, 1], [1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1]])  # S
    alphabet.append([[1, 1, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]])  # T
    alphabet.append([[1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]])  # U
    alphabet.append([[1, 0, 1], [1, 0, 1], [1, 0, 1], [0, 1, 0], [0, 1, 0]])  # V
    alphabet.append([[1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]])  # W, 5 columns long
    alphabet.append([[1, 0, 1], [1, 0, 1], [0, 1, 0], [1, 0, 1], [1, 0, 1]])  # X
    alphabet.append([[1, 0, 1], [1, 0, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0]])  # Y
    alphabet.append([[1, 1, 1], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]])  # Z

    return alphabet


def make_spam(spam, emote_letter, emote_filler):
    """Generate memes!"""
    alphabet = get_alphabet()

    copypasta = []

    for row in range(0, 5):
        row_string = emote_filler + " "  # Sum of one row; start with filler
        for letter in spam:
            letter_ascii = ord(letter) - 97  # ASCII value, minus 97
            if letter_ascii < 0:  # Blank space (baby, and I'll write your name)
                row_string += (emote_filler + " ")
                continue
            for unit in alphabet[letter_ascii][row]:
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
