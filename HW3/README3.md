 # Grammar Usage Example

## Introduction

This grammar is designed to recognize specific patterns in text, including email addresses, website addresses, decimal numbers, national numbers, application versions, and postal codes.

## Grammar Rules

- `EMAIL`: Matches a typical email address ending with '@gmail.com'.
- `WEBSITE_ADDRESS`: Matches a website address starting with 'http://' or 'https://' and consisting of alphanumeric characters.
- `DECIMAL_NUMBER`: Matches a decimal number in the format of digits separated by a dot.
- `NATIONAL_NUMBER`: Matches a sequence of digits representing a national number.
- `APPLICATION_VERSION`: Matches an application version in the format of 'v' followed by digits and optional dot-separated subversions.
- `POSTAL_CODE`: Matches a postal code in the format of digits separated by a hyphen.

## Example
 **Input:**
```plaintext
 john.doe@gmail.com
 http://example.com
 42.75
 123456789
 v1.2.3
 12345-6789


![Screenshot (47)](https://github.com/romina1831/compiler_design_fall_2023/assets/153179325/ef4ab024-2283-4b69-8fb3-948129b3c8c4)


