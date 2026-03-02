fahrenheit = float(input('Digite a temperatura em fahrenheit para a conversão: '))
print('A temperatura em graus é:', (fahrenheit - 32) * 5/9)

#----------------------------------

dolar = 5.21
valor = float(input('Digite o valor em dolar: '))
print('O valor em reais é: ', valor * dolar)

#----------------------------------

km = float(input('km/h: '))
print('A conversão de km pra metros é: ', km/3.6)

#----------------------------------

contrato = int(input('Solicite o número de dias que o encanador deverá vir: '))
print('O valor do contrato é: ', (contrato * 30) * (8/100))

#----------------------------------

hdegrau = float(input('informe a altura do degrau em m: '))
hescada = float(input('Informe a altura desejada: '))
print('a quantidade de degraus é igual a: ', hescada / hdegrau)

#----------------------------------

tempo = float(input('Informe o tempo da viagem: '))
vm = float(input('Informe a velocidade média: '))
dist = vm * tempo
consumo = dist / 12
print('Informações da viagem: ', vm, tempo, dist, consumo)