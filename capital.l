/*** Definition Section has one variable
which can be accessed inside yylex()
and main() ***/
%{
int count = 0;
%}
 
/*** Rule Section has three rules, first rule
matches with lowercase letters, second rule
matches with any character except newline and
third rule does not take input after the enter***/
%%
[a-z] {printf("%s is a small letter\n", yytext);
       count++;}
.     { /* Ignore other characters */ }
\n    { return 0; }
%%
 
/*** Code Section prints the number of
small letters present in the given input***/
int yywrap() { }
int main() {
    yylex();
    printf("\nNumber of Small letters "
           "in the given input - %d\n", count);
    return 0;
}
