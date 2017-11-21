import ox
from types import SimpleNamespace
import click

lexer = ox.make_lexer([
    ('NAME',r'[a-zA-Z]+'),
    ('NUMBER', r'\d+'),
    ('OPENING_PARENTHESES', r'\('),
    ('CLOSING_PARENTHESES', r'\)'),
    ('COMMA',r'\,'),
])

tokens_list = ['NUMBER', 'NAME','OPENING_PARENTHESES','CLOSING_PARENTHESES','COMMA']

atom_number = lambda value: ('atom_number',float(value))

parser = ox.make_parser([
    ('simple_block : simple_block simple_term', lambda first, second: (first, second)),
    ('simple_block : simple_term', lambda simple_block: simple_block),
    ('simple_term : OPENING_PARENTHESES simple_term CLOSING_PARENTHESES', lambda opening_paretheses, term, closing_parentheses: (opening_paretheses, term, closing_parentheses)),
    ('simple_term : atom simple_term',lambda first_term, second_term : (first_term, second_term)),
    ('simple_term : atom COMMA simple_term',lambda atom, comma, simple_term : (atom, comma, simple_term)),
    ('simple_term : atom', lambda term: term),
    ('atom : OPENING_PARENTHESES atom CLOSING_PARENTHESES', lambda opening_paretheses, term, closing_parentheses: (opening_paretheses, term, closing_parentheses)),
    ('atom : NUMBER', atom_number),
    ('atom : NAME',lambda name : name),
], tokens_list)

@click.command()
@click.argument('entry_file_name')

def read_file(entry_file_name):
    input_file = open(entry_file_name, 'r')
    
    args = SimpleNamespace(tokens=[]) 

    for line in input_file:
        ind = line.find(';')
        if(ind != -1):
            line = line[:ind] 
                                
        args.tokens.append(line)
                                                                                
    input_file.close()

    print(args.tokens)  

read_file()
#code = input('Enter lisp_f_ck code: ')
#tokens = lexer(code)
#print("Tokens: ",tokens)
#ast = parser(tokens)
#print("AST: ",ast)
