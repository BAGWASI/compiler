#Below is the implementation of a lexer for a simple mathematical expression parser written in Python. The lexer breaks down a mathematical expression into tokens like operators, numbers, variables, and functions.

#The lexer, for algebraic expressions converts a sequence of characters into a sequence of tokens. Step by step I created a simple enum type that allows me to create enums as used to from languages like C++ and Java. Then I implemented a Token class that holds all information about a token and enables me to easily print a token using the Python’s magic str method. Finally I added a Lexer class that processes character by character and returns the tokens. that resulted to the given python file.


#Overall, the lexer uses a combination of character manipulation, regular expressions, and state management to identify and tokenize different elements in a mathematical expression. The Token class encapsulates the information about each token, and the Lexer class handles the tokenization process.










import sys
import os
import re

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['key'] = reverse
    return type('Enum', (), enums)

#This creates an enumeration for different token types such as operators, functions, variables, and parentheses.
Type = enum('PLUS', 'MINUS', 'TIMES', 'DIV', 'MOD', 'EXP', 'FAC',
	'FUNC', 'VAR', 'NUMBER', 'LBRACE', 'RBRACE')


#The Token class is used to represent individual tokens with attributes like type, alias, and value.
class Token(object):
    def _init_(self, type, alias, value):
        self.type = type
        self.alias = alias
        self.value = value


    def _str_(self):
        return '{2} <{1}>'.format(self.type, self.alias, self.value)


#breaking down the input string into tokens.
class Lexer(object):

    #Initializes the lexer with the input string and sets the initial state.
    def __init__(self, stream):
        self.current = None
        self.offset = -1
        self.matchRes =None
    #The nextToken method Checks for different token types (operators, numbers, variables, etc.) using if conditions.
    #Uses regular expressions for pattern matching.
    #The getChar, getMatch, and match methods handle moving through the input string and extracting matches.
    def nextToken(self):
        if self.current is None:
            return None
        self.skipWhitespaces()
        if self.current == '+' and self.lookbefore() not in ('+','-','^','/','%'):
            return Token(Type.PLUS, Type.key[Type.PLUS], self.getChar())
        elif self.current == '-' and self.lookbefore() not in ('+','-','^','/','%'):
            return Token(Type.MINUS, Type.key[Type.MINUS], self.getChar())
        elif self.current == '*':
            return Token(Type.TIMES, Type.key[Type.TIMES], self.getChar())
        elif self.current == '/':
            return Token(Type.DIV, Type.key[Type.DIV], self.getChar())
        elif self.current == '%':
            return Token(Type.MOD, Type.key[Type.MOD], self.getChar())
        elif self.current == '^':
            return Token(Type.EXP, Type.key[Type.EXP], self.getChar())
        elif self.current == '!':
            return Token(Type.FAC, Type.key[Type.FAC], self.getChar())
        elif self.current == '(':
            return Token(Type.LBRACE, Type.key[Type.LBRACE], self.getChar())
        elif self.current == ')':
           return Token(Type.RBRACE, Type.key[Type.RBRACE], self.getChar())
        elif self.match('[a-zA-Z_][a-zA-Z0-9_]*(?=([ \t]+)?\()'):
            return Token(Type.FUNC, Type.key[Type.FUNC], self.getMatch())
        elif self.match('[+-]?[a-zA-Z_][a-zA-Z0-9_]*(?!([ \t]+)?\()'):
            return Token(Type.VAR, Type.key[Type.VAR], self.getMatch())
        elif self.match('[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?'):
            return Token(Type.NUMBER, Type.key[Type.NUMBER], self.getMatch())
        else:
            print ('No match found')


    def skipWhitespaces(self):
        while self.current.isspace():
           self.getChar()

    def getChar(self):
        if self.offset + 1 >= len(self.stream):
            return None
        result = self.stream[self.offset]
        self.offset += 1
        self.current = self.stream[self.offset]

        return result
    def getMatch(self):
        if self.matchRes is None:
            return None
        result = self.matchRes.group(0)
        self.offset += len(result)

        if self.offset + 1 >= len(self.stream):
            self.current = None
        else:
                self.current = self.stream[self.offset]
        return result
    def match(self, format):
        if self.matchRes is not None:
            return True
        else:
            return False


    #Methods to look ahead and look before the current position in the input string.   
    def lookahead(self):
        return self.stream[self.offset+1:self.offset+2]
    def lookbefore(self):
        return self.stream[self.offset-1:self.offset]
    

    #Parses command-line arguments, initializes the lexer, and prints the tokens.
    def main(argv):
        form = argv[0]

      
		
        lex = Lexer(form)
        token = lex.nextToken()
        while token is not None:
            print (token)
            token = lex.nextToken()

        else:
            print ('Invalid parameters.')
            sys.exit(1)

    
    #Executes the main function when the script is run, passing command-line arguments.
    if __name__ == "__main__":
        main(sys.argv[1:])











    

        


            
         


