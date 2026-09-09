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


#Question 2 - Amber & Bragg

#tokenize

def tokenize(expr_str):
    tokens = []
    i = 0
    while i < len(expr_str):
        c = expr_str[i]
        
        if c.isspace ():
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
            tokens.append(('OP', c))
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
    while tokens[index][0] == 'OP' and tokens[index][1] in ('+', '-'):
        op = tokens[index][1]
        index, right, right_tree = parse_two(tokens, index + 1)
        tree = f"({op} {tree} {right_tree})"
        if op == '+':
            result = result + right
        else:
            result = result - right
    return index, result, tree

#Level 2 Precendence and Associativity: Muptiplication (inc Implicit), Division, Percentage. Left

def parse_two(tokens, index):
    index, result, tree = parse_three(tokens, index)
    while True:
        token_type = tokens[index][0]
        token_val = tokens[index][1]

        if token_type == 'OP' and token_val in ('*', '/', '%'):
            op = token_val
            index, right, right_tree = parse_three(tokens, index + 1)
            tree = f"({op} {tree} {right_tree})"
            if op == '*':
                result = result * right
            elif op == '/':
                if right == 0:
                    result = "ERROR: Division by zero"
                else:
                    result = result / right
            elif op == '%':
                if right == 0:
                    result = "ERROR: Modulo by zero"
                else:
                    result = result % right
    
        elif token_type in ('LPAREN', 'NUMBER'):
            if token_type == 'NUMBER' and tokens[index-1][0] == 'NUMBER':
                raise SyntaxError("Adjacent numbers without an operator are invalid.")

            index, right, right_tree = parse_three(tokens, index)
            tree = f"(* {tree} {right_tree})"
            result = result * right
        else:
            break

    return index, result, tree

    #Level 3 Precendence and Associativity: Unary. Prefix

    def parse_three(tokens, index)
        if tokens[index][0] == 'OP' and tokens[index][1] == '-':
        index, operand, tree = parse_three(tokens, index + 1)
        return index, -operand, f"(- {tree})"
    elif tokens[index][0] == 'OP' and tokens[index][1] == '+':
        raise SyntaxError("Unary + is not supported.")
            
    return parse_four(tokens, index)

#Level 4 Precendence and Associativity: Expnentiation. Right 

def parse_four(tokens, index):
    index, result, tree = parse_base(tokens, index)
    if tokens[index][0] == 'OP' and tokens[index][1] == '^':
        index, right, right_tree = parse_four(tokens, index + 1)
        tree = f"(^ {tree} {right_tree})"
        result = result ** right
    return index, result, tree

#Base Level: Primary Values and Parentheses

def parse_base(tokens, index):
    token_type, token_value = tokens[index]
    
    if token_type == 'NUMBER':
        return index + 1, token_value, str(token_value)
    
    if token_type == 'LPAREN':
        index, result, tree = parse_one(tokens, index + 1)
        if tokens[index][0] != 'RPAREN':
            raise SyntaxError("Missing closing parenthesis")
        return index + 1, result, tree
    
    raise SyntaxError(f"Unexpected token: {token_value if token_value else token_type}")

#Decimals: Full numbers for .0, 4 decimal places otherwise

def format_output(value):
       
###TO DO: 
#finish decimal formatting
#token formatting for output
#rest of output file text formatting
#output file printout








                       

