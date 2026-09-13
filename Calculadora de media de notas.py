#Sistema de Gestão de Notas
 
#Função para calcular a média das nota
def media(notas):
    return sum(notas)/len(notas)

#Cadastro de notas
notas = [float(x) for x in input("Digite as notas separadas por vírgula: ").split(",")]

#Determinação da situação do aluno
if media(notas) >= 7:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

#Relatorio final
print("\n===== RELATÓRIO FINAL =====")
print("Notas:", notas)
print("Media:", round(media(notas)))
print("Situação:", situacao)