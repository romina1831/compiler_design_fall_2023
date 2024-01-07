# Password Grammar

This grammar defines a simple structure for password validation in a formal language specification. The grammar is written in ANTLR, a powerful parser generator.

## Grammar Rules

### `password`
- This rule represents the entire password and is defined as one or more occurrences of the `CHAR` rule.

### `CHAR`
- The `CHAR` rule defines a single character of the password and can be either an uppercase letter, lowercase letter, digit, symbol, or the end of the file (`EOF`).

### `DIGIT`
- This rule represents any digit from 0 to 9.

### `UPPERCASE`
- This rule represents any uppercase letter from A to Z.

### `LOWERCASE`
- This rule represents any lowercase letter from a to z.

### `SYMBOL`
- This rule represents any symbol character. Symbols include ! @ # $ % ^ & * ( ) - = _ + { } [ ] | ; ' : " , . < > ? /

### `WS`
- This rule skips whitespace characters such as tabs, carriage returns, and newlines.

## Usage

To use this grammar, you can generate a parser using ANTLR and then integrate it into your desired programming language. The grammar is designed to validate passwords based on the specified rules.

### Example:

```java
// Sample code in Java using ANTLR runtime
CharStream input = CharStreams.fromString("your_password_here");
PasswordGrammarLexer lexer = new PasswordGrammarLexer(input);
CommonTokenStream tokens = new CommonTokenStream(lexer);
PasswordGrammarParser parser = new PasswordGrammarParser(tokens);

// Use the generated parser to parse the input
parser.password();
