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
])

tokens_list = ['NUMBER', 'FUNCTION_DECLARATION', 'EXECUTION_BLOCK', 'READ_INPUT',
     'PRINT_OUTPUT', 'INCREMENT_OPERATOR', 'DECREMENT_OPERATOR', 
     'OPENING_BRACKET', 'CLOSING_BRACKET', 'DO_BEFORE_OPERATOR', 'DO_AFTER_OPERATOR']

code = input('Enter lisp_f_ck code:')
tokens = lexer(code)
print("Tokens: ",tokens)


