'''
    This program is parser for the MiniJava language.
    It is used to parse the input file and return a list of tokens
    and the respective syntactic structure
    Where the tokens are defined in the file tokens.py
    This program is based on the ply library
'''

import ply.yacc as yacc
import tokens as tk

class Parser:
    def __init__(self, file):
        self.file = file
        self.tokens = tk.tokens
        self.reserved = tk.reserved
        self.parser = yacc.yacc(module=self)
        self.parser.parse(self.file)
       
    # Programa
    def p_program(self, p):
        '''
            program : body_program
        '''

    def p_body_program(self, p):
        '''
            body_program : class_decl body_program
                | import_decl body_program
                | var_decl body_program
                | empty
        '''

    # Declaração de classe
    def p_class_decl(self, p):
        '''
            class_decl : CLASS ID EXTENDS ID LBRACE body RBRACE
                | CLASS ID LBRACE body RBRACE
                | access_modifier CLASS ID EXTENDS ID LBRACE body RBRACE
                | access_modifier CLASS ID LBRACE body RBRACE
        '''

    # Modificador de acesso
    def p_access_modifier(self, p):
        '''
            access_modifier : PUBLIC
                | PRIVATE
                | PROTECTED
        '''

    # Declaração de import
    def p_import_decl(self, p):
        '''
            import_decl : IMPORT ID DOT ID SEMICOLON
        '''

    # Declaração de variável
    def p_var_decl(self, p):
        '''
            var_decl : type ID SEMICOLON
                | type ID EQUAL expr SEMICOLON
        '''

    # Declaração de método
    def p_method_decl(self, p):
        '''
            method_decl : type ID LPAREN params RPAREN LBRACE body RBRACE
                        | access_modifier type ID LPAREN params RPAREN LBRACE body RBRACE
                        | type ID LPAREN RPAREN LBRACE body RBRACE
                        | access_modifier STATIC type ID LPAREN params RPAREN LBRACE body RBRACE
        '''

    # Declaração de parâmetros
    def p_params(self, p):
        '''
            params : type ID
                | type ID COMMA params
                | empty
        '''

    # Declaração de corpo
    def p_body(self, p):
        '''
            body : var_decl body
                | method_decl body
                | statement body
                | empty
        '''

    # Declaração de tipo
    def p_type(self, p):
        '''
            type : INT
                | BOOLEAN
                | STRING
                | ID
                | VOID
                | type LSQUARE RSQUARE
        '''

    # Declaração de expressão
    def p_expr(self, p):
        '''
            expr : expr PLUS term
                | expr MINUS term
                | term
        '''

    # Declaração de termo
    def p_term(self, p):
        '''
            term : term TIMES factor
                | term DIVIDE factor
                | factor
        '''

    # Declaração de fator
    def p_factor(self, p):
        '''
            factor : MINUS factor
                | NOT factor
                | INT_LITERAL
                | BOOLEAN_LITERAL
                | STRING_LITERAL
                | ID
                | ID LSQUARE expr RSQUARE
                | ID DOT ID
                | ID DOT ID LPAREN args RPAREN
                | ID LPAREN args RPAREN
                | NEW ID LPAREN RPAREN
                | NEW INT LSQUARE expr RSQUARE
                | LPAREN expr RPAREN
        '''
    
    # Declaração de argumentos
    def p_args(self, p):
        '''
            args : expr
                | expr COMMA args
                | empty
        '''

    # Declaração de statement
    def p_statement(self, p):
        '''
            statement : LBRACE body RBRACE
                | IF LPAREN expr RPAREN statement ELSE statement
                | IF LPAREN expr RPAREN statement
                | WHILE LPAREN expr RPAREN statement
                | SYSTEM DOT OUT DOT PRINTLN LPAREN expr RPAREN SEMICOLON
                | ID EQUALS expr SEMICOLON
                | ID LSQUARE expr RSQUARE EQUALS expr SEMICOLON
        '''
    
    # empty
    def p_empty(self, p):
        '''empty :'''
        pass

    # erro
    def p_error(self, p):
        if p:
            # print value, line and column
            print("Syntax error at '%s' line %d" % (p.value, p.lineno))
        else:
            print("Syntax error at EOF")
        exit(1)

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)


    