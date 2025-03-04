from datetime import datetime 

# Python object-Oriented Programming

# Classes
#     utilizado para criar objetos (Instancias)
#     Objeto sap ártes dentro de uma Classe (Instancias)
#     Classes sao utilizada para agrupar dados e funções,podendo reutilizar
#     =============
#     Class: Frutas 
#     objects: Abacate, Banana ...

#Criar a classe
class Funcionarios:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento
    
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome
    
    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento

            

#Criar o objeto
usuario1  = Funcionarios('Elena', 'Cabral', 2009)
usuario2  = Funcionarios('Carol', 'Silva', 2005)
usuario3  = Funcionarios('Andre', 'Iacono', 2003)


print(Funcionarios.idade_funcionario(usuario1))
print(Funcionarios.idade_funcionario(usuario2))
print(Funcionarios.idade_funcionario(usuario3))

 