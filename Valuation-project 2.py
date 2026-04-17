version 0.02
###
# Entrada do nome
nome = input("Digite seu nome: ")
 
# Lista de linguagens
linguagens = ["Python", "Java", "C#"]
 
# ESCOLHA DA LINGUAGEM
while True:
    try:
        print("\nEscolha a linguagem:")
        print("1 - Python")
        print("2 - Java")
        print("3 - C#")
        print("0 - Sair")
 
        opcao = int(input("Digite a opção da linguagem: "))
 
        if opcao == 0:
            print("Saindo...")
            exit()
 
        if opcao < 1 or opcao > 3:
            print("Opção inválida.")
            continue
 
        linguagem_escolhida = linguagens[opcao - 1]
        break
 
    except ValueError:
        print("Entrada inválida. Você digitou uma letra.")
        continuar = input("Deseja continuar? (s/n): ").strip().lower()
        if continuar != "s":
            print("Programa encerrado.")
            exit()
 
# ESCOLHA DO RESULTADO
while True:
    try:
        print("\nEscolha o resultado:")
        print("1 - Se tornou um programador de sucesso")
        print("2 - Não se tornou um programador de sucesso")
 
        resultado = int(input("Digite a opção: "))
 
        if resultado < 1 or resultado > 2:
            print("Opção de resultado inválida.")
            continue
        break
 
    except ValueError:
        print("Entrada inválida. Digite apenas números.")
 
# HISTÓRIA - PARTE 1
print("\nPARTE 1 - A HISTÓRIA DE UM PROGRAMADOR\n")
print(f"Certa vez um jovem chamado {nome} resolveu programar do zero.")
print("Ele começou a estudar programação e gostou bastante.")
print(f"A linguagem que {nome} mais gostou foi {linguagem_escolhida}.")
print("Então decidiu se especializar nessa linguagem.")
 
if resultado == 1:
    print(f"E com isso {nome} se tornou um programador de sucesso em {linguagem_escolhida}.")
else:
    print(f"E com isso {nome} não se tornou um programador de sucesso em {linguagem_escolhida}.")
 
# HISTÓRIA - PARTE 2
if resultado == 2:
    print("\nPARTE 2 - O CAMINHO DIFÍCIL\n")
    print(f"Com o tempo, {nome} encontrou muitas dificuldades ao estudar {linguagem_escolhida}.")
    print("Os erros constantes o deixavam desmotivado.")
    print("Ele não praticava todos os dias e acabou desistindo.")
    print(f"E com isso {nome} não se tornou um programador de sucesso em {linguagem_escolhida}.")
else:
    print("\nPARTE 2 - O SUCESSO\n")
    print(f"{nome} estudou todos os dias e não desistiu.")
    print(f"E com isso {nome} se tornou um programador de sucesso em {linguagem_escolhida}.")
    print("E conseguiu um emprego incrível e ajudou sua família.")
 
print("\nHistória finalizada.")
 
