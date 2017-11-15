import ox

lexer = ox.make_lexer([
    ('NUMBER', r'\d+'),
    ('FUNCTION_DECLARATION',r'def'),
    ('EXECUTION_BLOCK',r'do'),
    ('READ_INPUT',r'read'),
    ('PRINT_OUTPUT',r'print'),
    ('INCREMENT_OPERATOR',r'inc'),
    ('DECREMENT_OPERATOR',r'dec'),
    ('OPENING_BRACKET',r'\('),
    ('CLOSING_BRACKET',r'\)'),
    ('DO_BEFORE_OPERATOR',r'do\-before'),
    ('DO_AFTER_OPERATOR',r'do\-after'),
    ('ADD_OPERATOR',r'add'),
    ('SUB_OPERATOR',r'sub'),
    ('NAME',r'[a-zA-z]+\d*'),
])

tokens_list = ['NUMBER', 'FUNCTION_DECLARATION', 'EXECUTION_BLOCK', 'READ_INPUT',
     'PRINT_OUTPUT', 'INCREMENT_OPERATOR', 'DECREMENT_OPERATOR', 
     'OPENING_BRACKET', 'CLOSING_BRACKET', 'DO_BEFORE_OPERATOR', 'DO_AFTER_OPERATOR',
     'ADD_OPERATOR','SUB_OPERATOR','NAME']

atom_number = lambda value: ('atom_number',float(value))
atom_do = lambda value: ('atom_do','do')
simple_operation = lambda operator : ('simple_operation',operator)
read_operation = lambda read_operator : ('read_operation',read_operator)
print_operation = lambda print_operator : ('print_operation',print_operator)
add_operation = lambda add_operator, value : ('add_operation',(add_operator,value))
sub_operation = lambda sub_operator, value : ('sub_operation',(sub_operator,value))

parser = ox.make_parser([
    ('simple-term : simple-term atom',lambda first_term, second_term : (first_term,second_term)),
    ('simple-term : atom', lambda term: term),
    ('atom : SUB_OPERATOR NUMBER',sub_operation),
    ('atom : ADD_OPERATOR NUMBER',add_operation),
    ('atom : PRINT_OUTPUT', print_operation),
    ('atom : READ_INPUT', read_operation),
    ('atom : INCREMENT_OPERATOR', simple_operation),
    ('atom : DECREMENT_OPERATOR', simple_operation),
    ('atom : EXECUTION_BLOCK', atom_do),
    ('atom : NUMBER', atom_number),
    ('atom : NAME',lambda name : name), 
], tokens_list)

code = input('Enter lisp_f_ck code:')
tokens = lexer(code)
print("Tokens: ",tokens)
ast = parser(tokens)
print("AST: ",ast)
