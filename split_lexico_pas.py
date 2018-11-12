lexemas = []
listaSE = ['\'', ':=', ':', ';', '..', '.', ',', '{', '}', '(*', '*)', '(', ')', '[', ']', '=', '<>', '<=', '>=', '>', '<', '+', '-', '*', '/']

listaPR = ['program', 'var', 'const', 'type', 'procedure', 'function', 'begin', 'end', 'if', 'then', 'else', 'array', 'for', 'while', 'to', 'do', 'read', 'write', 'writeln', 'not', 'and', 'or', 'integer']

def lex_split(line, ln):
    for p in listaSE:
        line = str(line).replace(p, ' '+p+' ')
    line = line.split()
    # print(line)
    # break
    for token in line:
        if token in listaPR:
            lexemas.append({'line': ln, 'token': token, 'type': 'palavra_reservada'})
        elif token in listaSE:
            lexemas.append({'line': ln, 'token': token, 'type': 'simbolo_especial'})
        else:
            lexemas.append({'line': ln, 'token': token, 'type': 'identificador'})

def lex_print():
    for dic in lexemas:
        print('Linha: {0:3} | Tipo: {1:17} | Token: {2:30}'.format(dic['line'], dic['type'], dic['token']))
    print()

def split_file(path):
    with open(path) as f:
        ln = 0
        for line in f:
            ln += 1
            print(line)
            lex_split(line, ln)
        lex_print()
    
    return lexemas