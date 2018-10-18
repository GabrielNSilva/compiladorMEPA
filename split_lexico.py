lexemas = []
listaSE = ['#', '%', '&', '\'', '"', ',', '.', '=', '++', '+', '-', '/', '*', ';', '--', '==', '<', '>', '>=', '<=', '+=', '-=', '*=', '/=', '(', ')', '[', ']', '{', '}', '!', '!=']
listaPR = ['int', 'float', 'if', 'while', 'case', 'true', 'false', 'for', 'break', 'char', 'string', 'asm', 'auto', 'const', 'continue', 'default', 'do', 'double', 'else', 'enum', 'extern', 'goto', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'try', 'class', 'catch', 'delete', 'friend', 'inline', 'new', 'oparator', 'private', 'protected', 'public', 'template', 'this', 'throw', 'vitual', '_fastcall', 'NULL']

with open('my_alloc.h') as f:
    ln = 0
    for line in f:
        ln += 1
        # print('Line '+str(ln)+': '+line)
        # token = ''
        # for char in line:
        #     token += char
        #     if(token in tokens):
        #         lexemas.append(tuple(ln, token, 'simbolo'))
        #         token = ''
        for p in listaSE:
            line = str(line).replace(p, ' '+p+' ')
        line = line.split()
        for token in line:
            if token in listaPR:
                lexemas.append({'line': ln, 'token': token, 'type': 'palavra_reservada'})
            elif token in listaSE:
                lexemas.append({'line': ln, 'token': token, 'type': 'simbolo_especial'})
            else:
                lexemas.append({'line': ln, 'token': token, 'type': 'identificador'})

    for dic in lexemas:
        # print('Linha: '+str(dic['line'])+' | Tipo: '+dic['type']+'\t| Token: '+dic['token'])
        print('Linha: {0:3} | Tipo: {1:17} | Token: {2:30}'.format(dic['line'], dic['type'], dic['token']))
    print()