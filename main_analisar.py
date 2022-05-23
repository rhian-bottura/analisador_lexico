from analisador_arquivos import analisando_arquivo
import tokeniza as tk
import operadores as op

PROMPT = "expressão >>> "
QUIT = "exit()"
def main():
    
    print("Bem vindo ao analisador léxico")
    while True:
        print("Escolha qual opção desejas! \n 1 - Analisar expressão \n 2 - Analisar arquivo \n 3 - Sair")
        inp = int(input(">> "))
        if inp == 3:
            break
        elif inp == 2:
            file_name = input("Por favor, digite o nome do arquivo que deseja processar :  ")
            analisador = analisando_arquivo(file_name)
            analisador.process()
        elif inp == 1:
            expressao = input(PROMPT)
            while expressao != QUIT:
                lista_tokens = tk.tokeniza(expressao)
                for token in lista_tokens:
                # pegue item e tipo
                    item, tipo = token

                # cri string com a descriçao
                    if tipo in [tk.OPERADOR, tk.PARENTESES]:
                        descricao = "'%s' : %s" %(item,op.DESCRICAO[item])
                    elif tipo == tk.VARIAVEL:
                        descricao = "'%s' : nome de variável" %item
                    elif tipo == tk.NUMERO:
                        descricao = "%f : constante float" %item
                    else:
                        descricao = "'%s' : categoria desconhecida" %item

                    # imprima a descriçao
                    print(descricao)

                    # leia próxima expressão    
                decisao = int(input("deseja analisar outra expressão ? \n 1 - Sim \n 2 - Não : "))
                if decisao == 1 :
                    
                    expressao = input(PROMPT)
                else :
                    break
            else :
                print("por favor digite um valor válido!") 

main()