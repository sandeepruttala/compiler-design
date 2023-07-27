import re

class TokenSplitter:
    def __init__(self):
        # Lists of keywords, operators, and special symbols used in the code.
        self.keywords = [
            'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double', 'else', 'enum',
                         'extern', 'float', 'for', 'goto', 'if', 'int', 'long', 'register', 'return', 'short', 'signed',
                         'sizeof', 'static', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while'
        ]
        self.operators = [
            '++', '--', '==', '+=', '-=', '*=', '/=', '%=', '!=', '<', '>', '<=', '>=', '<<', '>>', '>>=', '<<=', '?:', '+',
            '-', '*', '/', '%', '&', '|', '&&', '||', '=', '?'
        ]
        self.special_symbols = [
            '(', ')', '{', '}', '[', ']', ';', ':', ',', '.', '!', '@', '#', '$', '%', '^', '&', '*', '-', '+', '/'
        ]

        # Create regex patterns for matching operators and special symbols in the code.
        self.escaped_operators = [re.escape(i) for i in self.operators]
        self.operators_regex = '|'.join(self.escaped_operators)
        self.escaped_special_symbols = [re.escape(i) for i in self.special_symbols]
        self.special_symbols_regex = '|'.join(self.escaped_special_symbols)

    def split_tokens(self, code):
        try:
            # Remove multi-line comments (/* ... */) from the code using regex.
            code = re.sub(re.compile(r'/\*.*\*/', re.DOTALL), '', code)
            
            # Remove single-line comments (// ...) from the code using regex.
            code = re.sub(re.compile(r'//.*\n'), '', code)
            
            # Use regex to find all words, operators, and special symbols in the code and tokenize it.
            tokens = re.findall(r"\w+|" + self.operators_regex + "|" + self.special_symbols_regex, code)
            
            return tokens
        except Exception as e:
            print('Error', e)
            return []

    def identify_token_type(self, token):
        # Check if the token matches any of the predefined lists to identify its type.
        if token in self.operators:
            return 'operator'
        elif token in self.special_symbols:
            return 'special symbol'
        elif token in self.keywords:
            return 'keyword'
        elif re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*', token):
            return 'identifier'
        else:
            return 'constant'


def main():
    # Read the code from the input file.
    input_file = r'C:\Users\sande\p\college\compiler-design\input.txt'
    with open(input_file, 'r') as fp:
        code = fp.read()

    # Create a TokenSplitter object.
    tokenizer = TokenSplitter()
    
    # Tokenize the code using the TokenSplitter.
    tokens = tokenizer.split_tokens(code)

    # Identify and print the type of each token.
    for token in tokens:
        token_type = tokenizer.identify_token_type(token)
        print(f'{token} is a {token_type}')


if __name__ == "__main__":
    main()