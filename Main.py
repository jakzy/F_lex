import re
import time
from Parser import MyParser


print('>>OPTIONS<<\n1. Check strings in a small test file\n2. Check strings in a 1 000 000 file\n3. Enter strings yourself\n0. Exit')
System = dict()
parser = MyParser()
while True:
    choice = input()
    if choice == '1':
        System.clear()

        _data = open('test.txt', 'r')
        _time = open('test_time.txt', 'w')
        _result = open('test_servers.txt', 'w')
        nf = _data.read()
        _data.close()

        start_time = time.perf_counter()
        parser = MyParser(True)
        parser.check_string(nf)
        System = parser.get_A()
        _time.write(str(time.perf_counter() - start_time) + '\n')
        _time.close()
        for i in System:
            _result.write(i + '\t' + str(System[i]) + '\n')
        _result.close()
    elif choice == '2':
        System.clear()

        _data = open(r'C:\Users\1\PycharmProjects\my_first_project\test.txt', 'r')
        _time = open('PLY_time.txt', 'a')
        _result = open('PLY_servers.txt', 'w')
        nf = _data.read()
        _data.close()

        start_time = time.perf_counter()
        parser = MyParser(True)
        parser.check_string(nf)
        System = parser.get_A()
        _time.write(str(time.perf_counter() - start_time) + '\n')
        _time.close()
        for i in System:
            _result.write(i + '\t' + str(System[i]) + '\n')
        _result.close()
    elif choice == '3':
        System.clear()
        parser = MyParser(False)
        nf = ''
        print('Enter string or 0 to get the results:')
        while nf != '0\n':
            nf = input()
            nf += '\n'
            parser.check_string(nf)
            if parser.get_A().keys():
                print("+ " + nf)
                res = list(parser.get_A().keys())[0]
            else:
                print("- " + nf)
        System = parser.get_A()
        for i in System:
            print(i + '\t' + str(System[i]) + '\n')
    elif choice == '0':
        print('Work finished, bye!\n')
        break
    else:
        print('Enter error!\n')
