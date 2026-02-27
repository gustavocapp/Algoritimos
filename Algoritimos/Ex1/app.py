# "Leia um número inteiro e imprima o resultadoda diferença do seu triplo pelo dobro do seu sucessor"

num = int(input('Digite o número '))

suc = num + 1
resultado = (num * 3) - (suc * 2)
print('O Resultado é:', resultado)

# "Determine a área do triângulo"

base = int(input('Informe a base do triângulo: '))
altura = int(input('Informe a altura do triângulo: '))
result = (base * altura) / 2
print('O Resultado é: ', result)


# "Leia o sálario mensal atual de um funcionário e o percentual de reajuste e determine o novo salário"

salario = float(input('Dê o salário mensal: '))
percent = float(input('Informe o percentual de reajuste: '))

calc = salario * (percent / 100)
print('O valor do novo salário é: ', calc)

# "Calcule o volume do cubo"

aresta = float(input('Determine o valor da aresta do cubo: '))
volume = aresta ** 3
print('O volume do cubo é: ', volume)

# "Elabore um programa que dada uma distância percorrida em km, bem como o total de combustivel gasto em L. Informe o consumo do veiculo"

dist = float(input('informe a distância percorrida em km: '))
gasto = float(input('Informe o gasto de combustivel em L: '))

print('O gasto foi de: ', dist / gasto)

# "Calcule o preço para forrar a sala dado o comprimento, altura e preço do metro quadrado"

comprimento = float(input('Informe o comprimento da sala em metros: '))
largura = float(input('Informe a largura da sala em metros: '))

preco = float(input('Informe o preço do metro quadrado: '))

area = comprimento * largura 
print('O custo total foi: ', area * preco)

#-------------------------------------------------

peso = float(input('Informe o peso: '))
altura = float(input('Informe a sua altura: '))
imc = peso / (altura **2)
print('O IMC é igual a: ', imc)

#----------------------------------------------------

valor = float(input('Informe o valor do concurso em reais: '))
primeiro = valor * (46/100)
segundo = valor * (32/100)
terceiro = valor * (22/100)
print('A quantia ganha por cada um dos ganhadores é:\n', primeiro ,'R$\n', segundo, 'R$\n', terceiro,'R$')

#-------------------------------------------------------

valor_compra = float(input('Informe o valor da compra; '))
valor_pago = float(input('Informe o preço da compra'))

troco = valor_compra - valor_pago 

nota100 = int(troco / 100)
resto = troco % 100

nota50 = int(resto / 50)
resto = resto % 50

nota20 = int(resto / 20)
resto = resto % 20

nota10 = int(resto / 10)
resto = resto % 10

nota5 = int(resto / 5)
resto = resto % 5

nota1 = int(resto / 1)

print('Valor da compra: ', valor_compra, '\nValor pago: ', valor_pago, '\nTroco: ', troco)
print('Notas de 100:', nota100,
      'Notas de 50: ', nota50,
      'Notas de 20: ', nota20,
      'Notas de 10: ', nota10,
      'Notas de 5: ',nota5,
       'Notas de 1: ', nota1)