version 0.0.1
######
# Entrada do nome
nome = input("Digite seu nome: ")

# Lista de linguagens
linguagens = ["Python", "Java", "C#"]
while True:
    print("\nEscolha a linguagem:💻")
    print("1 - Python")
    print("2 - Java")
    print("3 - C#")
    print("0 - não quero escolher uma linguagem , finalizar programa😒")
    opcao = int(input("Digite a opção da linguagem: "))

    if opcao == 0:
        print("Saindo...")
        break

# Validação da linguagem
    if opcao < 1 or opcao > 3:
     print("Opção de linguagem inválida!")
    else:
     linguagem_escolhida = linguagens[opcao - 1]

# Escolha do resultado
    print("\nEscolha o resultado:")                        
    print("1 - Se tornou um programador de sucesso")
    print("2 - Não se tornou um programador de sucesso")

    resultado = int(input("Digite a opção: "))

    if resultado < 1 or resultado > 2:
        print("Opção de resultado inválida!")
        
    else:
#História
        print("\nPARTE 1 -A HISTORIA DE UM PROGRAMADOR\n")

        print(f"Certa vez um jovem chamado {nome} resolveu programar do zero.")
        print(f"Ele começou a estudar programação e gostou bastante.")
        print(f"A linguagem que {nome} mais gostou foi {linguagem_escolhida}.")
        print(f"Então decidiu se especializar nessa linguagem.")
#Final da história
        if resultado == 1:
            print(f"E com isso {nome} se tornou um programador de sucesso em {linguagem_escolhida}! 🤑")
        else:
            print(f"E com isso {nome} não se tornou um programador de sucesso em {linguagem_escolhida}. 😢")
#PARTE 2
    if resultado == 2:
        print("\nPARTE 2 - O CAMINHO DIFÍCIL\n")
        print(f"Com o tempo, {nome} encontrou muitas dificuldades ao estudar {linguagem_escolhida}.")
        print("Os erros constantes o deixavam desmotivado.")
        print("Ele não praticava todos os dias e acabou desistindo.")
        print(f"E com isso {nome} não se tornou um programador de sucesso em {linguagem_escolhida}. 😢")
    else:
        print("\nPARTE 2 - O SUCESSO\n")
        print(f"{nome} estudou todos os dias e não desistiu.")
        print(f"E com isso {nome} se tornou um programador de sucesso em {linguagem_escolhida}! 🤑")
        print(f"E com isso {nome} conseguiu um emprego incrivel e ajudou  sua familia.")

        while True:
           print("historia finalizada")
           break

        
imagem1="------------------------------------------------------------------"
imagem1+="\n,---,---,---,---,---,---,---,---,---,---,---,---,---,-------"
imagem1+="\n|1/2| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 | + | ' |  <--  |"
imagem1+="\n|---'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,---------|"
imagem1+="\n| -&gt;| | Q | W | E | R | T | Y | U | I | O | P | ] | <--- |"
imagem1+="\n|-----',--',--',--',--',--',--',--',--',--',--',--',--'|  | |"
imagem1+="\n| Caps | A | S | D | F | G | H | J | K | L | \ | [ | * |    |"
imagem1+="\n|----,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'---'--------|"
imagem1+="\n|    | &lt; | Z | X | C | V | B | N | M | , | . | - |    ^  |"
imagem1+="\n|----'-,-',--'--,'---'---'---'---'---'---'-,-'---',--,------|"
imagem1+="\n| ctrl |  | alt |                          |altgr |  | ctrl |"
imagem1+="\n-------------------------------------------------------------"

print(imagem1)
