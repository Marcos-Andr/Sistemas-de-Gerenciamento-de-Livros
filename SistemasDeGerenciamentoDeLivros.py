#Sistemas de Gerenciamento de Livros

#Criação da classe Livros com os atributos título, autor, gênero e quantidade
class Livros:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

#Lista para armazenar os livros cadastrados
livros_cadastrados = []

#Sistema de cadastro de livros
def cadastrar_livro():
    print("\n--- CADASTRO DE LIVRO ---")
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    genero = input("Digite o gênero do livro: ")
    quantidade = int(input("Digite a quantidade de exemplares: "))
    
    livro = Livros(titulo, autor, genero, quantidade)
    livros_cadastrados.append(livro)
    print(f"Livro '{titulo}' cadastrado com sucesso!")

#Sistema de listagem de livros
def listar_livros():
    print("\n--- LISTA DE LIVROS ---")
    if not livros_cadastrados:
        print("Nenhum livro cadastrado ainda.\n")
        return
    for livro in livros_cadastrados:
        print(f"Título: {livro.titulo}")
        print(f"Autor: {livro.autor}")
        print(f"Gênero: {livro.genero}")
        print(f"Quantidade: {livro.quantidade}")
        print("-" * 30)

#Sistema de busca de livros por título
def buscar_livro_por_titulo():
    print("\n--- BUSCA DE LIVRO ---")
    titulo = input("Digite o título do livro que deseja buscar: ")
    for livro in livros_cadastrados:
        if livro.titulo.lower() == titulo.lower():
            print(f"Título: {livro.titulo}")
            print(f"Autor: {livro.autor}")
            print(f"Gênero: {livro.genero}")
            print(f"Quantidade: {livro.quantidade}")
            return
    print("Livro não encontrado.")

#Grafico de quantidade de livros por gênero
import matplotlib.pyplot as plt

def gerar_grafico():
    if not livros_cadastrados:
        print("\nCadastre livros antes de gerar o gráfico.\n")
        return
    
    generos = {}
    for livro in livros_cadastrados:
 # Garante que gêneros parecidos contem juntos
        genero_padrao = livro.genero.strip().title()
        generos[genero_padrao] = generos.get(genero_padrao, 0) + livro.quantidade

    plt.bar(generos.keys(), generos.values())
    plt.xlabel("Gênero")
    plt.ylabel("Quantidade de livros")
    plt.title("Quantidade de livros por gênero")
    plt.show()

# MENU PRINCIPAL INTERATIVO NO TERMINAL
def menu():
    while True:
        print("====== SISTEMA DE GERENCIAMENTO DE LIVROS ======")
        print("[1] Cadastrar Livro")
        print("[2] Listar Livros")
        print("[3] Buscar Livro por Título")
        print("[4] Gerar Gráfico por Gênero")
        print("[0] Sair do Programa")
        print("================================================")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            buscar_livro_por_titulo()
        elif opcao == "4":
            gerar_grafico()
        elif opcao == "0":
            print("\nEncerrando o sistema. Até logo!")
            break
        else:
            print("\nOpção inválida! Escolha um número de 0 a 4.\n")

# Executa o programa
if __name__ == "__main__":
    menu()