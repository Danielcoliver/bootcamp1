
def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    else:
        return x / y
def menu():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
while True:
    menu()
    escolha = input("Escolha uma opção (1/2/3/4) ou 'q' para sair: ")
    if escolha == 'q':
        print("Encerrando a calculadora.")
        break
    if escolha in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if escolha == '1':
            print(f"Resultado: {num1} + {num2} = {adicionar(num1, num2)}")
        elif escolha == '2':
            print(f"Resultado: {num1} - {num2} = {subtrair(num1, num2)}")
        elif escolha == '3':
            print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
        elif escolha == '4':
            print(f"Resultado: {num1} / {num2} = {dividir(num1, num2)}")
    else:
        print("Opção inválida! Tente novamente.")
