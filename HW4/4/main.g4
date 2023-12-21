grammar main;

password : PASSWORD;

PASSWORD : (UPPERCASE | SYMBOL | DIGIT | WS)+;

UPPERCASE : [A-Z];
SYMBOL : [!@#$%^&*()-_=+[\]{};:'",<.>/?];
DIGIT : [0-9];
WS : [ \t\r\n]+ -> skip; // Skip whitespaces

