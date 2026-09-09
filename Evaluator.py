#Decimals: Full numbers for .0, 4 decimal places otherwise

def format_output(value):

    if isinstance(value, (int, float)):
        if value == int(value):
            return str(int(value))
       
        rounded = round(value, 4)
        if rounded == int(rounded):
            return str(int(rounded))
           
        return f"{rounded:.4f}"
    return value

"""
#Formatting the tree for the output file.
def build_expression_tree(tokens):
    tree = Tree('')
    stack.push(tree)
    current_tree = tree

    for token in tokens:
        if token == '(':
            current_tree.insertLeft('')
            stack.push(current_tree)
            current_tree = current_tree.getLeftValue()
        elif token in ['+', '-', '*', '/']:
            current_tree.setOperator(token)
            current_tree.insertRight('')
            stack.push(current_tree)
            current_tree = current_tree.getRightValue()
        elif token.isdigit():
            current_tree.setOperator(int(token))
            parent = stack.pop()
            current_tree = parent
        elif token == ')':
            current_tree = stack.pop()
        else:
            raise ValueError(f"Invalid token: {token}")

    return tree
"""
#Formatting the tokens for the output file.

def format_tokens(tokenize):
    """Formats the list of internal tokens into the requested string structure."""
    formatted = []
    for token_type, value in tokenize:
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

#Evaluating the expression and returning the tree string, token string, and result value..
def evaluate(expr_str):

    if not expr_str.strip():
        return None, None, "Error: Empty expression"
    try:
        tokens = tokenize(expr_str)
        token_str = format_tokens(tokens)
       
        index, result, tree_str = parse_one(tokens, 0)
       
        if tokens[index][0] != 'EOF':
            raise SyntaxError("Unexpected tokens at end of expression")
           
        return tree_str, token_str, format_output(result)
    except (SyntaxError, ZeroDivisionError) as e:
        return "ERROR", "ERROR", f"ERROR: {str(e)}"
    except Exception:
        return "ERROR", "ERROR", "ERROR: Invalid expression"

#Opening and processing the input file.
def process_file():
    results = []
    with open("input_text.txt", 'r') as infile:
        for line in infile:
            stripped = line.strip()
            if not stripped:
                continue
            try:
                tokens = tokenize(stripped)
                index, res, tree = parse_one(tokens, 0)
                if index != len(tokens):
                    raise SyntaxError("Unexpected token")
            except (SyntaxError, ValueError) as e:
                token_str = f"ERROR: {str(e)}"
                res_str = f"ERROR: {str(e)}"
                raise SyntaxError(f"Error processing line '{stripped}': {str(e)}")
            results.append(f"Input: {stripped}\n")
            results.append(f"Tree: {tree}\n")
            results.append(f"Tokens: {format_tokens(tokens)}\n")
            results.append(f"Result: {format_output(res)}\n\n")
#Writing the results to the output file.             
    with open("output_text.txt", 'w') as outfile:
        outfile.writelines(results)
 
if __name__ == '__main__':
    process_file()

