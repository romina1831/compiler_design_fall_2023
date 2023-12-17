grammar grammer;

// Define the main rule
start: password EOF;

// Define tokens
password: PASSWORD;

// Password pattern
PASSWORD: (DIGIT | SYMBOL | UPPERCASE | ~[ \t\n\r])+;

// Define token rules
fragment DIGIT: [0-9];
fragment SYMBOL: [!@#$%^&*()_+{}\[\]:;<>,.?~\\/-];
fragment UPPERCASE: [A-Z];
