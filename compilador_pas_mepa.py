import split_lexico_pas as lexico
from tradutor import Tradutor

lex = lexico.split_file('teste.pas')

# print(lex)

trd = Tradutor(lex)
trd.traduz()
