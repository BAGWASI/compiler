LAB1;
QN1; The rule [ \t\n]+ matches and ignores spaces and newlines.

      The rule [a-zA-Z]+ matches words (sequences of alphabetic characters) and prints them using printf.
QN2;The  rule [a-z] matches lowercase letters. 
    The rule .(\n) matches any character except newline (\n) and ignores it. This ensures that only lowercase letters are processed, and other characters are ignored.
    The  rule \n matches newline characters and returns 0, effectively ending the lexer's operation.
