grammar main;

palindrome
    : 'z' entry EOF ;
entry
    : 'a' entry 'a'
    | 'b' entry 'b'
    | 'a'
    | 'b'
    |
    ;

WS : [ \t\r\n]+ -> skip ;
