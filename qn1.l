%option noyywrap

%{
#include <stdio.h>
%}

%%
[a-zA-Z]+    { printf("%s\n", yytext); }
.            ;  /* Ignore the other characters */
%%

int main() {
    yylex();
    return 0;
}
