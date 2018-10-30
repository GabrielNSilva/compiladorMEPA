class Gramatica():

    def __init__(self, regras):
        self.regras = regras        
        self.primeiros = self.gen_primeiros()
        self.seguintes = self.gen_seguintes()

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
        if self.regras == None:
            return None
        else:
            return self.regras

    def gen_seguintes(self):
        print('Funcao seguintes')
        if self.regras == None:
            return None
        else:
            return self.regras


r = {'A': ['aA','a','B'], 'B': ['bB','b']}
g = Gramatica(r)
print(g)