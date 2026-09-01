print("=" * 50)
print("HIT137 - Software Now - Assignment 2")
print("Group Name: DAN/EXT04")
print("=" * 50)
print("Group Members:")
print("_" * 50)
print(f"{'Amber Francis':<20} {'s403747':>20}")
print(f"{'Darren Bragg':<20} {'s406821':>20}")
print(f"{'Duncan Brown':<20} {'s407728':>20}")
print(f"{'Jonathan Falkner':<20} {'s400817':>20}")
print("_" * 50)
print(" " * 50)
print(" " * 50)
print(" " * 50)
print("_" * 50)
print("Question 1")
print("_" * 50)


def encrypt_file(char: str, shift1: int, shift2: int) -> str:
    if char.islower():
        index = ord(char) - ord('a')
        if index < 13:                                          # a-m
            new_index = (index + shift1 * shift2) % 13          # uses first half of alphabet for letter wrapping
        else:                                                   # n-z
            rel = index - 13
            new_index = 13 + (rel - shift1 - shift2) % 13       # uses second half of alphabet for letter wrapping
        return chr(new_index + ord('a'))
    elif char.isupper():
        index = ord(char) - ord('A')
        if index < 13:                                          # A-M
            new_index = (index - shift1) % 13                   # uses first half of alphabet for letter wrapping
        else:                                                   # N-Z
            rel = index - 13
            new_index = 13 + (rel + shift2 * shift2) % 13       # uses second half of alphabet for letter wrapping
        return chr(new_index + ord('A'))
    elif char.isdigit():
        return str((int(char) + shift1 - shift2) % 10)
    else:
        return char

def encode_text(text: str, shift1: int, shift2: int) -> str:
    result = ""
    for char in text:
        result += encrypt_file(char, shift1, shift2)
    return result


def main():
    input_file = "raw_text.txt"
    with open(input_file, "r") as file:
        content = file.read()
    shift1 = int(input("Enter the first letter shift value (+ve integer): "))
    shift2 = int(input("Enter the second letter shift value (+ve integer): "))

    # Encode the text and save to a file
    encoded = encode_text(content, shift1, shift2)
    encrypted_file = "encrypted_text.txt"
    with open(encrypted_file, "w") as file:
        file.write(encoded)
    print(f"Done! The encoded text was saved to {encrypted_file}")

if __name__ == "__main__":
    main()

#Jonathan's Component

def Decryption(char, shift1, shift2):
    if char.islower():
        index = ord(char) - ord('a')
        if index < 13:                                        # a-m
            new_index = (index - shift1 * shift2) % 13
        else:                                                  # n-z
            rel = index - 13
            new_index = 13 + (rel + shift1 + shift2) % 13
        return chr(new_index + ord('a'))
    elif char.isupper():
        index = ord(char) - ord('A')
        if index < 13:                                        # A-M
            new_index = (index + shift1) % 13
        else:                                                  # N-Z
            rel = index - 13
            new_index = 13 + (rel - shift2 * shift2) % 13
        return chr(new_index + ord('A'))
    elif char.isdigit():
        return str((int(char) - shift1 + shift2) % 10)
    else:
        return char

def decrypt_text():
    input_file = "encrypted_text.txt"
    with open(input_file, "r") as file:
        content = file.read()
    Decrypted_chars = []
    for char in content:
        Decrypted_chars.append(Decryption(char, shift1, shift2))
    Decrypted = str("".join(Decrypted_chars))

    decrypted_file = "decrypted_text.txt"
    with open(decrypted_file, "w") as file:
        file.write(Decrypted)
    print(f"Decryption Completed! Decrypted text saved to {decrypted_file}")

decrypt_text()

def comparison():
  Original_file = 'raw_text.txt'
  Decrypted_file = 'decrypted_text.txt'

  with open(Original_file, 'r') as orig_file:
    Original_text = orig_file.read().strip()
  
  with open(Decrypted_file, 'r') as decrypt_file:
    Decrypted_text = decrypt_file.read().strip()

  if Original_text == Decrypted_text:
    print('Files are identical! Encryption and Decryption process successful!')
  else:
    print('Error, please check code and/or source files. Process was unsuccessful.')
  return

comparison()