# Grammar Usage Example

## Introduction

This grammar is designed to recognize specific patterns in text, including email addresses, website addresses, decimal numbers, national numbers, and application versions.

## Grammar Rules

- `EMAIL`: Matches a typical email address ending with '@gmail.com'.
- `WEBSITE_ADDRESS`: Matches a website address starting with 'http://' and consisting of alphanumeric characters.
- `DECIMAL_NUMBER`: Matches a decimal number in the format of digits separated by a dot.
- `NATIONAL_NUMBER`: Matches a sequence of digits representing a national number.
- `APPLICATION_VERSION`: Matches an application version in the format of 'v' followed by digits and optional dot-separated subversions.

## Example

**Input:**
johndoe@gmail.com
http://example.com
42.75
123456789
v1.2.3


