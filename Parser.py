from Lexer import Lexer
import ply.yacc as yacc


class MyParser(object):
    tokens = Lexer.tokens
    __Servers_A = dict()
    __A = []
    __result_file = 'PLY_analyze.txt'

    def get_A(self):
        return self.__Servers_A

    def __init__(self, from_file=False):
        self.__file = from_file
        self.lexer = Lexer()
        self.parser = yacc.yacc(module=self, optimize=True, debug=False, write_tables=False)

    def check_string(self, code):
        self.__Servers_A.clear()
        if self.__file:
            self.__f = open(self.__result_file, 'w')
        result = self.parser.parse(code)
        if self.__file:
            self.__f.close()
        return result

    # p_NAME_postfix

    def p_server_list(self, p):
        '''server_list : server
        | server_list server '''

    # int foo(...); \n
    def p_server(self, p):
        '''server : DOUBLESLASH SERVER DATA NL'''
        if len(str(p[1]) + str(p[2]) + str(p[3])) <= 100:
            if self.__file:
                self.__f.write('+ ' + str(p[1]) + str(p[2]) + str(p[3]) + '\n')
            if self.__Servers_A.get(p[2]) is None:
                self.__Servers_A.setdefault(p[2], 1)
            else:
                self.__Servers_A[p[2]] += 1
        else:
            if self.__file:
                self.__f.write('- ' + str(p[1]) + str(p[2]) + str(p[3]) + '\n')

    def p_server_zero_err_type(self, p):
        'server : err_list NL'
        if self.__file:
            self.__f.write('- ' + str(p[1]) + '\n')

    def p_server_first_err_type(self, p):
        'server : DOUBLESLASH err_list NL'
        if self.__file:
            self.__f.write('- ' + str(p[1]) + str(p[2]) + '\n')

    def p_server_second_err_type(self, p):
        'server : DOUBLESLASH SERVER err_list NL'
        if self.__file:
            self.__f.write('- ' + str(p[1]) + str(p[2]) + str(p[3]) + '\n')

    def p_server_forth_err_type(self, p):
        'server : DOUBLESLASH SERVER DATA err_list NL'
        if self.__file:
            self.__f.write('- ' + str(p[1]) + str(p[2]) + str(p[3]) + str(p[4]) + '\n')

    def p_err_list_type3(self, p):
        '''err_list : err_list err'''
        p[0] = p[1]
        p[0] += p[2]

    def p_err_list_type1(self, p):
        '''err_list : '''

    def p_err_list_type2(self, p):
        '''err_list : err'''
        p[0] = p[1]

    def p_err(self, p):
        '''err : ANY'''
        p[0] = p[1]

    # system
    def p_error(self, p):
        print('Unexpected token:', p)


if __name__ == "__main__":
    f = open(r"test.txt")
    nf = f.read()
    f.close()
    parser = MyParser()
    print(parser.check_string(nf))
