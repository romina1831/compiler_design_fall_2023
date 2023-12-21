from antlr4 import InputStream, CommonTokenStream
from mainLexer import mainLexer
from mainParser import mainParser

def main():
    input_password = "YourPasswordHere"  # Replace with user input

    lexer = mainLexer(InputStream(input_password))
    parser = mainParser(CommonTokenStream(lexer))

    is_valid = parser.password().getText() == input_password
    print("Is the password valid?", is_valid)

if __name__ == "__main__":
    main()
