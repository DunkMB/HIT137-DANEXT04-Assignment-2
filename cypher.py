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


def cypher(char, shift1, shift2):
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

def main():
    input_file = "raw_text.txt"
    with open(input_file, "r") as file:
        content = file.read()
    shift1 = int(input("Enter the first shift value (+ve integer): "))
    shift2 = int(input("Enter the second shift value (+ve integer): "))
    encoded = cypher(content, shift1, shift2)

    output_file = "encrypted_text.txt"
    with open(output_file, "w") as file:
        file.write(f"{shift1}, {shift2}\n")                          # Write the shift values to the first line
        file.write(encoded)

    print(f"Done! Encoded text saved to {output_file}")

if __name__ == "__main__":
    main()




#Question 2

#tokenize
def tokenize(expr_str):
    tokens = []
    i = 0
    while i < len(expr_str):
        c = expr_str[i}
        
    if c.isspace ()
        i += 1
        continue
        
    if c in (' ', '\t', '\r', '\n'):
        i += 1
        continue
        
    if c == '(':
        tokens.append(('LPAREN', '('))
         i += 1
        continue
    if c == ')':
        tokens.append(('RPAREN', ')'))
         i += 1
        continue
        
    if c in '+-*/%^':
        tokens.append(('OP', char))
        i += 1
        continue
        
    if c.isdigit() or c == '.':
        start = i
        has_decimal = False
        while i < len(expr_str) and (expr_str[i].isdigit() or expr_str[i] == '.'):
            if expr_str[i] == '.':
                if has_decimal:
                    raise SyntaxError("Multiple decimal points")
                has_decimal = True
            i += 1

        num_str = expr_str[start:i]
        val = float(num_str) if has_decimal else int(num_str)
        tokens.append(('NUMBER', val))
        continue
                       
    raise SyntaxError(f"Unexpected character: {char}")

tokens.append(('EOF', ''))
return tokens

#Level 1 Precendence and Associativity: Addition and Subtraction. Left
def parse_one(tokens, index):
    index, result, tree = parse_two(tokens, index)
    while tokens[index][0] == 'OP' and tokens[index][1] in ('+'. '-'):
        op = tokens[index][1]
        index, right, right_tree = parse_two






                       

