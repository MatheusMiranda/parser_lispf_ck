import ox

lexer = ox.make_lexer([
    ('NAME',r'[a-zA-Z]+'),
    ('NUMBER', r'\d+'),
])

tokens_list = ['NUMBER', 'NAME']

atom_number = lambda value: ('atom_number',float(value))

parser = ox.make_parser([
    ('simple_block : simple_term', lambda simple_block: simple_block),
    ('simple_term : simple_term atom',lambda first_term, second_term : (first_term, second_term)),
    ('simple_term : atom', lambda term: term),
    ('atom : NUMBER', atom_number),
    ('atom : NAME',lambda name : name),
], tokens_list)

code = input('Enter lisp_f_ck code: ')
tokens = lexer(code)
print("Tokens: ",tokens)
ast = parser(tokens)
print("AST: ",ast)
