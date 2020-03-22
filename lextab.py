# lextab.py. This file automatically created by PLY (version 3.11). Don't edit!
_tabversion   = '3.10'
_lextokens    = set(('ANY', 'DATA', 'DOUBLESLASH', 'NL', 'SERVER'))
_lexreflags   = 64
_lexliterals  = ''
_lexstateinfo = {'INITIAL': 'inclusive', 'server': 'exclusive', 'tail': 'exclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_DOUBLESLASH>(?m)^\\\\\\\\)|(?P<t_NL>(\\n))|(?P<t_ANY>(.))', [None, ('t_DOUBLESLASH', 'DOUBLESLASH'), ('t_NL', 'NL'), None, (None, 'ANY')])], 'server': [('(?P<t_server_SERVER>([A-Z][A-Z0-9]{,14}))|(?P<t_server_ANY>(.))|(?P<t_server_NL>(\\n))', [None, ('t_server_SERVER', 'SERVER'), None, ('t_server_ANY', 'ANY'), None, ('t_server_NL', 'NL')])], 'tail': [('(?P<t_tail_DATA>(\\\\[A-Za-z][A-Za-z0-9]{,30}[A-Za-z0-9$]?\\\\([A-Za-z][A-Za-z0-9]{,31}\\\\)*([A-Za-z][A-Za-z0-9]{,31})?))|(?P<t_tail_ANY>.)|(?P<t_tail_NL>(\\n))', [None, ('t_tail_DATA', 'DATA'), None, None, None, ('t_tail_ANY', 'ANY'), ('t_tail_NL', 'NL')])]}
_lexstateignore = {'INITIAL': '', 'server': '', 'tail': ''}
_lexstateerrorf = {'INITIAL': 't_error', 'server': 't_server_error', 'tail': 't_tail_error'}
_lexstateeoff = {}
