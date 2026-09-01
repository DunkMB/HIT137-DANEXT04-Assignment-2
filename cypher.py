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
