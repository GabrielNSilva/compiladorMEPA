class Tradutor():
    '''
        Tradutor da linguagem pascal para MEPA.
        Funciona somente com codigo sintaticamente correto e com os tokens previamente separados

        Args:
            tokens: dict() | tokens separado e classificados
    '''

    def __init__(self, tokens):
        self.tokens = tokens
        self.tk_len = len(tokens)
        self.tk_pointer = -1
        self.token = None
        self.identificadores = dict()
        self.id_len = 0
        self.mepa = list()
        self.mepa_len = 0
        self.mem_pos = -1

    def next_token(self):
        self.tk_pointer = self.tk_pointer + 1
        self.token = self.tokens[self.tk_pointer]
        return self.token

    def next_end(self):
        self.mem_pos = self.mem_pos + 1
        return self.mem_pos

    def get_end(self, token):
        return self.identificadores[token['token']]['end']

    def new_id(self, name_id, type_id=None):#, val_id=None):
        # if val_id == None:
        #     if type_id == 'integer':
        #         val_id = 0
                
        self.identificadores[name_id] = {
            # 'value': val_id,
            'type': type_id,
            'end': self.next_end()
        }

    # def change_id(self, name_id, type_id=None):#, val_id=None):
        # if val_id != None:
        #     self.identificadores[name_id]['value']: val_id
        # if type_id != None:
            # self.identificadores[name_id]['type']: type_id

    def traduz(self):
        '''
            Faz a traducao do dict tokens para MEPA

            Returns:
                mepa: list() | lista contendo cada linha do codigo mepa gerado
        '''

        while self.tk_pointer < self.tk_len-1:
            self.next_token()
            if self.token['token'] == 'program':
                self.mepa.append('    INPP')
                self.next_token()
                self.new_id(self.token['token'], 'program')
                self.next_token()  # avanca o ;
            elif self.token['token'] == 'var':
                vravs = list()
                self.next_token()
                while self.token['token'] != ':':
                    if self.token['type'] == 'identificador':
                        vravs.append(self.token['token'])
                        self.new_id(self.token['token'])
                    self.next_token()
                self.next_token() # aqui token recebe o tipo das variaveis
                for v in vravs:
                    # self.change_id(v, self.token['token']) # inserindo o tipo
                    self.identificadores[v]['type'] = self.token['token']

                self.mepa.append('    AMEM '+str(len(vravs)))
                self.next_token()  # avanca o ;
            elif self.token['token'] == 'read':
                self.mepa.append('    LEIT')
                self.next_token() # avanca o (
                self.next_token() # recebe o identificador
                self.mepa.append('    ARMZ '+str(self.get_end(self.token)))
                self.next_token()  # avanca o )
                self.next_token()  # avanca o ;
            elif self.token['token'] == 'write':
                self.next_token() # avanca o (
                self.next_token() # recebe o identificador
                self.mepa.append('    CRVL '+str(self.get_end(self.token)))
                self.mepa.append('    IMPR')
                self.next_token()  # avanca o )
                self.next_token()  # avanca o ;
            elif self.token['type'] == 'identificador':
                # print(self.token)
                armz = self.get_end(self.token)
                if (self.next_token()['token'] == ':' and self.next_token()['token'] == '='):
                    pilha = self.shunting_yard()
                    pilha.append('    ARMZ '+str(armz))
                    self.mepa = self.mepa + pilha
                # print(pilha)


        # print(self.identificadores)
        print()
        for l in self.mepa:
            print(l)

    def shunting_yard(self):
        sequence = list()
        operators = list()
        while self.next_token()['token'] != ';':
            # read a token.
            if self.token['type'] == 'constante':
                sequence.append('    CRCT '+self.token['token'])
            if self.token['type'] == 'identificador':
                sequence.append('    CRVL '+str(self.get_end(self.token)))
            # # if self.token is a function then:
            # if self.token['type'] == 'palavra_reservada':
            #     push it onto the operator stack 
            if self.token['type'] == 'simbolo_especial':
                # while (
                    # (there is a function at the top of the operator stack) or
                    # (there is an operator at the top of the operator stack with greater precedence) or
                    # (the operator at the top of the operator stack has equal precedence and is left associative)) and
                    # (the operator at the top of the operator stack is not a left bracket):
                    # pop operators from the operator stack onto the output queue.
                if self.token['token'] == '+':
                    operators.append('    SOMA')
                elif self.token['token'] == '-':
                    operators.append('    SUBT')
                elif self.token['token'] == '*':
                    operators.append('    MULT')
                elif self.token['token'] == '/':
                    operators.append('    DIVI')
            if self.token['token'] == '(':
                operators.append('(')
            if self.token['token'] == ')':
                aux = operators.pop()
                while aux != '(':
                    sequence.append(aux)
                    aux = operators.pop()
                # if the stack runs out without finding a left bracket, then there are mismatched parentheses.
        # if there are no more tokens to read:
        while len(operators):
            # if the operator token on the top of the stack is a bracket, then there are mismatched parentheses.
            sequence.append(operators.pop())
        return sequence
