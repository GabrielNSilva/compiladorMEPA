class Gramatica():

    def __init__(self, regras):
        self.regras = regras        
        self.primeiros = self.gen_primeiros()
        self.seguintes = self.gen_seguintes()
        self.tabela_sintatica = self.gen_tabela_sintatica()

    def __str__(self):
        string = ''
        for nt, prods in self.regras.items():
            string = string + nt + ' ⇒ '
            for p in prods:
                string = string + p + ' | '
            string = string + '\n'
        return string

    def gen_primeiros(self):
        print('Funcao primeiros')
        # if self.regras == None:
        #     return None
        # else:
        return self.regras

    def gen_seguintes(self):
        print('Funcao seguintes')
        # if self.regras == None:
        #     return None
        # else:
        return self.regras

    def gen_tabela_sintatica(self):
        print('Funcao tabela sintatica')
        # if self.regras == None:
        #     return None
        # else:
        return self.regras

    def reconhece(self, cadeia):
        cadeia.append('$')
        print('Tentado reconhecimento da cadeia ', end='')
        print(cadeia)

        pilha = ['$','E']

        while cadeia:
            print()
            print("cadeia:")
            print(cadeia)
            print("pilha:")
            print(pilha)
            print()
            topo = pilha.pop()
            if topo == cadeia[0]:
                cadeia = cadeia[1:]
            else:
                aux = self.tabela_sintatica[topo][cadeia[0]]

                if aux == None:
                    print('ERRO')
                    return False
                    
                empilha = aux[:]

                empilha.reverse()
                # print(topo)
                print(empilha)
                if empilha != ['λ']:
                    pilha = pilha + empilha
                # print(pilha)
                # break

        print('RECONHECE!')
        return True

# r = {'A': ['aA','a','B'], 'B': ['bB','b']}
# g = Gramatica(r)
# g.primeiros = {'A': ['a'], 'B': ['b']}
# print(g.primeiros)

r = {
    'E': ['TS'],
    'T': ['FG'],
    'S': ['+TS', '-TS', 'λ'],
    'G': ['*FG', '/FG', 'λ'],
    'F': ['id', 'num', '(E)']
}
g = Gramatica(r)
print(g)
g.primeiros = {
    'E': ['id', 'num', '('],
    'T': ['id', 'num', '('],
    'S': ['+', '-', 'λ'],
    'G': ['*', '/', 'λ'],
    'F': ['id', 'num', '(']
}
g.seguintes = {
    'E': [')', '$'],
    'T': ['+', '-', ')', '$'],
    'S': [')', '$'],
    'G': ['+', '-', ')', '$'],
    'F': ['*', '/', '+', '-', ')', '$']
}
g.tabela_sintatica = {
    'E': {'id': ['T','S'], 'num': ['T','S'], '+': None, '-': None, '*': None, '/': None, '(': ['T','S'], ')': None, '$': None},
    'T': {'id': ['F','G'], 'num': ['F','G'], '+': None, '-': None, '*': None, '/': None, '(': ['F','G'], ')': None, '$': None},
    'S': {'id': None, 'num': None, '+': ['+','T','S'], '-': ['-','T','S'], '*': None, '/': None, '(': None, ')': ['λ'], '$': ['λ']},
    'G': {'id': None, 'num': None, '+': ['λ'], '-': ['λ'], '*': ['*','F','G'], '/': ['/','F','G'], '(': None, ')': ['λ'], '$': ['λ']},
    'F': {'id': ['id'], 'num': ['num'], '+': None, '-': None, '*': None, '/': None, '(': ['(','E',')'], ')': None, '$': None}
}

g.reconhece(['(','id','+','num',')','-'])