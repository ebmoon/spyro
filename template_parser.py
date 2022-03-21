import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'SPLITTER', 'ID', 'INT',
    'LPAREN', 'RPAREN', 'ARROW', 'COMMA', 'HOLE', 'SEMI',
    'LT', 'LE', 'GT', 'GE', 'AND', 'OR', 'NOT', 'EQ', 'NEQ',
    'PLUS', 'MINUS', 'TIMES', 'DIV'
)

t_SPLITTER = r'\|'
t_ID = r'[A-Za-z_][A-Za-z0-9_]*'
t_INT = r'\d+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ARROW = r'->'
t_COMMA = r','
t_HOLE = r'\?\?'
t_SEMI = r';'
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_EQ = r'=='
t_NEQ = r'!='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIV = r'/'
t_ignore = ' \t\r\n'

def t_error(t):
    print("Illegal character %s" % repr(t.value[0]))
    t.lexer.skip(1)

lexer = lex.lex(debug=0)

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIV'),
    ('right', 'UMINUS')
)

def p_rulelist(p):
    '''rulelist : rule
                | rulelist rule'''

    if len(p) > 2:
        p[0] = p[1]
        p[0].append(p[2])
    else:
        p[0] = [p[1]]       

def p_rule(p):
    "rule : type symbol ARROW exprlist SEMI"
    
    p[0] = (p[1], p[2], p[4])

def p_type(p):
    "type : ID"
    
    p[0] = p[1]

def p_symbol(p):
    "symbol : ID"
    
    p[0] = p[1]

def p_exprlist(p):
    '''exprlist : expr
                | exprlist SPLITTER expr'''

    if len(p) > 2:
        p[0] = p[1]
        p[0].append(p[3])
    else:
        p[0] = [p[1]]    

def p_expr_uminus(p):
    "expr : MINUS expr %prec UMINUS"
    
    p[0] = ('UNARY', '-', p[2])

def p_expr_unaryop(p):
    "expr : NOT expr"
    
    p[0] = ('UNARY', p[1], p[2])

def p_expr_binop(p):
    '''expr : expr PLUS expr
            | expr MINUS expr
            | expr TIMES expr
            | expr DIV expr
            | expr LT expr
            | expr LE expr
            | expr GT expr
            | expr GE expr
            | expr EQ expr
            | expr NEQ expr
            | expr AND expr
            | expr OR expr'''

    p[0] = ('BINOP', p[2], p[1], p[3])

def p_expr_var(p):
    "expr : ID"

    p[0] = ('VAR', p[1])

def p_expr_num(p):
    "expr : INT"

    p[0] = ('INT', p[1])

def p_expr_call(p):
    "expr : ID LPAREN args RPAREN"

    p[0] = ('FCALL', p[1], p[3])

def p_args(p):
    '''args : expr
            | args COMMA expr'''

    if len(p) > 2:
        p[0] = p[1]
        p[0].append(p[3])
    else:
        p[0] = [p[1]]

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

class TemplateParser():
    def __init__(self, template):
        # Split input code into three parts
        template, variable_section = self.__split_section_from_code(template, 'var')
        template, relation_section = self.__split_section_from_code(template, 'relation')
        template, generator_section = self.__split_section_from_code(template, 'generator')
        template, example_section = self.__split_section_from_code(template, 'example')

        self.__implenetation = template
        self.__var_decls = self.__split_var_section(variable_section)
        self.__relations = self.__split_relation_section(relation_section)
        self.__generators = self.__split_generator_section(generator_section)
        # self.__example_generators = self.__split_example_section(example_section)

    def __split_section_from_code(self, code, section_name):
        target = section_name
        section_symbol_loc = code.find(target)
        start = code.find('{', section_symbol_loc)
        end = code.find('}', start)

        section_content = code[start+1:end]
        remainder = code[:section_symbol_loc] + code[end + 1:]

        return (remainder.strip(), section_content.strip())

    def __split_var_section(self, section_content):
        decls = [decl.strip().split() for decl in section_content.split(';')]
        return [(decl[0], decl[1]) for decl in decls[:-1]]

    def __split_relation_section(self, section_content):
        return [rel.strip() for rel in section_content.split(';')[:-1]]

    def __split_generator_section(self, section_content):
        return parser.parse(section_content)

    def __split_example_section(self, section_content):
        # To-Do: Implement
        return []

    def get_context(self):
        return {rule[1]:rule[0] for rule in self.__generators}

    def get_generator_rules(self):
        return self.__generators

    def get_implementation(self):
        return self.__implenetation + '\n\n'

    def get_arguments_defn(self):
        return ','.join([typ + ' ' + symbol for typ, symbol in self.__var_decls])

    def get_arguments_call(self):
        return ','.join(symbol for _, symbol in self.__var_decls)

    def get_variables_with_hole(self):
        def decl(typ, symbol):
            hole = '??'
            return f'\t{typ} {symbol} = {hole};'

        return '\n'.join([decl(typ, symbol) for typ, symbol in self.__var_decls])

    def get_relations(self):
        return '\n'.join(['\t' + rel + ';' for rel in self.__relations])