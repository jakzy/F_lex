# coding=utf8
import ply.lex as lex
from ply.lex import TOKEN


class Lexer(object):
    # СПИСОК СОСТОЯНИЙ
    states = (
        ('server', 'exclusive'),
        ('tail', 'exclusive'),
    )
    # СПИСОК ТОКЕНОВ
    tokens = (
        'DOUBLESLASH', 'ANY', 'NL', 'SERVER', 'DATA',
    )

    t_ANY = r'(.)'

    # ОПРЕДЕЛЕНИЕ ТОКЕНОВ
    def t_DOUBLESLASH(self, t):
        r'(?m)^\\\\'
        t.lexer.begin('server')
        return t

    def t_NL(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        return t

    def t_server_SERVER(self, t):
        r'([A-Z][A-Z0-9]{,14})'
        t.lexer.begin('tail')
        return t

    def t_server_ANY(self, t):
        r'(.)'
        t.lexer.begin('INITIAL')
        return t

    def t_server_NL(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    def t_tail_DATA(self, t):
        r'(\\[A-Za-z][A-Za-z0-9]{,30}[A-Za-z0-9$]?\\([A-Za-z][A-Za-z0-9]{,31}\\)*([A-Za-z][A-Za-z0-9]{,31})?)'
        t.lexer.begin('INITIAL')
        return t

    def t_tail_ANY(self, t):
        r'.'
        t.lexer.begin('INITIAL')
        return t

    def t_tail_NL(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    t_server_ignore = ''
    t_tail_ignore = ''
    t_ignore = ''

    # ОБРАБОТКА ОШИБОК
    def t_server_error(self, t):
        print("Illegal character in SERVER '%s'" % t.value[0])
        # t.lexer.skip(1)
        t.lexer.begin('INITIAL')

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        # t.lexer.skip(1)
        t.lexer.begin('INITIAL')

    def t_tail_error(self, t):
        print("Illegal character in TAIL'%s'" % t.value[0])
        # t.lexer.skip(1)
        t.lexer.begin('INITIAL')

    def input(self, data):
        return self.lexer.input(data)

    def token(self):
        return self.lexer.token()

    def __init__(self):
        # Build the lexer
        self.lexer = lex.lex(module=self, optimize=True)


if __name__ == "__main__":

    # f = open("..\\Functions\\sample.txt")
    # nf = f.read()
    # f.close()
    nf = input()
    lexer = Lexer()
    lexer.input(nf)
    while True:
        tok = lexer.token()  # читаем следующий токен
        if not tok:
            break
        print(tok.type, tok.value)
