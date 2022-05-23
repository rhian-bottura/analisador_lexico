
# Constantes
from operator import le, ne
import re
from sunau import Error


TESTE   = False

# caracteres usados em operadores
OPERADORES = "%*/+-!^="

# caracteres usados em números inteiros
DIGITOS = "0123456789"

# ponto decimal
PONTO = "."

# todos os caracteres usados em um números float
FLOATS = DIGITOS + PONTO

# caracteres usados em nomes de variáveis
LETRAS  = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# abre e fecha parenteses
ABRE_FECHA_PARENTESES = "()"

# categorias
OPERADOR   = 1 # para operadores aritméticos e atribuição
NUMERO     = 2 # para números: todos são considerados float
VARIAVEL   = 3 # para variáveis
PARENTESES = 4 # para '(' e ')

# Whitespace characters: space, newline, horizontal tab,
# vertical tab, form feed, carriage return
BRANCOS    = [' ', '\n', '\t', '\v', '\f', '\r']

# caractere que indica comentário
COMENTARIO = "#"


#------------------------------------------------------------
def tokeniza(exp):
    """(str) -> list

    Recebe uma string exp representando uma expressão e cria 
    e retorna uma lista com os itens léxicos que formam a
    expressão.

    Cada item léxico (= token) é da forma
       
        [item, tipo]

    O componente item de um token é 

        - um float: no caso do item ser um número; ou 
        - um string no caso do item ser um operador ou 
             uma variável ou um abre/fecha parenteses.

    O componente tipo de um token indica a sua categoria
    (ver definição de constantes acima). 

        - OPERADOR;
        - NUMERO; 
        - VARIAVEL; ou 
        - PARENTESES

    A funçao ignora tuo que esta na exp apos o caractere
    COMENTARIO (= "#").
    """
    # escreva o seu código abaixo
    DELIMITADOR = ";"

    def agrupa_caracteres_var(i, exp):
        acumulado = i
        while i < len(exp):
            if exp[i] in LETRAS or exp[i] in DIGITOS:
                acumulado = i
                i += 1
            else:
                break
        return acumulado

    def agrupa_caracteres_float(i, exp):
        acumulado = i
        while i < len(exp):
            if exp[i] in DIGITOS or exp[i] in PONTO:
                acumulado = i
                i += 1
            else:
                break
        return acumulado

    lista_item_tipo = []

    i = 0
    while i < len(exp):
        atual = exp[i]
        if atual in OPERADORES:
            lista_item_tipo.append([atual, OPERADOR])
        elif atual in DIGITOS:
            proximo = agrupa_caracteres_float(i, exp)
            lista_item_tipo.append([float(exp[i:proximo+1]), NUMERO])
            i = proximo
        elif atual in LETRAS:
            proximo = agrupa_caracteres_var(i, exp)
            lista_item_tipo.append([exp[i:proximo+1], VARIAVEL])
            i = proximo
        elif atual in ABRE_FECHA_PARENTESES:
            lista_item_tipo.append([atual, PARENTESES])
        elif atual in COMENTARIO:
            break
        elif atual in BRANCOS or atual in DELIMITADOR:
            next
        else:
            raise Error(f"{atual} não é uma lexema reconhecido")
        i += 1

    return lista_item_tipo

def ler_arquivo_por_delimitador():
    DELIMITADOR = ";"
    lista_tokens = []
    arquivo_delimitado = open("./teste.txt", "r").read().split(DELIMITADOR)
    for exp in arquivo_delimitado:
        lista_tokens.append(tokeniza(exp))
    print(lista_tokens)

ler_arquivo_por_delimitador()