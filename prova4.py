num_alunos = int(input("Digite o número de alunos: "))

soma_medias = 0


for i in range(num_alunos):
    print("Digite as informações do aluno.")
    nome = input("Nome do aluno: ")
    
    soma_notas = 0
 
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
  
    soma_notas = nota1 + nota2 + nota3
    
    media = soma_notas / 3
    
    soma_medias += media
    
    if media >= 7.0:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    

    print(f"Nome: {nome}")
    print(f"Notas: {nota1}, {nota2}, {nota3}")
    print(f"Média: {media}")
    print(f"Situação: {situacao}")


media_geral = soma_medias / num_alunos


print(f"Média geral da turma: {media_geral}")  