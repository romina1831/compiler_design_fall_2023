grammar main;


// Define the start rule for the parserrr
startRule: number+ EOF;

// Define a rule for a palindrome number
number: DIGIT+ { print("Palindrome Number:", $text); };

// Define a rule for a digit
DIGIT: [0-9];

// Define a rule for whitespace (to ignore spaces, tabs, etc.)
WS: [ \t\r\n]+ -> skip;

