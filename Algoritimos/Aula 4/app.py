def ex1():
    idade = int(input("Qual a sua idade?"))
    if idade >= 18 and idade <=67:
        print("Pode realizar o exame")
    else:
        print("Não pode realizar o exame")

def ex2():
    x = int(input("Qual o valor de X: "))
    y = int(input("Qual o valor de Y: "))
    z = int(input("Qual o valor de Z: "))

    if x < z and y > z:
        print("Dentro do intervalo definido")
    else:
        print("Fora do intervalo definido")

def ex3():
    a= int(input("Qual o valor de A: "))
    b = int(input("Qual o valor de B: "))
    c = int(input("Qual o valor de C: "))
    nums = [a,b,c]
    nums.sort()
    print(nums)

def ex4():
    salario = float(input("Digite o salário: "))
    plano = float(input("Informe o plano desejado: "))

    match plano:
        case 1:
            print("O Salário recebeu amuemnto de 10%: ", salario * (10/100))
        case 2:
            print("O Salário recebeu amuemnto de 20%: ", salario * (20/100))
        case 3:
            print("O Salário recebeu amuemnto de 30%: ", salario * (30/100))

def ex5():
    x = int(input("Informe o número base (Valor inteiro não negativo)"))
    n = int(input("Informe o expoente"))
    resultado = 1
    i = 0

    while i < n:
        resultado = resultado * x
        i += 1
    return resultado
print(ex5())