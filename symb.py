import re

# Symbol Table and starting address
symbol_table = {}
addr = 1000

# Function to identify token type
def get_type(token):
    if token in "+-*/=()":
        return "Operator"
    elif token.isdigit():
        return "Constant"
    elif token.isidentifier():
        return "Identifier"
    else:
        return "Unknown"

# Function to process expression
def process(expr):
    global addr

    # Tokenization using regex
    tokens = re.findall(r'[a-zA-Z_]\w*|\d+|[+\-*/=()]', expr)

    print("\nToken      Type            Address")
    print("----------------------------------------")

    for t in tokens:
        ttype = get_type(t)

        # Assign address for identifiers & constants
        if ttype in ["Identifier", "Constant"]:
            if t not in symbol_table:
                symbol_table[t] = addr
                addr += 1
            address = symbol_table[t]
        else:
            address = "-"

        # Proper formatting
        print(f"{t:<10}{ttype:<15}{address}")

# Main program
if __name__ == "__main__":
    expr = input("Enter expression: ")
    process(expr)