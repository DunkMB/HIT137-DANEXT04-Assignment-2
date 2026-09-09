#Question 2 - Amber & Bragg
#Reading from an input text
#Open input text
from inspect import stack
from unittest import result

#Tokenize (Darren)

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
                       
        raise SyntaxError(f"Unexpected character: {c}")

    tokens.append(('EOF', ''))
    return tokens

#Level 1 Precendence and Associativity: Addition and Subtraction. Left (Darren)

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

#Level 2 Precendence and Associativity: Muptiplication (inc Implicit), Division, Percentage. Left (Darren)

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

#Level 3 Precendence and Associativity: Unary. Prefix (Darren)

def parse_three(tokens, index):
    if tokens[index][0] == 'OP' and tokens[index][1] == '-':
        index, operand, tree = parse_three(tokens, index + 1)
        return index, -operand, f"(- {tree})"
    elif tokens[index][0] == 'OP' and tokens[index][1] == '+':
        raise SyntaxError("Unary + is not supported.")
           
    return parse_four(tokens, index)

#Level 4 Precendence and Associativity: Expnentiation. Right (Darren)

def parse_four(tokens, index):
    index, result, tree = parse_base(tokens, index)
    if tokens[index][0] == 'OP' and tokens[index][1] == '^':
        index, right, right_tree = parse_four(tokens, index + 1)
        tree = f"(^ {tree} {right_tree})"
        result = result ** right
    return index, result, tree

#Base Level: Primary Values and Parentheses (Darren)

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

#Decimals: Full numbers for .0, 4 decimal places otherwise (Amber)

def format_output(value):
    if isinstance(value, (int, float)):
        if value == int(value):
            return str(int(value))
       
        rounded = round(value, 4)
        if rounded == int(rounded):
            return str(int(rounded))
           
        return f"{rounded:.4f}"
    return value

#Format tokens for output text. (Amber)
def format_tokens(tokens):
    """Formats the list of internal tokens into the requested string structure."""
    formatted = []
    for token_type, value in tokens:
        if token_type == 'NUMBER':
            formatted.append(f"[NUM:{value}]")
        elif token_type == 'OP':
            formatted.append(f"[OP:{value}]")
        elif token_type == 'LPAREN':
            formatted.append("[LPAREN:(]")
        elif token_type == 'RPAREN':
            formatted.append("[RPAREN:)]")
        elif token_type == 'EOF':
            formatted.append("[END]")
    return " ".join(formatted)

#Evaluate expression for output text. (Amber)
def evaluate(expression):
    """Evaluates an expression and returns its Tree string, Token string, and Result value."""
    if not expression.strip():
        return None, None, "Error: Empty expression"
    try:
        tokens = tokenize(expression)
        token_str = format_tokens(tokens)
       
        index, result, tree_str = parse_one(tokens, 0)
       
        if tokens[index][0] != 'EOF':
            raise SyntaxError("Unexpected tokens at end of expression")
           
        return tree_str, token_str, format_output(result)
    except (SyntaxError, ZeroDivisionError) as e:
        return "ERROR", "ERROR", f"ERROR: {str(e)}"
    except Exception:
        return "ERROR", "ERROR", "ERROR: Invalid expression"

#Import the imput text, process it and write the output text. (Amber)
def process_file(input_filename="input.txt", output_filename="output.txt"):
    """Reads expressions from input.txt and writes evaluations block-style to output.txt."""
    try:
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()
    except FileNotFoundError:
        print(f"Error: {input_filename} not found.")
        return

    results = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
           
        tree, tokens, res = evaluate(stripped)
       
        if tree is None:  # Skips completely empty inputs safely
            continue
           
        # Creates your required multiline target structural format
        results.append(f"Input: {stripped}\n")
        results.append(f"Tree: {tree}\n")
        results.append(f"Tokens: {tokens}\n")
        results.append(f"Result: {res}\n\n")
#Write output text. (Amber)
    with open(output_filename, 'w') as outfile:
        outfile.writelines(results)

if __name__ == '__main__':
    process_file()

