// Write a g4 grammar in ANTLR to describe the email formats.

grammar main;

email: mailbox '@' domain;

mailbox: word (DOT word)*;

domain: atom (DOT atom)*;

atom: [a-zA-Z0-9]+;

word: atom | quoted_string;

quoted_string:  ( ["\r\n] | '""')* ;

DOT: '.' ;

