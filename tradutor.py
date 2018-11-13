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
        self.identificadores = dict()
        self.id_len = 0
        self.mepa = list()
        self.mepa_len = 0
        self.mem_pos = -1

    def next_token(self):
        self.tk_pointer = self.tk_pointer + 1
        return self.tokens[self.tk_pointer]

    def next_end(self):
        self.mem_pos = self.mem_pos + 1
        return self.mem_pos

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
            token = self.next_token()
            if token['token'] == 'program':
                self.mepa.append('\tINPP')
                token = self.next_token()
                self.new_id(token['token'], 'program')
                token = self.next_token()  # avanca o ;
            elif token['token'] == 'var':
                vravs = list()
                token = self.next_token()
                while token['token'] != ':':
                    if token['type'] == 'identificador':
                        vravs.append(token['token'])
                        self.new_id(token['token'])
                    token = self.next_token()
                token = self.next_token() # aqui token recebe o tipo das variaveis
                for v in vravs:
                    # self.change_id(v, token['token']) # inserindo o tipo
                    self.identificadores[v]['type'] = token['token']

                self.mepa.append('\tAMEM '+str(len(vravs)))
                token = self.next_token()  # avanca o ;
            elif token['token'] == 'read':
                self.mepa.append('\tLEIT')
                token = self.next_token() # avanca o (
                token = self.next_token() # recebe o identificador
                self.mepa.append(
                    '\tARMZ '+str(self.identificadores[token['token']]['end']))
                token = self.next_token()  # avanca o )
                token = self.next_token()  # avanca o ;
            elif token['type'] == 'identificador':
                pass


        print(self.identificadores)
        print(self.mepa)
