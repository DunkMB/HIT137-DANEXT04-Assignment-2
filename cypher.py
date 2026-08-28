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


def encrypt_file(char, shift1, shift2):
    if char.islower():
        index = ord(char) - ord('a')  
        if index < 13:                                               # a-m
            return chr((index + shift1 * shift2) % 26 + ord('a'))
        else:                                                        # n-z
            return chr((index - shift1 - shift2) % 26 + ord('a'))
    elif char.isupper():
        index = ord(char) - ord('A')
        if index < 13:                                               # A-M
            return chr((index - shift1) % 26 + ord('A'))
        else:                                                        # N-Z
            return chr((index + shift2 * shift2) % 26 + ord('A'))
    elif char.isdigit():                                             # if chars are digits
        return str((int(char) + shift1 - shift2) % 10)    
    else:
        return char

def encode_text(text, shift1, shift2):
    result = ""
    for char in text:
        result += encrypt_file(char, shift1, shift2)
    return result

# def decrypt_file(char, shift1, shift2):
#     if char.islower():
#         index = ord(char) - ord('a')  
#         if index < 13:                                               # a-m
#             return chr((index - shift1 * shift2) % 26 + ord('a'))
#         else:                                                        # n-z
#             return chr((index + shift1 + shift2) % 26 + ord('a'))
#     elif char.isupper():
#         index = ord(char) - ord('A')
#         if index < 13:                                               # A-M
#             return chr((index + shift1) % 26 + ord('A'))
#         else:                                                        # N-Z
#             return chr((index - shift2 * shift2) % 26 + ord('A'))
#     elif char.isdigit():                                             # if chars are digits
#         return str((int(char) - shift1 + shift2) % 10)    
#     else:
#         return char

def main():
    input_file = "raw_text.txt"
    with open(input_file, "r") as file:
        content = file.read()
    shift1 = int(input("Enter the first shift value (+ve integer): "))
    shift2 = int(input("Enter the second shift value (+ve integer): "))
    encoded = encode_text(content, shift1, shift2)

    output_file = "encrypted_text.txt"
    with open(output_file, "w") as file:
        file.write(f"{shift1}, {shift2}\n")                          # Write the shift values to the first line of the output file
        file.write(encoded)

    print(f"Done! Encoded text saved to {output_file}")

if __name__ == "__main__":
    main()


amber test push
