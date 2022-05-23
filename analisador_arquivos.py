import csv
from ntpath import join
class analisando_arquivo():
    def __init__(self, file_name):
        self.file_name = file_name
    
    def process(self):
        try:
            rows = []
            with open(self.file_name, mode = "r") as csv_file:
                csvreader = csv.DictReader(csv_file, delimiter=';')        
                count = 0
                for row in csvreader:
                    print("-----------------------------------------------------")
                    print("Nome: " + str(count) + " ", end="")
                    print({row["nome"]})
                    print("Idade: " + str(count)  + " ", end="")
                    print({row["idade"]})
                    print("Logradouro: " + str(count)  + " ", end="")
                    print({row["logradouro"]})
                    print("Numero: " + str(count)  + " ", end="")
                    print({row["numero"]})
                    print("Complemento: " + str(count)  + " ", end="")
                    print({row["complemento"]})
                    print("Cidade: " + str(count) + " ", end="")
                    print({row["cidade"]})
                    print("Estado: " + str(count)  + " ", end="")
                    print({row["estado"]})
                    print("Pais: " + str(count)  + " ", end="")
                    print({row["pais"]})
                    count = count + 1
                    rows.append(row)
            print("Registros lidos = " + str(count))
        except Exception:
            print("Erro: arquivo nao encontrado")
        return rows
        
        

