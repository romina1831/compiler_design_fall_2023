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

## example
![Screenshot (74)](https://github.com/romina1831/compiler_design_fall_2023/assets/153179325/3a11f589-e38d-4653-b4e3-7283f8f273e8)

