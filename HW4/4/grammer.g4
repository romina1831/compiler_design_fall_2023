grammar grammer;

start: password EOF;

password: DIGIT{8,};

DIGIT: [0-9];
