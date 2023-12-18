grammar main;

// Define the main rule
start: (email  | website_address |  decimal_number  | national_number | application_version| postal_code )+ EOF;

// Define tokens
email: EMAIL;
website_address: WEBSITE_ADDRESS;
decimal_number: DECIMAL_NUMBER;
national_number: NATIONAL_NUMBER;
application_version: APPLICATION_VERSION;
postal_code: POSTAL_CODE;

EMAIL: [a-zA-Z0-9.%+-]+ '@gmail.com';
WEBSITE_ADDRESS: 'http://'[a-zA-Z0-9]+'.'[a-zA-Z]+ |'https://'[a-zA-Z0-9]+'.'[a-zA-Z]+;
DECIMAL_NUMBER: [0-9]+'.'[0-9]+;
NATIONAL_NUMBER: [0-9]+;
APPLICATION_VERSION: 'v' [0-9]+ ('.' [0-9]+)*;
POSTAL_CODE: [0-9]+'-'[0-9]+;